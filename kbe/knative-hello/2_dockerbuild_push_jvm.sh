#!/bin/bash

VERSION=0.0.1
APP=kbe-knative-hello

podman build -t dev.local/redhattraining/$APP:$VERSION -f src/main/docker/Dockerfile.jvm .

podman login quay.io

podman tag dev.local/redhattraining/$APP:$VERSION quay.io/redhattraining/$APP:$VERSION
podman push quay.io/redhattraining/$APP:$VERSION
