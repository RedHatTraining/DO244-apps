# Ping-go App

Ping-go is a Container image for an app written in Go.
The app is a simple web server, that returns whatever value is in the TARGET environment variable.

This app is automatically started by the startup scripts for the Traffic routing GE.

## To publish this image, log into quay.io and then execute the following:

```bash
./publish.sh
```
## To pull and run the image:

```bash
podman pull quay.io/redhattraining/do244-serving-manage
podman run --name serving-manage -d -p 8080:8080 quay.io/redhattraining/do244-serving-manage
```

 You can use `curl` to `GET` test the endpoint:

```console
curl  http://localhost:8080
```
