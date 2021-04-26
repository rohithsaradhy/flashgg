## Changes not yet commited... Keeping track of files and changes
### Clean up this file after every commit


## Changes made:
./README.org
- Edited the readme to change the git clone repo src to rohithsaradhy/flashgg

./proxy.sh
- Created file proxy.sh to create a voms-proxy as ~/myproxy & run cmsenv

.gitignore
- Edited to not include ./vh-anomalous folder

./DataFormats/interface/WHLeptonicTag.h
- Added public functions and private variables to include WH BDT Variable (WHmva & WHptV)


./DataFormats/src/classes_def.xml
- Edited WHLeptonicTag Class to version 13 with checksum 2048958826

./MetaData/data/cross_sections.json
- Updated the cross_sections file to include WH Anomalous files...


./Systematics/test/WH_anom_dumper.py
- Edited from workspaceStd.py
<!-- - Created customize_vars.py and WH_anomalous_variables.py for keeping things organized. -->
- Tag List contains WHLeptonic, and ZH Leptonic ->Categories are removed for WHLeptonic
- Dumps variables only for WHLeptonic
- process.flashggWHLeptonicTag.Boundaries_GT75 set to -1 to config Choose Category

<!-- ./Systematics/test/tools
- Added multiple helper files for WH_anom_dumper.py -->

./Systematics/test/compile.sh
- Created File to compile flashgg. Need to edit the class_def file manually

./Systematics/test/json/*
- Created json files for VH, VH_bkg, WH Anomalous. Note the settings used.

./Systematics/test/script_VH.sh
- Script fggRun VH NTuples

./Systematics/test/script_ggH_VBF_ttH.sh
- Script fggRun ggH_VBF_ttH NTuples

./Systematics/test/script_WH_Anomalous.sh
- Script fggRun VH NTuples

./Taggers/plugins/WHLeptonicTagProducer.cc
- Edited ChooseCategory to relax the WHBDT cut, and create only one category
- Added code to include WHMVA and ptV variables used for WH BDT (choose category to be done offline)


## Files Edited
./README.org ./proxy.sh ./DataFormats/interface/WHLeptonicTag.h ./DataFormats/src/classes_def.xml ./Systematics/test/WH_anom_dumper.py ./Systematics/test/tools ./Systematics/test/compile.sh ./Taggers/plugins/WHLeptonicTagProducer.cc ./Systematics/test/json/* ./Systematics/test/script_VH.sh ./Systematics/test/script_ggH_VBF_ttH.sh ./Systematics/test/script_WH_Anomalous.sh ./MetaData/data/cross_sections.json


## To Do
Add the variables from flasgg.Systematics/python folder. 