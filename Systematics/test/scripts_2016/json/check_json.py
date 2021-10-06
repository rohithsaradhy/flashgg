#!/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_8/external/slc7_amd64_gcc700/bin/python3


from json.decoder import JSONDecoder
import subprocess
import json



cmd = ["fggManageSamples.py", "-C", "Era2016_RR-17Jul2018_v2",  "list", 'raw']
# cmd = ["fggManageSamples.py", "-C", "Era2017_RR-31Mar2018_v2",  "list", 'raw']
# cmd = ["fggManageSamples.py", "-C", "Era2017_legacy_v1",  "list", 'raw']
# cmd = ["fggManageSamples.py", "-C", "Era2018_RR-17Sep2018_v2",  "list", 'raw']

result = subprocess.run(cmd, stdout=subprocess.PIPE)

def test_json(json_file):
    f = open(json_file)
    data = json.load(f)
    total_found=0
    for p in data['processes'].keys():
        total_file_in_process = 0
        dat = data['processes'][p]
        file_name = dat[0]
        print("$$$$$$$$$$$$$$ BEGIN:",file_name.split('/')[1],"$$$$$$$$$$$$$$")
        # break
        found =False
        similar_files = []
        exact_name_files = []
        for link in result.stdout.decode("utf-8").split('\n'):
            if link.find(file_name) != -1:
                similar_files.append(link)
                # print("filenames:",link)
                total_file_in_process +=1
                # print(link.split(" ")[0].split('/')[1])
                # print(file_name.split('/')[1])

                if link.split(" ")[0].split('/')[1] == file_name.split('/')[1]:
                    found = True
                    total_found = total_found + 1
                    exact_name_files.append(link)

        
        if total_file_in_process > 1 and found==True:
            print("Exact Match Found; More than one file found though:")
            
            print("Files with exact names: ",len(exact_name_files))
            if len(exact_name_files) > 1:
                for file in exact_name_files:
                    name = file.split('/')[1]
                    print('Root Name:',name)
                    print('Fullname :',file)
                    print("$$$$$$$$")

            print('Files with non exact names:',len(similar_files))
            for file in similar_files:
                name = file.split('/')[1]
                print('Root Name:',name)
                print('Fullname :',file)
                print("$$$$$$$$")
        
        elif total_file_in_process > 1 and found==False:
            print("No Exact Matches were Found; Files found: ",len(similar_files))
            for file in similar_files:
                name = file.split('/')[1]
                print('Root Name:',name)
                print('Fullname :',file)
                print("$$$$$$$$") 
        
        elif total_file_in_process == 1 and found==True:
            print('SUCCESS::Exact Match Found Once:')
            for file in similar_files:
                name = file.split('/')[1]
                print('Root Name:',name)
                print('Fullname :',file)
                print("$$$$$$$$")
        
        elif total_file_in_process == 0  and found == False:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("Exact Name Not Found:", file_name)
            print('Double Check')
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")



        print("$$$$$$$$$$$$$$ END:",file_name.split('/')[1],"$$$$$$$$$$$$$$")
        print('')
        print('')
        print('')
        






print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# test_json('sig.json')
# test_json('bkg.json')
# test_json('wh_anom.json')
test_json('zh_anom.json')

