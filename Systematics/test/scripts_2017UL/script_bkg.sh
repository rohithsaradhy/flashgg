nEvents=-1
outdir=bkg
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/bkg.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True
