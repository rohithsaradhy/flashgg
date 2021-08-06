nEvents=-1
outdir=2021_04_15_Output_bkg_WGToLNuG_v2
dumper=WH_anom_dumper.py
queue=workday
json=json/bkg_WGToLNuG.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
