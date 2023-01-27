#!/bin/bash

storageDir="/eos/cms/store/group/dpg_ecal/comm_ecal/localreco/vbfhgg/HiggsCouplings/Trees_2023_01_27_allSTXSCats"
outDir=$1
if [[ -z $outDir ]]; then
    echo "usage: $0 <outDir>"
    exit -1
fi
year2016preVFPDir="signal_IA_UL16preVFP"
year2016postVFPDir="signal_IA_UL16postVFP"
year2017Dir="signal_IA_UL17"
year2018Dir="signal_IA_UL18"

mkdir -p ${storageDir}/${outDir}_${year2016preVFPDir}
fggRunJobs.py --load sig_jobs_2016preVFP_UL.json -d ${outDir}_${year2016preVFPDir} -x cmsRun ../workspaceVbf.py metaDataSrc=flashgg dumpTrees=True doSystematics=True applyNNLOPSweight=True recalculatePDFWeights=True doPdfWeights=True useParentDataset=True anomalousCouplings=True dumpLHE=False melaEFT=True --nCondorCpu=2 pujidWP=tight maxEvents=-1 --stage-to=${storageDir}/${outDir}_${year2016preVFPDir} -q workday -n 100 -H --no-copy-proxy --no-use-tarball &

mkdir -p ${storageDir}/${outDir}_${year2016postVFPDir}
fggRunJobs.py --load sig_jobs_2016postVFP_UL.json -d ${outDir}_${year2016postVFPDir} -x cmsRun ../workspaceVbf.py metaDataSrc=flashgg dumpTrees=False doSystematics=True applyNNLOPSweight=True recalculatePDFWeights=True doPdfWeights=True useParentDataset=True anomalousCouplings=True dumpLHE=False melaEFT=True --nCondorCpu=2 pujidWP=tight maxEvents=-1 --stage-to=${storageDir}/${outDir}_${year2016postVFPDir} -q workday -n 100 -H --no-copy-proxy --no-use-tarball &

mkdir -p ${storageDir}/${outDir}_${year2017Dir}
fggRunJobs.py --load sig_jobs_2017_UL.json -d ${outDir}_${year2017Dir} -x cmsRun ../workspaceVbf.py metaDataSrc=flashgg dumpTrees=False doSystematics=True applyNNLOPSweight=True recalculatePDFWeights=True doPdfWeights=True useParentDataset=True anomalousCouplings=True dumpLHE=False melaEFT=True --nCondorCpu=2 pujidWP=tight maxEvents=-1 --stage-to=${storageDir}/${outDir}_${year2017Dir} -q workday -n 100 -H --no-copy-proxy --no-use-tarball &

mkdir -p ${storageDir}/${outDir}_${year2018Dir}
fggRunJobs.py --load sig_jobs_2018_UL.json -d ${outDir}_${year2018Dir} -x cmsRun ../workspaceVbf.py metaDataSrc=flashgg dumpTrees=False doSystematics=True applyNNLOPSweight=True recalculatePDFWeights=True doPdfWeights=True useParentDataset=True anomalousCouplings=True dumpLHE=False melaEFT=True --nCondorCpu=2 pujidWP=tight maxEvents=-1 --stage-to=${storageDir}/${outDir}_${year2018Dir} -q workday -n 100 -H --no-copy-proxy --no-use-tarball &
