'use strict';

const func = require('..').handle;
const test = require('tape');

const fixture = { log: { info: console.log } };

test('Unit: handles an HTTP GET', t => {
  t.plan(1);
  // Invoke the function, which should complete without error.
  const result = func({ ...fixture, method: 'GET', query: { name: 'tiger' } }, { type: "MyEvent"});
  t.deepEqual(result, "OK");
  t.end();
});

test('Unit: handles an HTTP POST', t => {
  t.plan(1);
  // Invoke the function, which should complete without error.
  const result = func({ ...fixture, method: 'POST', body: { name: 'tiger' } }, { type: "MyEvent"});
  t.deepEqual(result, "OK");
  t.end();
});
