# Make the base image configurable:
ARG BASEIMAGE=gitlab-registry.cern.ch/treemaker/cmssw-docker/cmssw:CMSSW_10_2_21-2020-04-07-fc019a29

# Set up the CMSSW base:
FROM ${BASEIMAGE}

ARG BUILD_DATE
ARG VCS_REF
ARG VCS_URL
ARG VERSION
LABEL   org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.name="TreeMaker Docker image for ServiceX" \
        org.label-schema.description="Provide completely offline-runnable CMSSW images with the TreeMaker and ServiceX dependencies pre-installed." \
        org.label-schema.url="https://github.com/TreeMaker/TreeMaker" \
        org.label-schema.vcs-ref=$VCS_REF \
        org.label-schema.vcs-url=$VCS_URL \
        org.label-schema.vendor="FNAL" \
        org.label-schema.version=$VERSION \
        org.label-schema.schema-version="1.0"

USER    cmsusr
WORKDIR /home/cmsusr

ARG CMSSW_VERSION=CMSSW_10_2_21
ARG CURRENT_USER
ARG CURRENT_BRANCH
ARG DOWNLOAD_URL
ARG FILE_NAME

COPY .github/ServiceX/scripts/setup.sh ./setup_servicex.sh
COPY cmssw_src.tar.gz ./cmssw_src.tar.gz

RUN sudo chown cmsusr setup_servicex.sh && \
    sudo chmod +x setup_servicex.sh && \
    ./setup_servicex.sh -c $CMSSW_VERSION -f $FILE_NAME -t ${HOME}/cmssw_src.tar.gz -u $DOWNLOAD_URL && \
    rm ${HOME}/setup_servicex.sh && \
    rm ${HOME}/cmssw_src.tar.gz

ENTRYPOINT ["/bin/zsh"]
