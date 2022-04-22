nEvents=-1
outdir=ac_quick
dumper=../WH_anom_dumper.py
queue=tomorrow
# queue=microcentury
# queue=nextweek
json=json/ac_quick.json

# fggRunJobs.py --load $json \
#               -d $outdir \
#               -n 100 \
#               -q $queue \
#               --no-use-tarball --no-copy-proxy -D -P \
#               -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True




fggRunJobs.py --load $json \
              -d $outdir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True


