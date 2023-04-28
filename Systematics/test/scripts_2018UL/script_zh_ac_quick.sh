nEvents=-1
outdir=zh_ac_quick
dumper=../ZH_anom_dumper.py
#queue=microcentury
queue=workday
# queue=tomorrow
# queue=nextweek
json=json/zh_ac_quick.json
date_name='2023_02_09_18UL_NoSys_v0_XS1'
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

            
# # --make-light-tarball \
