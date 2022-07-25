#!/usr/bin/env bash

# Use this script to buid and publish the image

CONTAINERFILE=Dockerfile

echo "Building from ${CONTAINERFILE}..."
echo ""


podman build . --layers=false -t do244-custom-ping -f ${CONTAINERFILE} && \
podman tag do244-custom-ping quay.io/redhattraining/do244-serving-manage
podman push quay.io/redhattraining/do244-serving-manage