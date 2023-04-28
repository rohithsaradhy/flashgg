nEvents=-1
outdir=wh_sig
dumper=../WH_anom_dumper.py
queue=workday
# queue=tomorrow
json=json/wh_sig.json
date_name='2023_02_24_17UL_NoSys_v0_XS1_BDTv2'
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/$date_name/raw/$outdir/
mkdir -p $eos_dir


fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
              --no-copy-proxy \
              --make-light-tarball \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
