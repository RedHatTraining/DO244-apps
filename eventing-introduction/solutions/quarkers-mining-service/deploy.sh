#!/bin/bash

REGISTRY=image-registry.openshift-image-registry.svc:5000
IMAGE_GROUP=developer-eventing-introduction
IMAGE_NAME=quarkers-mining-service
IMAGE_TAG=1.0.0-SNAPSHOT

kn service create \
  quarkers-mining-service \
  --image "$REGISTRY/$IMAGE_GROUP/$IMAGE_NAME:$IMAGE_TAG" \
  --concurrency-target=1
