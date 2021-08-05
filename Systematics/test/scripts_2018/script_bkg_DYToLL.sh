nEvents=-1
outdir=2021_04_15_Output_bkg_DYToLL_v2
dumper=WH_anom_dumper.py
queue=tomorrow
json=json/bkg_DYToLL.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
