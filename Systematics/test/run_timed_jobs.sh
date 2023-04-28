#!/bin/bash

# Systematics/test/scripts_2017UL/script_wh_data.sh
# Systematics/test/scripts_2018RR/script_wh_bkg.sh

cd scripts_2016ULpre
echo "Entering scripts_2016ULpre"

echo "Launching 18RR AC 2" > run_timed_jobs.log
source script_wh_ac_quick.sh &

sleep 45m
echo "Launching 18RR SIG" >> run_timed_jobs.log
source script_wh_sig.sh &

sleep 45m
echo "Launching 18RR DATA" >> run_timed_jobs.log
source script_wh_data.sh &


# wait