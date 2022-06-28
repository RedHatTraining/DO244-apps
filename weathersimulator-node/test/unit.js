'use strict';

const { start } = require('faas-js-runtime');
const request = require('supertest');

const func = require('..').handle;
const test = require('tape');

const fixture = { log: { info: console.log } };

const errHandler = t => err => {
  t.error(err);
  t.end();
};

// test('Unit: handles an HTTP GET', t => {
//   t.plan(1);
//   // Invoke the function, which should complete without error.
//   const result = func({ ...fixture, method: 'GET', query: { name: 'tiger' } });
//   t.deepEqual(result, { query: { name: 'tiger' } });
//   t.end();
// });

test('City in response should Equal Mumbai if Mumbai is passed as query param', t => {
  start(func).then(server => {
    t.plan(2);
    request(server)
      .get('/?cityname=Mumbai')
      .expect(200)
      .expect('Content-Type', /json/)
      .end((err, res) => {
        t.error(err, 'No error');
        t.deepEqual(res.body.data.cityname, 'Mumbai');
        t.end();
        server.close();
      });
  }, errHandler(t));
});

// test('Unit: handles an HTTP POST', t => {
//   t.plan(1);
//   // Invoke the function, which should complete without error.
//   const result = func({ ...fixture, method: 'POST', body: { name: 'tiger' } });
//   t.deepEqual(result, { body: { name: 'tiger' } });
//   t.end();
// });

// test('Unit: responds with error code if neither GET or POST', t => {
//   t.plan(1);
//   const result = func(fixture);
//   t.deepEqual(result, { statusCode: 405, statusMessage: 'Method not allowed' });
//   t.end();
// });
