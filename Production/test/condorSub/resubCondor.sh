#!/bin/bash

#assumptions in this script:
#all .jdl and .condor files are in the current directory
#all .jdl files are named jobExecCondor_JOBNAME.jdl
#all .condor files are named JOBNAME_$(Cluster).condor
#one .jdl file per JOBNAME (i.e. only "Queue 1" is used)

#progress bar function
function redraw_progress_bar { # curr, tot, barlength
local CURR=$1
local TOT=$2
local BARLENGTH=$3
local PROGRESS=$(( $BARLENGTH * $CURR / $TOT ))
local PERCENT=$(( 100 * $CURR / $TOT ))
echo -n "["
for ((j = 0; j < $PROGRESS; j++)); do echo -n ">"; done
for ((j = $PROGRESS; j < $BARLENGTH; j++)); do echo -n " "; done
echo -n "] $PERCENT% ( $CURR / $TOT )"$'\r'
}

#initialize parameters
TIME=""
OUTNAME=""

#check arguments
while getopts "t:f:o:" opt; do
	case "$opt" in
	t)
		TIME=$OPTARG
	;;
	f)  #option to start from the time of a file
		if (stat $OPTARG > /dev/null 2>&1); then
			TIME=$(date -r $OPTARG +"%Y-%m-%d %H:%M")
		fi
	;;
	o)
		OUTNAME=$OPTARG
	;;
	esac
done

#default is beginning of time
if [[ -z $TIME ]]; then
	#old default was 24 hrs ago
	#TIME=$(date "--date=$(date) -1 day" +"%Y-%m-%d %H:%M")
	TIME="1970-01-01 00:00"
fi

#default is resub.sh
if [ -z "$OUTNAME" ]; then
	OUTNAME="resub.sh"
fi

#setup resub script
echo "#!/bin/bash" > ${OUTNAME}
echo "" >> ${OUTNAME}

#keep track of jobs that have been checked
joblist=""
counter=0

#search for "return value" in condor logs newer than TIME - denotes finished job
#or "abort" - denotes removed job
echo -n "Searching logs after $TIME..."
IFS=$'\n' filelist=($(grep -m1 "return value\|abort" $(find . -name \*.condor -newermt "${TIME}"))); unset IFS
filelistlen=${#filelist[@]}
echo " found $filelistlen"
for ((i=0; i < $filelistlen; i++)); do
	redraw_progress_bar $i $filelistlen 20

	fileline=${filelist[$i]}
	#split filename and matched line from grep
	IFS=':' read -r file line <<< "$fileline"; unset IFS
	
	#skip job if it finished successfully - return value 0
	success=$(echo "$line" | fgrep -w "return value 0")
	if [[ -n $success ]]; then
		continue
	fi
	
	#get JOBNAME from filename
	base=$(echo $(basename ${file}) | rev | cut -d'_' -f1-1 --complement | rev)
	
	#skip job if it has already been checked
	if (echo "$joblist" | fgrep -qw $base); then
		continue
	fi
	
	#check for newer logs that succeeded or are still running
	newerfiles=$(find . -name ${base}_\*.condor -newer "${file}")
	newerstatus=""
	stillrunning=""
	if [[ -n $newerfiles ]]; then
		newerstatus=$(grep -lw "return value 0" ${newerfiles})
		if [[ -z $newerstatus ]]; then
			stillrunning=$(grep -L "return value\|abort" ${newerfiles})
		fi
	fi
	
	#if none were found, the job failed
	if [[ -z $newerstatus && -z $stillrunning ]]; then
		#optional: output return value for failed job as comment in resub script
		#echo "#"$(grep -w "return value" ${file}) >> ${OUTNAME}
		echo "condor_submit jobExecCondor_${base}.jdl" >> ${OUTNAME}
		counter=$((counter+1))
	fi
	
	#append jobname to list
	joblist="${base} ${joblist}"
done

redraw_progress_bar $filelistlen $filelistlen 20
echo ""
echo "Job resubmission script created: ${OUTNAME}"
echo "     Number of jobs to resubmit: ${counter}"
chmod +x ${OUTNAME}
