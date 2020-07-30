#!/bin/bash -e

CMSSWVER=CMSSW_10_2_21
DIR="${HOME}"
TARBALL=""
URL=""

usage(){
    EXIT=$1

    echo "setup.sh [options]"
    echo ""
    echo "-c [version]        use specified CMSSW version (default = ${CMSSWVER})"
    echo "-d [dir]            project installation area for the CMSSW directory (default = ${DIR})"
    echo "-t [tarball]        the name and path to the tarball containing the \$CMSSW_BASE/src files (default = ${TARBALL})"
    echo "-h                  display this message and exit"

    exit $EXIT
}

# process options
while getopts "c:d:t:h" opt; do
    case "$opt" in
    c) CMSSWVER=$OPTARG
    ;;
    d) DIR=$OPTARG
    ;;
    t) TARBALL=$OPTARG
    ;;
    h) usage 0
    ;;
    esac
done

# Add these lines to the .bashrc and .zshrc files
lines="\n\
# Needed to access FNAL EOS\n\
export XrdSecGSISRVNAMES=\"cmseos.fnal.gov\"\n"
echo -e ${lines} >> ${HOME}/.bashrc
echo -e ${lines} >> ${HOME}/.zshrc

# Checkout a CMSSW release and source the cmsset if in a standalone CMSSW image
if [[ -f /opt/cms/entrypoint.sh ]]; then
	/opt/cms/entrypoint.sh
fi
if [[ -f /opt/cms/cmsset_default.sh ]]; then
	echo "Sourcing the cmsset ... "
	source /opt/cms/cmsset_default.sh
fi

# Move to the CMSSW directory and initialize the CMSSW environment
pwd
ls -alh ./
cd ${DIR}/${CMSSWVER}/src/
pwd
ls -alh ./
echo "Setting the CMSSW environment ..."
eval `scramv1 runtime -sh`

# Untar and build the software, if provided
if [[ -n "$TARBALL" ]]; then
	echo "Unpacking ${TARBALL} into ${PWD} ..."
	tar -xzf ${TARBALL}
	pwd
	ls -alh ./
	echo "Compiling the software ..."
	scramv1 b -j 8
fi

# Return to the ${HOME} directory
echo -e "Returning to ${HOME} ... "
cd ${HOME}
