#!/bin/bash -e

usage() {
	echo "lnbatch.sh [todir]"
	echo "lnbatch.sh [fromdir] [todir]"
	echo ""
	echo "fromdir must be absolute or relative to todir (not current dir), following lndir behavior"

	exit 1
}

# usage:

FROMDIR=../condorSub
TODIR=""

if [[ $# -eq 1 ]]; then
	TODIR=$1
elif [[ $# -eq 2 ]]; then
	FROMDIR=$1
	TODIR=$2
else
	usage
fi

mkdir -p $TODIR
lndir -silent -ignorelinks $FROMDIR $TODIR	

if [[ "${TODIR}/CACHEDIR.TAG" ]]; then
	unlink ${TODIR}/CACHEDIR.TAG
	cp ${TODIR}/$FROMDIR/CACHEDIR.TAG $TODIR
fi
