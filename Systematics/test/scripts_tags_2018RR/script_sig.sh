nEvents=-1
outdir=sig
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/sig.json
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/2022_04_20/raw


fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
              \ #--no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True
