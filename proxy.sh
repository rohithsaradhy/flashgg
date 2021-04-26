#!/bin/bash
cmsenv
export X509_USER_PROXY=~/myproxy
voms-proxy-init -voms cms --valid 168:00
echo $X509_USER_PROXY