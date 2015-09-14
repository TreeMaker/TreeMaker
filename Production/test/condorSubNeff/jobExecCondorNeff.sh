#!/bin/bash

#
# variables from arguments string in jdl
#

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release
echo "CMSSW on Condor"

CMSSWVER=$1
SAMPLE=$2
NSTART=$3
NFILES=$4

echo ""
echo "parameter set:"
echo "CMSSWVER:   $CMSSWVER"
echo "SAMPLE:     $SAMPLE"
echo "NSTART:     $NSTART"
echo "NFILES:     $NFILES"

tar -xzf ${CMSSWVER}.tar.gz
cd ${CMSSWVER}
scram b ProjectRename
source /cvmfs/cms.cern.ch/cmsset_default.sh
# cmsenv
eval `scramv1 runtime -sh`
cd -

# run CMSSW
cmsRun nefffinder_cfg.py name=${SAMPLE} nstart=${NSTART} nfiles=${NFILES} 2>&1



