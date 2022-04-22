nEvents=-1
outdir=data
dumper=../WH_anom_dumper.py
queue=testmatch
json=json/data.json
eos_dir=/eos/user/r/rsaradhy/vh_anomalous/2022_04_20/raw

fggRunJobs.py --load $json \
              -d $outdir \
              --stage-to $eos_dir \
              -n 100 \
              -q $queue \
            #   --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True
