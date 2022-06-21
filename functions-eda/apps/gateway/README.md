# Drone Telemetry App Gateway

This application is the source [quay.io/redhattraining/do244-financial-api:1.0](https://quay.io/repository/redhattraining/do244-drone-telemetry-gateway), required for the `functions-eda` guided exercise.

## Build and Publish Container Image

If you need to rebuild the container image, run these commands:

```
podman build . -t quay.io/redhattraining/do244-drone-telemetry-gateway:1.0
podman push quay.io/redhattraining/do244-drone-telemetry-gateway:1.0
```
