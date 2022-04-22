nEvents=-1
outdir=bkg
dumper=../WH_anom_dumper.py
queue=tomorrow
# queue=microcentury
json=json/bkg.json
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/2022_04_20/raw



fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
            #   --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents  #copyInputMicroAOD=True
