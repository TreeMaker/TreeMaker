#!/bin/bash -e

CMSSWVER=CMSSW_10_2_21
DIR="${HOME}"
OFILE="testfile.root"
OPATH="TreeMaker/Production/test/"
URL=""

usage(){
        EXIT=$1

        echo "setup.sh [options]"
        echo ""
        echo "-c [version]        use specified CMSSW version (default = ${CMSSWVER})"
        echo "-d [dir]            project installation area for the CMSSW directory (default = ${DIR})"
        echo "-f [filename]       the output filename for the downloaded file (default = ${OFILE})"
        echo "-p [path]           the output path for the downloaded file (default = ${OPATH})"
        echo "-u [url]            a url to download (default = ${URL})"
        echo "-h                  display this message and exit"

        exit $EXIT
}

# process options
while getopts "c:d:f:p:u:h" opt; do
        case "$opt" in
        c) CMSSWVER=$OPTARG
        ;;
        d) DIR=$OPTARG
        ;;
        f) OFILE=$OPTARG
		;;
		p) OPATH=$OPTARG
		;;
        u) URL=$OPTARG
		;;
        h) usage 0
        ;;
        esac
done

# Turn this on so that stdout isn't buffered - otherwise logs in kubectl don't
# show up until much later!
export PYTHONUNBUFFERED=1
export X509_USER_PROXY=/etc/grid-security/x509up

# Setup the folders needed for the grid proxy
mkdir -p /etc/grid-security/

# Initialize the CMSSW environment
cd ${DIR}/${CMSSWVER}/src
eval `scramv1 runtime -sh`

# Install missing python packages
python -m pip install --user --no-cache-dir -r ${CMSSW_BASE}/src/.github/ServiceX/data/requirements.txt

# Download CMS Open Data test file
if [[ -n "$URL" ]]; then
	wget ${URL} -O \ ${CMSSW_BASE}/src/${OPATH}/${OFILE}
fi
