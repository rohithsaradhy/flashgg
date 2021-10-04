nEvents=-1
outdir=data
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/data.json


# fggRunJobs.py --load $json \
#               -d $outdir \
#               -n 100 \
#               -q $queue \
#               --no-use-tarball --no-copy-proxy -D -P \
#               -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True



fggRunJobs.py --load $json \
              -d $outdir \
              -n 10 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
