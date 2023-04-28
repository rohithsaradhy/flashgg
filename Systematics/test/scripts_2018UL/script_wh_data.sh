nEvents=-1
outdir=wh_data
dumper=../WH_anom_dumper.py
queue=testmatch
json=json/wh_data.json
date_name='2023_02_24_18UL_NoSys_v0_XS1_BDTv2'
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
