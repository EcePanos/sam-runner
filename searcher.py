import os, fnmatch
import csv


# Test file to check the traversal Functions

# Find the template in an application's repository
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root))
    return result

app_list = find('template.*', 'serverless-application-model')
print(len(app_list))
print(app_list)
#for item in app_list:
    #sam_auto_invoke.autorun(item)

# Find repositories in the data dump -> works
# 'Fix' invalid links -> works
# and avoid duplicates -> may not work
results=[]
repos=[]
with open('autocontents-2019-04-24.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        results.append(row)
for item in results:
    if 'tree' in item[6]:
        item[6] = item[6].split('tree')[0]
    if item[6] not in repos:
        repos.append(item[6])
print(repos)
