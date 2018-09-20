#!/bin/bash

case `uname` in
  Linux) ECHO="echo -e" ;;
  *) ECHO="echo" ;;
esac

usage(){
	EXIT=$1
	$ECHO "haddWrongPU.sh [options]"
	$ECHO
	$ECHO "Options:"
	$ECHO "-x xrd          \txrootd storage element location (default = root://cmseos.fnal.gov/)"
	$ECHO "-L lfn          \tlogical address of input directory (/store/..., required)"
	$ECHO "-o output       \tname for output file (default = Fall17PU.root)"
	$ECHO "-h              \tprint this message and exit"
	exit $EXIT
}

XRDLOC=root://cmseos.fnal.gov/
INPUT=""
OUTPUT=Fall17PU.root

#check arguments
while getopts "x:L:o:h" opt; do
	case "$opt" in
	x) XRDLOC=$OPTARG
	;;
	o) OUTPUT=$OPTARG
	;;
	L) INPUT=$OPTARG
	;;
	h) usage 0
	;;
	esac
done

if [ -z "$INPUT" ] || [ -z "$XRDLOC" ] || [ -z "$OUTPUT" ]; then
	usage 1
fi

# concatenate contents of dir (with pfns)
NAMES=$(xrdfs $XRDLOC ls $INPUT | sed 's~^/store~'$XRDLOC'/store~' | tr '\n' ' ')

hadd -f $OUTPUT $NAMES
