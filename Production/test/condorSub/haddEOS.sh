#!/bin/bash

case `uname` in
  Linux) ECHO="echo -e" ;;
  *) ECHO="echo" ;;
esac

usage(){
	EXIT=$1
	$ECHO "haddEOS.sh [options]"
	$ECHO
	$ECHO "Options:"
	$ECHO "-i input        \tcomma-separated list of samples to check for hadding (if omitted, searches entire dir)"
	$ECHO "-d dir          \tlogical directory containing files, e.g. /store/user/... (required)"
	$ECHO "-x xrd          \txrootd storage element location (default = root://cmseos.fnal.gov)"
	$ECHO "-g search       \tadditional string to append when listing input files, e.g. _block"
	$ECHO "-o output       \toutput dir for tmp file (default = pwd)"
	$ECHO "-s suffix       \toptional suffix to append to output filename"
	$ECHO "-u              \tupdate an existing file (output filename added to list of input files)"
	$ECHO "-k              \tkeep input files when finished (default = delete upon successful hadd + stageout)"
	$ECHO "-r              \tactually run (default = dry run, print number of input files)"
	$ECHO "-v              \tverbose output for dry run"
	$ECHO "-h              \tprint this message and exit"
	exit $EXIT
}

INPUT=""
DIR=""
SUFF=""
SEARCH=""
RUN=0
UPDATE=0
VERBOSE=0
XRDLOC=root://cmseos.fnal.gov
OUTPUT=""
KEEPINPUT=0

#check arguments
while getopts "d:i:s:g:x:o:kruvh" opt; do
	case "$opt" in
	r) RUN=1
	;;
	u) UPDATE=1
	;;
	s) SUFF=$OPTARG
	;;
	d) DIR=$OPTARG
	;;
	i) INPUT=$OPTARG
	;;
	g) SEARCH=$OPTARG
	;;
	v) VERBOSE=1
	;;
	x) XRDLOC=$OPTARG
	;;
	o) OUTPUT=$OPTARG
	;;
	k) KEEPINPUT=1
	;;
	h) usage 0
	;;
	esac
done

if [[ -z "$DIR" ]]; then
	usage 1
fi

#search entire dir
if [[ -z "$INPUT" ]]; then
	IFS=$'\n' SAMPLES=($(python findHadds.py -x ${XRDLOC} -d ${DIR} -g ${SEARCH})); unset IFS
else
	#convert input into array
	IFS=',' read -r -a SAMPLES <<< "$INPUT"; unset IFS
fi

XRDIR=$XRDLOC/$DIR
for BASE in ${SAMPLES[@]}; do
	$ECHO $BASE
	
	#check to see if anything needs to be hadded
	IFS=$'\n' LGFILES=($(xrdfs $XRDLOC ls ${DIR} | grep "${BASE}${SEARCH}")); unset IFS
	if [[ ${#LGFILES[@]} -eq 0 ]]; then
		$ECHO "nothing to hadd for $BASE"
		continue
	fi
	
	ALLFILES=""
	for FILE in ${LGFILES[@]}; do
		ALLFILES="${ALLFILES} ${XRDIR}/`basename ${FILE}`"
	done
	
	#include base file when updating
	if [[ $UPDATE -eq 1 ]]; then
		ALLFILES="${XRDIR}/${BASE}.root ${ALLFILES}"
	fi

	#setup filename	
	TMPFILE=${BASE}.root
	if [[ -n "$SUFF" ]]; then
		TMPFILE=${BASE}_${SUFF}.root
	fi
	#use specified output dir
	if [[ -n "$OUTPUT" ]]; then
		TMPFILE=${OUTPUT}/${TMPFILE}
	fi

	#dryrun (list nfiles) is default
	if [[ $RUN -eq 0 ]]; then
		if [[ $VERBOSE -eq 0 ]]; then
			$ECHO ${ALLFILES} | wc -w
		else
			sed 's/ /\n\t/g' <<< "Input:$ALLFILES"
			$ECHO "Output:\n\t$TMPFILE"
		fi
		continue
	fi
	
	#hadd to tmp file
	hadd ${TMPFILE} ${ALLFILES}
	
	#check exit code
	HADDEXIT=$?
	if [[ $HADDEXIT -ne 0 ]]; then
		rm ${TMPFILE}
		$ECHO "exit code $HADDEXIT, skipping xrdcp"
		exit $HADDEXIT
	fi
	
	#copy hadded file to eos
	xrdcp -f ${TMPFILE} ${XRDIR}/

	#check exit code
	XRDEXIT=$?
	if [[ $XRDEXIT -ne 0 ]]; then
		rm ${TMPFILE}
		$ECHO "exit code $XRDEXIT, failure in xrdcp"
		exit $XRDEXIT
	fi	
	
	#remove original files (only if hadd and xrdcp succeeded, and keep=0)
	if [[ $KEEPINPUT -eq 0 ]]; then
		for FILE in ${LGFILES[@]}; do
			xrdfs $XRDLOC rm ${FILE}
		done
	fi
	
	#remove tmp file
	rm ${TMPFILE}
done
