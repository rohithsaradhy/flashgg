nEvents=-1
outdir=sig_different_mass
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/sig_different_mass.json


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
