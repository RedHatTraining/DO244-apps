# Node.js HTTP Function

Welcome to your new Node.js function project! The boilerplate function code can be found in [`index.js`](./index.js). This function will respond to incoming HTTP GET request. This example function is written asynchronously, returning a JSON value. It will take city name provided as query parameter from the url and return the weather data for the city.

## Local execution

Before executing the function follow these steps:
1. Go to https://openweathermap.org/api
2. Sign up and create an API_KEY.
3. Copy and paste your API_KEY in env.local file under env folder.
4. npm install
5. npm start

You can use `curl` to `GET` a response from the function endpoint:

```console
curl -X GET "http://localhost:8080?city=London"
```
## Building the function

```console
kn func build -v
```
## Deploy the function on the cluster

```console
kn func deploy -v
```

## Testing

This function project includes a [unit test](./test/test.js). All `.js` files in the test directory are run.

```console
npm test
```
