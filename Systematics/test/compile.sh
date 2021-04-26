#!/bin/bash
pwd=$PWD
cd $CMSSW_BASE/src
echo "Moved to CMSSW SRC :"$PWD

# scram build updateclassversion
scram b -j 8
echo "Going Back to Directory " $pwd

