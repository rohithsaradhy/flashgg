nEvents=-1
outdir=sig
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/sig.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True
