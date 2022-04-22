nEvents=-1
outdir=main
dumper=../WH_anom_dumper.py
# queue=microcentury
# queue=workday
# queue=tomorrow
queue=testmatch
# queue=nextweek
json=json/main.json
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/2022_04_20/raw/$outdir/

fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              --no-copy-proxy \
              -q $queue \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True 

            

