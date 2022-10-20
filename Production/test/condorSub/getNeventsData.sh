#!/bin/bash

YEARS=(
2016 \
2017 \
2018 \
)

getNevents(){
	if [ -z "$@" ]; then return; fi
	for SAMPLE in $@; do
		dasgoclient -query="file dataset=$SAMPLE | sum(file.nevents)" | cut -d' ' -f2
	done | awk '{sum += $1} END {print sum}'
}

readarray -t SAMPLES <<< $(python -c 'from sizetest import tests; print "\n".join([fname for fname,test in tests if test["type"]=="data"])')

echo -e "from collections import OrderedDict\n"
echo "neventsData = OrderedDict(["
for SAMPLE in ${SAMPLES[@]}; do
	LINE="   (\"$SAMPLE\", {"
	for YEAR in ${YEARS[@]}; do
		QUERY="/${SAMPLE}/Run${YEAR}*-*UL${YEAR}_MiniAODv2-v*/MINIAOD"
		RTMP=$(dasgoclient -query="$QUERY")
		SUM=0
		if [ -n "$RTMP" ]; then
			SUM=$(getNevents "$RTMP")
		fi
		LINE="${LINE}\"${YEAR}\": $SUM, "
	done
	LINE="${LINE}}),"
	echo "$LINE"
done
echo "])"
