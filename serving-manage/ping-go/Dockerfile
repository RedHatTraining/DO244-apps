# RedHat Training Dockerfile for ping-go app of DO244
FROM registry.redhat.io/rhel8/go-toolset:1.17.7-13
LABEL description="Custom http ping container image"
MAINTAINER Randy Thomas <althomas@redhat.com>
EXPOSE 8080
ENV PORT "8080"
ENV TARGET "Hello World"
COPY ping-go.go /opt/app-root/src/.
COPY go.mod /opt/app-root/src/.
RUN go build . && \
    chmod u+x ping-go
ENTRYPOINT ["/opt/app-root/src/ping-go"]