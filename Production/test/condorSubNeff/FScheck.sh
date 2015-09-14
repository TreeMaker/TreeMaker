#!/bin/bash

KEEPTAR=$1

# grid proxy existence & expiration check
PCHECK=`voms-proxy-info -timeleft`
if [[ ($? -ne 0) || ("$PCHECK" -eq 0) ]]; then
  voms-proxy-init -voms cms --valid 168:00
fi

# tarball of CMSSW area
if [ -z "$KEEPTAR" ]; then
  tar --exclude-caches-all -zcf ${CMSSW_VERSION}.tar.gz -C ${CMSSW_BASE}/.. ${CMSSW_VERSION}
fi

