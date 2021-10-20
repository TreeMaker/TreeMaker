#!/bin/bash

# helper function to structure the ouput into folders
structuredOutput() {
	RES=""
	TMP=${1/.//}
	IFS='_' read -r -a array <<< "$TMP"
	cut=$(expr ${#array[@]} - 2)
	for index in "${!array[@]}"; do
		if [[ $index -lt $cut ]]; then
			if [[ $index -eq 0 ]]; then
				RES=${RES}${array[index]}
			else
				RES=${RES}"_"${array[index]}
			fi
		elif [[ $index -eq $cut ]]; then
			RES=${RES}"/"${array[index]}
		else
			RES=${RES}"_"${array[index]}
		fi
	done
	echo ${RES}
}

export JOBNAME=""
export PROCESS=""
export OUTDIR=""
export REDIR=""
export OPTIND=1
export USE_FOLDERS="false"
while [[ $OPTIND -le $# ]]; do
	# getopts in silent mode, don't exit on errors
	OPTOLD=$OPTIND
	getopts ":fj:p:o:x:" opt || status=$?
	case "$opt" in
		f) export USE_FOLDERS="true"
		;;
		j) export JOBNAME=$OPTARG
		;;
		p) export PROCESS=$OPTARG
		;;
		o) export OUTDIR=$OPTARG
		;;
		x) export REDIR=$OPTARG
		;;
		# keep going if getopts had an error, but make sure not to skip anything
		\? | :) OPTIND=$((OPTOLD+1))
		;;
	esac
done

echo "parameter set:"
echo "OUTDIR:      $OUTDIR"
echo "JOBNAME:     $JOBNAME"
echo "PROCESS:     $PROCESS"
echo "REDIR:       $REDIR"
echo "USE_FOLDERS: $USE_FOLDERS"
echo ""

# link files from CMSSW dir
ln -s ${CMSSWVER}/src/TreeMaker/Production/test/data
ln -s ${CMSSWVER}/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py

# run CMSSW
ARGS=$(cat args_${JOBNAME}_${PROCESS}.txt)
if [[ -n "$REDIR" ]]; then
	ARGS="$ARGS redir=${REDIR}"
fi
THREADS=$(getFromClassAd RequestCpus)
if [[ -n "$THREADS" ]]; then
	ARGS="$ARGS threads=${THREADS}"
fi
echo "cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1"
cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1

CMSEXIT=$?

rm runMakeTreeFromMiniAOD_cfg.py

if [[ $CMSEXIT -ne 0 ]]; then
	rm *.root
	echo "exit code $CMSEXIT, skipping xrdcp"
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
if [[ ( "$CMSSITE" == *"T1_US_FNAL"* && "${OUTDIR}" == *"root://cmseos.fnal.gov/"* ) ]]; then
	export CMDSTR="gfal-copy"
	export GFLAG="-g"
	export GSIFTP_ENDPOINT="gsiftp://cmseos-gridftp.fnal.gov//eos/uscms/store/user/"
	export OUTDIR=${GSIFTP_ENDPOINT}${OUTDIR#root://cmseos.fnal.gov//store/user/}
elif [[ "${OUTDIR}" == *"gsiftp://"* ]]; then
	export CMDSTR="gfal-copy"
	export GFLAG="-g"
fi
echo "$CMDSTR output for condor"
for FILE in *.root; do
	FILE_DST=${FILE}
	if [[ "${USE_FOLDERS}" == "true" ]]; then
		echo "Changing to folder structure consisting of <era>/<sample>/<filename>.root"
		echo -e "\tPrior to change: ${FILE_DST}"
		FILE_DST=`structuredOutput ${FILE_DST}`
		echo -e "\t   After change: ${FILE_DST}"
	fi
	echo "${CMDSTR} -f ${FILE} ${OUTDIR}/${FILE_DST}"
	stageOut ${GFLAG} -x "-f" -i ${FILE} -o ${OUTDIR}/${FILE_DST} -r -c '*.root'
	XRDEXIT=$?
	if [[ $XRDEXIT -ne 0 ]]; then
		echo "exit code $XRDEXIT, failure in $CMDSTR"
		exit $XRDEXIT
	fi
done

