# Make the base image configurable:
ARG BASEIMAGE=gitlab-registry.cern.ch/treemaker/cmssw-docker/cmssw:CMSSW_10_2_21-2020-04-22-2c2fe7c3

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

# This part can eventually be removed when the atlas references are removed from ServiceX
RUN sudo mkdir /home/atlas/ && \
    sudo cp /home/cmsusr/.bashrc /home/atlas/.bashrc && \
    sudo cp /home/cmsusr/.zshrc /home/atlas/.zshrc
COPY .github/ServiceX/scripts/proxy-exporter.sh /home/atlas/
COPY .github/ServiceX/python/validate_requests.py /home/atlas/
COPY .github/ServiceX/python/transformer.py /home/atlas/
RUN sudo chown -R cmsusr:cmsusr /home/atlas && \
    sudo chmod +x /home/atlas/proxy-exporter.sh

ENTRYPOINT ["/bin/zsh"]
