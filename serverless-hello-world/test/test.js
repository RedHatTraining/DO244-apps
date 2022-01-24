"use strict";

const func = require("..").handle;
const test = require("tape");

const fixture = { log: { info: console.log } };

test("Unit: handles an HTTP GET", (t) => {
  t.plan(1);
  // Invoke the function, which should complete without error.
  const result = func({
    ...fixture,
    method: "GET"
  });
  t.deepEqual(result, {
    statusCode: 200,
    message: "Welcome to the world of serverless",
  });
  t.end();
});

test("Unit: handles any other HTTP method", (t) => {
  t.plan(1);
  // Invoke the function, which should complete without error.
  const result = func({
    ...fixture,
    method: "POST"
  });
  t.deepEqual(result, { statusCode: 405, statusMessage: "Method not allowed" });
  t.end();
});
