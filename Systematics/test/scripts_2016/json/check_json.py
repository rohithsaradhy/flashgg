#!/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_8/external/slc7_amd64_gcc700/bin/python3


import subprocess
import json


# cmd = ["fggManageSamples.py", "-C", "Era2017_RR-31Mar2018_v2",  "list", "'*TTGJets*'"]
cmd = ["fggManageSamples.py", "-C", "Era2016_RR-17Jul2018_v2",  "list"]

# result = subprocess.run(['which','fggManageSamples.py'], stdout=subprocess.PIPE)

result = subprocess.run(cmd, stdout=subprocess.PIPE)
# print(result.stdout.decode('utf-8'))




print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Signal MC")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
f = open('sig.json')
data = json.load(f)
total_found=0
for p in data['processes'].keys():
    dat = data['processes'][p]
    file_name = dat[0]
    # print(file_name)
    # break
    found =False
    for link in result.stdout.decode("utf-8").split('\n'):
        if link.find(file_name) != -1:
            
            if link.split(" ")[0] == file_name:
                found = True
                total_found = total_found + 1
                print ('Found:',link)
            # else:
            #     print ('Partially Found:',link)
    if found == False:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Not Found:", file_name)
        print('Please check the full name in json')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print('Found/Total:', total_found,'/',len(data['processes'].keys()))



print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("BKG MC")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
f = open('bkg.json')
data = json.load(f)
total_found=0
for p in data['processes'].keys():
    dat = data['processes'][p]
    file_name = dat[0]
    # print(file_name)
    # break
    found =False
    for link in result.stdout.decode("utf-8").split('\n'):
        if link.find(file_name) != -1:
            
            if link.split(" ")[0] == file_name:
                found = True
                total_found = total_found + 1
                print ('Found:',link)
            # else:
            #     print ('Partially Found:',link)
    if found == False:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Not Found:", file_name)
        print('Please check the full name in json')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print('Found/Total:', total_found,'/',len(data['processes'].keys()))


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("WH ANOM MC")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
f = open('wh_anom.json')
data = json.load(f)
total_found=0
for p in data['processes'].keys():
    dat = data['processes'][p]
    file_name = dat[0]
    # print(file_name)
    # break
    found =False
    for link in result.stdout.decode("utf-8").split('\n'):
        if link.find(file_name) != -1:
            
            if link.split(" ")[0] == file_name:
                found = True
                total_found = total_found + 1
                print ('Found:',link)
            # else:
            #     print ('Partially Found:',link)
    if found == False:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Not Found:", file_name)
        print('Please check the full name in json')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print('Found/Total:', total_found,'/',len(data['processes'].keys()))



print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("ZH ANOM MC")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
f = open('zh_anom.json')
data = json.load(f)
total_found=0
for p in data['processes'].keys():
    dat = data['processes'][p]
    file_name = dat[0]
    # print(file_name)
    # break
    found =False
    for link in result.stdout.decode("utf-8").split('\n'):
        if link.find(file_name) != -1:
            
            if link.split(" ")[0] == file_name:
                found = True
                total_found = total_found + 1
                print ('Found:',link)
            # else:
            #     print ('Partially Found:',link)
    if found == False:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Not Found:", file_name)
        print('Please check the full name in json')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print('Found/Total:', total_found,'/',len(data['processes'].keys()))