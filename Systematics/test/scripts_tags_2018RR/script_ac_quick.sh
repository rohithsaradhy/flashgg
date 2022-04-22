nEvents=100000
outdir=ac_quick
dumper=../WH_anom_dumper.py
queue=microcentury
# queue=workday
# queue=tomorrow
# queue=nextweek
json=json/ac_quick.json
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/2022_04_20/raw/$outdir/

fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              --no-copy-proxy \
              -q $queue \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True 

            

