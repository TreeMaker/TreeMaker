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
counter=0
mkdir -p removed

#search for "return value" in condor logs newer than TIME - denotes finished job
#or "abort" - denotes removed job
echo -n "Searching logs after $TIME..."
readarray filelist < <(find . -maxdepth 1 -name \*.condor -newermt "${TIME}" -print0 | xargs -0 -n1 -P4 grep -l -m1 "abort")
filelistlen=${#filelist[@]}
echo " found $filelistlen"
for ((i=0; i < $filelistlen; i++)); do
	redraw_progress_bar $i $filelistlen 20

	fileline=${filelist[$i]}
	#split filename and matched line from grep
	IFS=':' read -r file line <<< "$fileline"; unset IFS
	
	#get JOBNAME from filename
	base=$(echo $(basename ${file}) | rev | cut -d'_' -f1-1 --complement | rev)
	
	#move condor file to backup dir, remove empty stdout/stderr files
	mv ${file} removed/${file}
	rm $(basename ${file} .condor).stdout
	rm $(basename ${file} .condor).stderr

	#add job to resubmission list
	echo "condor_submit jobExecCondor_${base}.jdl" >> ${OUTNAME}
	counter=$((counter+1))
done

redraw_progress_bar $filelistlen $filelistlen 20
echo ""
echo "Job resubmission script created: ${OUTNAME}"
echo "     Number of jobs to resubmit: ${counter}"
chmod +x ${OUTNAME}
