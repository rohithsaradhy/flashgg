nEvents=-1
outdir=2021_04_15_Output_WH_Anomalous
dumper=WH_anom_dumper.py
queue=workday
json=json/WH_Anomalous.json

fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
