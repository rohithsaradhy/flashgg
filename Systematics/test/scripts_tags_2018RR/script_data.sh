nEvents=-1
outdir=data
dumper=../WH_anom_dumper.py
queue=testmatch
json=json/data.json

fggRunJobs.py --load $json \
              -d $outdir \
              -n 150 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
