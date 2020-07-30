# Make the base image configurable:
ARG BASEIMAGE=gitlab-registry.cern.ch/treemaker/cmssw-docker/cmssw:CMSSW_10_2_21-2020-04-22-2c2fe7c3

# Set up the CMSSW base:
FROM ${BASEIMAGE}

ARG BUILD_DATE
ARG VCS_REF
ARG VCS_URL
ARG VERSION
LABEL   org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.name="TreeMaker Docker image" \
        org.label-schema.description="Provide completely offline-runnable CMSSW images with TreeMaker pre-installed." \
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

COPY .docker/setupStandalone.sh ./setupStandalone.sh
COPY cmssw_src.tar.gz ./cmssw_src.tar.gz

RUN ./setupStandalone.sh -c $CMSSW_VERSION -t ${HOME}/cmssw_src.tar.gz && \
    rm ${HOME}/setupStandalone.sh && \
    rm ${HOME}/cmssw_src.tar.gz

ENTRYPOINT ["/bin/zsh"]