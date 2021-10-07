nEvents=-1
outdir=wh_anom
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/wh_anom.json

fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
