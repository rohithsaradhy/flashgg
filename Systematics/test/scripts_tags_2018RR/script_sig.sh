nEvents=-1
outdir=sig
dumper=../WH_anom_dumper.py
queue=workday
# queue=tomorrow
json=json/sig.json
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/2022_04_20/raw/$outdir/


fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
              --no-copy-proxy \
              --make-light-tarball \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
