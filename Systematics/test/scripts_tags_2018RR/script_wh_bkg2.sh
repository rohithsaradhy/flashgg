nEvents=-1
outdir=wh_bkg2
dumper=../WH_anom_dumper.py
# queue=workday
queue=tomorrow
# queue=microcentury
json=json/wh_bkg2.json
date_name='2022_08_23_STXS_Cuts'
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/$date_name/raw/$outdir/
mkdir -p $eos_dir

fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
              --no-copy-proxy \
              --make-light-tarball \
              -x cmsRun $dumper maxEvents=$nEvents  copyInputMicroAOD=True


#   --make-light-tarball \