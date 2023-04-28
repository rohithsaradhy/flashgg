#!/usr/bin/bash
# This is a file that will dump the fggManageSamples into text files that can be parsed using find samples


fggManageSamples.py -C Era2018_legacy_v1_Summer19UL list raw > ./tmp/Era2018_legacy_v1_Summer19UL.txt
fggManageSamples.py -C Era2018_legacy_v1_Summer20UL list raw > ./tmp/Era2018_legacy_v1_Summer20UL.txt

fggManageSamples.py -C Era2017_legacy_v1_Summer19UL list raw > ./tmp/Era2017_legacy_v1_Summer19UL.txt
fggManageSamples.py -C Era2017_legacy_v1_Summer20UL list raw > ./tmp/Era2017_legacy_v1_Summer20UL.txt

fggManageSamples.py -C Era2016_legacyPreVFP_v1_Summer19UL list raw > ./tmp/Era2016_legacyPreVFP_v1_Summer19UL.txt
fggManageSamples.py -C Era2016_legacyPreVFP_v1_Summer20UL list raw > ./tmp/Era2016_legacyPreVFP_v1_Summer20UL.txt

fggManageSamples.py -C Era2016_legacyPostVFP_v1_Summer19UL list raw > ./tmp/Era2016_legacyPostVFP_v1_Summer19UL.txt
fggManageSamples.py -C Era2016_legacyPostVFP_v1_Summer20UL list raw > ./tmp/Era2016_legacyPostVFP_v1_Summer20UL.txt
