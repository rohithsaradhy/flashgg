nEvents=-1
outdir=2021_04_15_Output_ggH_VBF_ttH
dumper=WH_anom_dumper.py
queue=workday
json=json/sig_jobs_ggH_VBF_ttH.json


fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
