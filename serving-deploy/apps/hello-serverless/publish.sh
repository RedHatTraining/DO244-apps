#!/usr/bin/env bash

# Use this script to buid and publish the image (both v1 and v2)

usageMsg="usage:ScriptName --scan [scan type] [keyword] OR --help"

if [ $# -eq 0 ]
  then
    echo "Version is a required parameter [v1|v2]"
    exit 1
fi

VERSION=$1
CONTAINERFILE=Containerfile.${VERSION}

echo "Building from ${CONTAINERFILE}..."
echo ""


podman build . -t do244-serving-deploy-quotas -f ${CONTAINERFILE} && \
podman tag do244-serving-deploy-quotas quay.io/redhattraining/do244-serving-deploy-quotas:${VERSION}
podman push quay.io/redhattraining/do244-serving-deploy-quotas:${VERSION}
