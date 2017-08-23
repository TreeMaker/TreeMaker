#!/bin/bash

#
# variables from arguments string in jdl
#

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release
echo "CMSSW on Condor"

# to get condor-chirp from CMSSW
PATH="/usr/libexec/condor:$PATH"
source /cvmfs/cms.cern.ch/cmsset_default.sh

CMSSWVER=$1
OUTDIR=$2
SAMPLE=$3
NPART=$4
NSTART=$5
NFILES=$6
SCENARIO=$7
THREADS=$8
REDIR=$9

echo ""
echo "parameter set:"
echo "CMSSWVER:   $CMSSWVER"
echo "OUTDIR:     $OUTDIR"
echo "SAMPLE:     $SAMPLE"
echo "NPART:      $NPART"
echo "NSTART:     $NSTART"
echo "NFILES:     $NFILES"
echo "SCENARIO:   $SCENARIO"
echo "THREADS:    $THREADS"
echo "REDIR:      $REDIR"

tar -xzf ${CMSSWVER}.tar.gz
cd ${CMSSWVER}
scram b ProjectRename
# cmsenv
eval `scramv1 runtime -sh`
cd -

# run CMSSW
ARGS="outfile=${SAMPLE}_${NPART} inputFilesConfig=${SAMPLE} nstart=${NSTART} nfiles=${NFILES} scenario=${SCENARIO} threads=${THREADS}"
if [[ -n "$REDIR" ]]; then
 ARGS="$ARGS redir=${REDIR}"
fi
cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1

CMSEXIT=$?

if [[ $CMSEXIT -ne 0 ]]; then
  rm *.root
  echo "exit code $CMSEXIT, skipping xrdcp"
  exit $CMSEXIT
fi

# copy output to eos
echo "xrdcp output for condor"
for FILE in *.root
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/${FILE}"
  xrdcp -f ${FILE} ${OUTDIR}/${FILE} 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done

