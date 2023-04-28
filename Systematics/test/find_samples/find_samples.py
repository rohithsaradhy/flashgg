#!/cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_6_29/external/slc7_amd64_gcc700/bin/python3

UL_dict={
    'UL18_Summer19'         :   'Era2018_legacy_v1_Summer19UL',
    'UL18_Summer20'         :   'Era2018_legacy_v1_Summer20UL',
    'UL17_Summer19'         :   'Era2017_legacy_v1_Summer19UL',
    'UL17_Summer20'         :   'Era2017_legacy_v1_Summer20UL',
    'UL16_Summer19_PreVPF'  :   'Era2016_legacyPreVFP_v1_Summer19UL',
    'UL16_Summer20_PreVPF'  :   'Era2016_legacyPreVFP_v1_Summer20UL',
    'UL16_Summer19_PostVFP' :   'Era2016_legacyPostVFP_v1_Summer19UL',
    'UL16_Summer20_PostVFP' :   'Era2016_legacyPostVFP_v1_Summer20UL'
}


ac_sample_names=[
#WH
"WHiggs0L1ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"WHiggs0L1f05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"WHiggs0MToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"WHiggs0Mf05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"WHiggs0PHToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"WHiggs0PHf05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"WHiggs0PMToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
#ZH
"ZHiggs0L1ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0L1ZgToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0L1Zgf05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0L1f05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0MToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0Mf05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0PHToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0PHf05ph0ToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8",
"ZHiggs0PMToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8"
]

sig_sample_names=[
"VHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8",
"GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8_storeWeights",
"ttHJetToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_storeWeights",
"VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8_storeWeights"
]


bkg_sample_names=[
"DYJetsToLL_M-50",
"DiPhotonJetsBox_M40",
"DiPhotonJetsBox_MGG-80toInf",
"GJet_Pt-20to40",
"GJet_Pt-40toInf",
"TTGJets_TuneCP5",
"TTJets_TuneCP5",
"WGToLNuG_01J",
"WW_TuneCP5",
"WZ_TuneCP5",
"ZGToLLG_01J",
"ZZ_TuneCP5",
"TGJets_TuneCP5",
"TTGG_0Jets",
]

import os
import sys
import subprocess

def find_sample(era,sample): #given a era and sample, check if it is in the tmp files created by capture_all_samples.sh
    with open(f"./tmp/{era}.txt") as f:
        instances_found = 0
        for line in f.readlines():
            if sample in line:
                # print("yes")
                instances_found+=1
                print(line)
        print(f"Instances found = {instances_found}")        
    return instances_found


def runEraCheck(era): #Checks if everything is available...
    out_dict = {}
    for sample in ac_sample_names + sig_sample_names + bkg_sample_names:
        out_dict[sample] = 0
        with open(f"./tmp/{era}.txt") as f:
            for line in f.readlines():
                if sample in line:
                    out_dict[sample] += 1


    print("$"*50)
    print("AC SAMPLE")
    print("$"*50)
    for sample in ac_sample_names :
        print(f"{sample:80}:{out_dict[sample]:10}")
    print("$"*50)
    print("SIG SAMPLE")
    print("$"*50)
    for sample in sig_sample_names:
        print(f"{sample:80}:{out_dict[sample]:10}")
    print("$"*50)
    print("BKG SAMPLE")
    print("$"*50)
    for sample in bkg_sample_names:
        print(f"{sample:80}:{out_dict[sample]:10}")
    pass








if len(sys.argv) == 3:
    # print (sys.argv)
    find_sample(sys.argv[1],sys.argv[2])
elif len(sys.argv) == 2:
    runEraCheck(sys.argv[1])
elif len(sys.argv) == 1: # Check all the 
    for key in UL_dict:
        print("$"*50)
        print(key)
        print("$"*50)
        runEraCheck(UL_dict[key])
    