nEvents=-1
outdir=sig_all_mass
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/sig_all_mass.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
