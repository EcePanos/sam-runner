import csv
import git
import sam_auto_invoke
import shutil
import os
from pathlib import Path
import signal
import time
import sys
import fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root))
    return result


def handler(signum, frame):
    print("Clone is taking too long")
    raise Exception("Skipping")


def run_all(diff_file):
    results = []
    repos = {}
    with open(diff_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    path = 'test'
    if Path(path).exists():
        shutil.rmtree(path)
    if Path('testdata.yaml').exists():
        os.remove('testdata.yaml')
    index = 0
    for item in results:
        if 'github' in item[6]:
            if 'tree' in item[6]:
                item[6] = item[6].split('/tree')[0]
            if item[6] not in repos.values():
                repos.update({item[0]:item[6]})
    #print(repos)

    for key in repos:
        with open('logs.txt','a') as f:
            f.write(str(index) + '\n')
            f.write(key + '\n')
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(40)
        try:
            git.Repo.clone_from(repos[key], path)
        except Exception as exc:
            print(exc)
        signal.alarm(0)
        template_paths = find('template.*',path)
        for application in template_paths:
            with open('logs.txt','a') as f:
                f.write(application + '\n')
                f.write(str(index) + '\n')
            sam_auto_invoke.autorun(application)
            index+=1
            with open('logs.txt','a') as f:
                f.write('---------------------------' + '\n')
        if Path('testdata.yaml').exists():
            os.remove('testdata.yaml')
        if Path(path).exists():
            try:
                shutil.rmtree(path)
            except:
                path = 'test' + str(index)
        index+=1
        with open('logs.txt','a') as f:
            f.write('---------------------------' + '\n')
    
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        run_all(sys.argv[1])
    else:
        print("No input file specified")
