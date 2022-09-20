#!/bin/bash

export JOBNAME=""
export PROCESS=""
export OUTDIR=""
export REDIR=""
export OPTIND=1
while [[ $OPTIND -lt $# ]]; do
	# getopts in silent mode, don't exit on errors
	getopts ":j:p:x:o:" opt || status=$?
	case "$opt" in
		j) export JOBNAME=$OPTARG
		;;
		p) export PROCESS=$OPTARG
		;;
		o) export OUTDIR=$OPTARG
        ;;
		x) export REDIR=$OPTARG
		;;
		# keep going if getopts had an error
		\? | :) OPTIND=$((OPTIND+1))
		;;
	esac
done

echo "parameter set:"
echo "OUTDIR:     $OUTDIR"
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

CMSEXIT=$?

rm nefffinder_cfg.py

if [[ $CMSEXIT -ne 0 ]]; then
	rm *.root
	echo "exit code $CMSEXIT, failure, skipping xrdcp"
	exit $CMSEXIT
fi

# copy output to eos
echo "CMSSITE currently set to: ${CMSSITE}"
if [[ -z "$CMSSITE" ]] || [[ "$CMSSITE" == "" ]]; then
    echo -e "\tGetting CMSSITE from the job ClassAd"
    CMSSITE=$(getFromClassAd MachineAttrGLIDEIN_CMSSite0)
    echo -e "\tCMSSITE is now set to: ${CMSSITE}"
fi
export CMDSTR="xrdcp"
export GFLAG=""
export COPYARGS="-f"
if [[ ( "$CMSSITE" == *"T1_US_FNAL"* && "${OUTDIR}" == *"root://cmseos.fnal.gov/"* ) ]]; then
    export CMDSTR="gfal-copy"
    export GFLAG="-g"
    export COPYARGS="${COPYARGS} -p"
    export WEBDAV_ENDPOINT="davs://cmseos.fnal.gov:9000/eos/uscms/store/user/"
    export OUTDIR=${WEBDAV_ENDPOINT}${OUTDIR#root://cmseos.fnal.gov//store/user/}
elif [[ "${OUTDIR}" == *"davs://"* ]]; then
    export CMDSTR="gfal-copy"
    export GFLAG="-g"
    export COPYARGS="${COPYARGS} -p"
fi
echo "$CMDSTR output for condor"
for FILE in *.root; do
	echo "${CMDSTR} -f ${FILE} ${OUTDIR}/${FILE}"
	stageOut ${GFLAG} -x ${COPYARGS} -i ${FILE} -o ${OUTDIR}/${FILE} -r -c '*.root'
	XRDEXIT=$?
	if [[ $XRDEXIT -ne 0 ]]; then
		echo "exit code $XRDEXIT, failure in $CMDSTR"
		exit $XRDEXIT
	fi
done
