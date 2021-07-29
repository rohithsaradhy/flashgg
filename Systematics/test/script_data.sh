nEvents=-1
outdir=2021_05_28_Output_data
dumper=WH_anom_dumper.py
queue=workday
# json=json/data_jobs.json
json=json/legacy_runII_v2_2018_final.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
