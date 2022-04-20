#!/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_8/external/slc7_amd64_gcc700/bin/python3
import glob
import os





def combine_roots(file_folder,save_folder): #Will not work for Backgrounds
    samples = []
    samples_files = []
    for file in glob.glob(file_folder):
        file_name = file.split("/")[-1]  
        sample_name = file_name.split("_")[1]    
        if sample_name not in samples:
            samples.append(sample_name)
            samples_files.append(file )




    # print(samples_files[0])
    # for sample in samples:
    # hadd_string = 'hadd '
    os.system(f'mkdir -p {save_folder}')
    # os.system(f'which hadd')
    for sample in samples:
        hadd_string = 'hadd '
        hadd_string +=f"{save_folder}{sample}.root "
        hadd_string +=f"{file_folder.split('*')[0]}output_{sample}*root"
        
        # print(hadd_string)
        os.system(f'{hadd_string}')

    # print(samples)



file_folder = 'scripts_all/all/*root'
save_folder = 'Era2018RR_All/all/'
combine_roots(file_folder,save_folder)

# file_folder = 'scripts_2018/zh_anom/*root'
# save_folder = 'Era2018RR/zh_anom/'
# combine_roots(file_folder,save_folder)


# file_folder = 'scripts_2018/sig/*root'
# save_folder = 'Era2018RR/sig/'
# combine_roots(file_folder,save_folder)


# file_folder = 'scripts_2018/bkg/*root'
# save_folder = 'Era2018RR/bkg/'
# combine_roots(file_folder,save_folder)