#!/bin/bash

export JOBNAME=""
export PROCESS=""
export REDIR=""
export OPTIND=1
while [[ $OPTIND -lt $# ]]; do
	# getopts in silent mode, don't exit on errors
	getopts ":j:p:x:" opt || status=$?
	case "$opt" in
		j) export JOBNAME=$OPTARG
		;;
		p) export PROCESS=$OPTARG
		;;
		x) export REDIR=$OPTARG
		;;
		# keep going if getopts had an error
		\? | :) OPTIND=$((OPTIND+1))
		;;
	esac
done

echo "parameter set:"
echo "JOBNAME:    $JOBNAME"
echo "PROCESS:    $PROCESS"
echo "REDIR:      $REDIR"
echo ""

# link files from CMSSW dir
ln -s ${CMSSWVER}/src/TreeMaker/Production/test/nefffinder_cfg.py

# run CMSSW
ARGS=$(cat argsNeff_${JOBNAME}_${PROCESS}.txt)
if [[ -n "$REDIR" ]]; then
 ARGS="$ARGS redir=${REDIR}"
fi
echo "cmsRun nefffinder_cfg.py ${ARGS} 2>&1"
cmsRun nefffinder_cfg.py ${ARGS} 2>&1
rm nefffinder_cfg.py

CMSEXIT=$?

if [[ $CMSEXIT -ne 0 ]]; then
  echo "exit code $CMSEXIT, failure"
  exit $CMSEXIT
fi
