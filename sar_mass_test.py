import csv
import git
import sam_auto_invoke
import shutil
import os
from pathlib import Path
import signal
import time


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
        if 'github' in item[6] and 'tree' not in item[6] and 'packs' not in item[6]:
            print(index)
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(30)
            try:
                git.Repo.clone_from(results[index][6], path)
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
