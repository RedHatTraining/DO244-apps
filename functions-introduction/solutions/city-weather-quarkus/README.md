# Function project

Welcome to your new Quarkus function project!

This sample project contains a single function: `functions.Function.function()`,
the function just returns its argument.

## Local execution
Make sure that `Java 11 SDK` is installed.

To start server locally run `./mvnw quarkus:dev`.
The command starts http server and automatically watches for changes of source code.
If source code changes the change will be propagated to running server. It also opens debugging port `5005`
so debugger can be attached if needed.

To run the application locally run `./mvnw compile quarkus:dev`.

To run test locally run `./mvnw test`.

## The `func` CLI

It's recommended to set `FUNC_REGISTRY` environment variable.
```shell script
# replace ~/.bashrc by your shell rc file
# replace docker.io/johndoe with your registry
export FUNC_REGISTRY=docker.io/johndoe
echo "export FUNC_REGISTRY=docker.io/johndoe" >> ~/.bashrc 
```

## The `kn` CLI

The kn version should be 25 or greater than that.

We can check the version using `kn func version`.

### Building

This command builds OCI image for the function.

```shell script
kn func build                  # build jar
kn func build -i image-name    # it builds the image
```

### Running

This command runs the func locally in a container
using the image created above.
```shell script
kn func run
```

### Deploying

This commands will build and deploy the function into cluster.

```shell script
kn func deploy # also triggers build
```

## Function invocation

Do not forget to set `URL` variable to the route of your function.

You get the route by following command.
```shell script
func info
```

### cURL

```shell script
$ curl http://localhost:8080/?city=toronto
{"message":"{\"city\":\"toronto\",\"temperature\":{\"kelvin\":263.19,\"celsius\":-9.95999999999998,\"fahrenheit\":14.072000000000003}}"}
```
