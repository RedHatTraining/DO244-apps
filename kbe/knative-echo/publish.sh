if [ $# -eq 0 ] ; then
    echo "Provide version parameter"
    exit 1
fi

VERSION=$1
IMAGE="quay.io/redhattraining/kbe-knative-echo:$VERSION"

echo "=== Publishing $IMAGE"

podman build . -t kbe-knative-echo
podman tag kbe-knative-echo $IMAGE
podman push $IMAGE
