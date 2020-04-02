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

# Add these lines to the .bashrc file
echo -e "\n \
# Turn this on so that stdout isn't buffered - otherwise logs in kubectl don't\n \
#   show up until much later!\n \
export PYTHONUNBUFFERED=1\n \
export X509_USER_PROXY=/etc/grid-security/x509up\n" >> ${HOME}/.bashrc

# Initialize the CMSSW environment
echo -e "Running \'cmsenv\' ... "
cd ${DIR}/${CMSSWVER}/src
eval `scramv1 runtime -sh`

# Install missing python packages
echo -e "Installing python packages via \'pip\' ... "
python -m pip install --user --no-cache-dir -r ${CMSSW_BASE}/src/TreeMaker/.github/ServiceX/data/requirements.txt

# Download CMS Open Data test file
if [[ -n "$URL" ]]; then
    DESTINATION="${CMSSW_BASE}/src/${OPATH}/${OFILE}"
    echo -e "Downloading a file ...\n\tFrom: ${URL}\n\tDestination: ${DESTINATION}"
    wget ${URL} -O ${DESTINATION}
fi

# Return to the ${HOME} directory
echo -e "Returning to ${HOME} ... "
cd ${HOME}