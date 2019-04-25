import csv
import git
import sam_auto_invoke
import shutil
import os
from pathlib import Path
import signal
import time
import sys


def handler(signum, frame):
    print("Clone is taking too long")
    raise Exception("Skipping")


def run_all(diff_file):
    results = []
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
        #if 'github' in item[6] and 'tree' not in item[6] and 'packs' not in item[6]:
        if 'github' in item[6]:
            if 'tree' in item[6]:
                item[6] = item[6].split('tree')[0]
            print(index)
            print(item[0])
            with open('logs.txt','a') as f:
                f.write(str(index) + '\n')
                f.write(item[0] + '\n')
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(40)
            try:
                git.Repo.clone_from(item[6], path)
            except Exception as exc:
                print(exc)
            signal.alarm(0)
            sam_auto_invoke.autorun(path)
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
