# Node.js HTTP Function

Welcome to your new Node.js function project! The function code can be found in [`index.js`](./index.js). This function will respond to incoming HTTP GET and POST requests. This example function is written synchronously, returning a JSON value. 

## Local execution

After executing `npm install`, you can run this function locally by executing `npm start`.

The parameter provided to the function endpoint at invocation is a `Context` object containing HTTP request information.

```js
function handleRequest(context) {
  const log = context.log;
  log.info(context.httpVersion);
  log.info(context.method); // the HTTP request method (only GET or POST supported)
  log.info(context.query); // if query parameters are provided in a GET request
  log.info(context.body); // contains the request body for a POST request
  log.info(context.headers); // all HTTP headers sent with the event
}
```
 You can use `curl` to `GET` or `POST` an event to the function endpoint:

```console
curl -X GET http://localhost:8080
curl -X POST http://localhost:8080
```

## Testing

This function project includes a [unit test](./test/test.js). All `.js` files in the test directory are run.

```console
npm test
```
