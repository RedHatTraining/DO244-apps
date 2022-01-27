# Node.js Cloud Events Function

Welcome to your new Node.js function project! The boilerplate function
code can be found in [`index.js`](./index.js). This function is meant
to respond to [Cloud Events](https://cloudevents.io/).

## Local execution

After executing `npm install`, you can run this function locally by executing
`npm start`.

You can use `curl` to `POST` a request to the function endpoint:

```console
curl -X POST -d '{"name": "Tiger", "customerId": "0123456789"}' \
  -H'Content-type: application/json' \
  -H'Ce-id: 1' \
  -H'Ce-source: cloud-event-example' \
  -H'Ce-type: dev.knative.example' \
  -H'Ce-specversion: 1.0' \
  http://localhost:8080
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
