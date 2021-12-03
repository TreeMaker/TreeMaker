#!/bin/bash -e

CMSSWVER=CMSSW_10_6_29
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

# Source the cmsset if in a standalone CMSSW image
if [[ -f /opt/cms/cmsset_default.sh ]]; then
	echo "Sourcing the cmsset ... "
	source /opt/cms/cmsset_default.sh
fi

# Setup a symlink if in a standalone CMSSW image
if [[ -f /opt/cms/cmsset_default.sh ]]; then
	sudo ln -s /opt/cms /cvmfs/cms.cern.ch
fi

# Move to the project installation area
pwd
ls -alh ./
cd ${DIR}
pwd
ls -alh ./

# Untar the the CMSSW release, if provided, and change directories to the release area
if [[ -n "$TARBALL" ]]; then
	echo "Unpacking ${TARBALL} into ${PWD} ..."
	tar -xzf ${TARBALL}
	pwd
	ls -alh ./
	cd ${CMSSWVER/src/}
	scram b ProjectRename
	pwd
	ls -alh ./
else
	cd ${CMSSWVER}/src/
	pwd
	ls -alh ./
fi

# Initialize the CMSSW environment
echo "Setting the CMSSW environment ..."
eval `scramv1 runtime -sh`
echo "The CMSSW_BASE is ${CMSSW_BASE}"

# Return to the ${HOME} directory
echo -e "Returning to ${HOME} ... "
cd ${HOME}
