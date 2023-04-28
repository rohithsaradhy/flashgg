nEvents=-1
outdir=zh_sig_all_mass
dumper=../ZH_anom_dumper.py
queue=tomorrow
json=json/zh_sig_all_mass.json

date_name='2022_08_24_ZH_NoCuts'
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
