nEvents=-1
outdir=2021_08_01_output_data
dumper=WH_anom_dumper.py
queue=tomorrow
json=json/data.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
