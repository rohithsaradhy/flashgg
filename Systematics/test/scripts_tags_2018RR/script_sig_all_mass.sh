nEvents=-1
outdir=sig_all_mass
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/sig_all_mass.json

date_name='2022_08_23_STXS_Cuts'
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/$date_name/raw/$outdir/
mkdir -p $eos_dir
fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
              --no-copy-proxy -D -P \
              --make-light-tarball \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True
