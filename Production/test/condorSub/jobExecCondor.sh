#!/bin/bash

#
# variables from arguments string in jdl
#

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release
echo "CMSSW on Condor"

CMSSWVER=$1
OUTDIR=$2
SAMPLE=$3
FILELIST=$4
SCENARIO=$5

echo ""
echo "parameter set:"
echo "CMSSWVER:   $CMSSWVER"
echo "OUTDIR:     $OUTDIR"
echo "SAMPLE:     $SAMPLE"
echo "FILELIST:   $FILELIST"
echo "SCENARIO:   $SCENARIO"

tar -xzf ${CMSSWVER}.tar.gz
cd ${CMSSWVER}
scram b ProjectRename
source /cvmfs/cms.cern.ch/cmsset_default.sh
# cmsenv
eval `scramv1 runtime -sh`
cd -

# run CMSSW
cmsRun runMakeTreeFromMiniAOD_cfg.py outfile=${SAMPLE} dataset=${FILELIST} scenario=${SCENARIO} 2>&1

# copy output to eos
echo "xrdcp output for condor"
for FILE in *.root
  do
    echo "xrdcp -f ${FILE} ${OUTDIR}/${FILE}"
    xrdcp -f ${FILE} ${OUTDIR}/${FILE}
    rm ${FILE}
  done



