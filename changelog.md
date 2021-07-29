## Changes not yet commited... Keeping track of files and changes
### Clean up this file after every commit


## Notes 
Commit Generated data for 2021_04_15_Output
This was run for 2018 RR dataset.



## Changes made:

./set_environment.sh
 - Created file to set cmsenv and $X509_USER_PROXY

 ./proxy.sh
 - Edited to use set_environment.sh

./MetaData/data/cross_sections.json
- Updated WGToLNuG_TuneCP5_13TeV dataset xsec to 1

./Systematics/test/WH_anom_dumper.py
 - Changed mu2_ph1 --> mu2_phi

## Files Edited
./Systematics/test/WH_anom_dumper.py

## Created bgk json and data json
./Systematics/test/json/*
bkg jobs json
bkg2 has the rest of the samples (Didn't find it first, but later found it and added to bkg2 json):
 	"ZGammaTo2LGamma" : [["/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"],{"args" :["outputFile=output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"]}] 
    "TTgammaJets"  : [["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8"],{"args" :["outputFile=output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"]}]
    "DiPhoton_80ToInf"  : [["/DiPhotonJetsBox_M40_80-Sherpa"],{"args" :["outputFile=output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"]}],
    "DYToLL"  : [["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"],{"args" :["outputFile=output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"]}],
    "TTGammaGamma_ZeroJets"  : [["/TTGG_0Jets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8"],{"args" :["outputFile=output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"]}],
    "TGammaJets"  : [["/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8"],{"args" :["outputFile=output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"]}]

bk3 has missing channels from bkg, & bkg2
 -      "ttjets"  : ["/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8"],
        "WGammaToLNuGamma"  : ["/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8"],
        "DYToLL"  : ["/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8"]


added separate channels for ttjets, DYToLL, WGammaToLNuGamma


data json is kept in (Additional cmsRun arguments were added):
./Systematics/test/json/legacy_runII_v2_2018_final.json
- removed 

        "vbf_120" : [ "/VBFHToGG_M120_13TeV_amcatnlo_pythia8" ],
        "vbf_125" : [ "/VBFHToGG_M125_13TeV_amcatnlo_pythia8" ],
        "vbf_130" : [ "/VBFHToGG_M130_13TeV_amcatnlo_pythia8" ],
        "ggh_120" : [ "/GluGluHToGG_M120_TuneCP5_13TeV-amcatnloFXFX-pythia8" ],
        "ggh_125" : [ "/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8" ],
        "ggh_130" : [ "/GluGluHToGG_M130_TuneCP5_13TeV-amcatnloFXFX-pythia8" ],
        "zh_120"  : [ [ "/VHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8", { "args" :["outputFile=output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8.root"] } ] ],
        "zh_125"  : [ [ "/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8", { "args" :["outputFile=output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root"] } ] ],
        "zh_130"  : [ [ "/VHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8", { "args" :["outputFile=output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8.root"] } ] ],
        "tth_120" : [ "/ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8/spigazzi-Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-20759e3d08a46e955aa3c86f42facf93/USER" ],
        "tth_125" : [ "/ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8" ],
        "tth_130" : [ "/ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8" ]


## Created scripts for job submissions
./Systematics/test/script_bkg.sh
./Systematics/test/script_bkg2.sh
./Systematics/test/script_bkg3.sh
- created a third bkg3 script

./Systematics/test/script_bkg_DYToLL.sh 
./Systematics/test/script_bkg_TTJet.sh
./Systematics/test/script_bkg_WGammaToLNuGamma.sh
-created a separate script for these three, and changed queue to tomorrow

./Systematics/test/script_data.sh
 - changed maxEvents to -1


## To Do
Add the variables from flasgg.Systematics/python folder. 
Add met variables

# Git Files
./Systematics/test/json/* ./Systematics/test/WH_anom_dumper.py ./Systematics/test/WH_anom_dumper.py Systematics/test/script_bkg.sh ./Systematics/test/script_data.sh ./Systematics/test/script_bkg2.sh ./Systematics/test/script_bkg3.sh ./set_environment.sh ./proxy.sh ./changelog.md ./MetaData/data/cross_sections.json ./Systematics/test/script_bkg_DYToLL.sh ./Systematics/test/script_bkg_TTJet.sh ./Systematics/test/script_bkg_WGammaToLNuGamma.sh
