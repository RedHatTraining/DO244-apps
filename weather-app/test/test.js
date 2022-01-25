'use strict';

const { start } = require('faas-js-runtime');
const request = require('supertest');

const func = require('..').handle;
const test = require('tape');

const errHandler = t => err => {
  t.error(err);
  t.end();
};

test('City in response should Equal Mumbai if Mumbai is passed as query param', t => {
  start(func).then(server => {
    t.plan(2);
    request(server)
      .get('/?city=Mumbai')
      .expect(200)
      .expect('Content-Type', /json/)
      .end((err, res) => {
        t.error(err, 'No error');
        t.deepEqual(res.body.data.city, 'Mumbai');
        t.end();
        server.close();
      });
  }, errHandler(t));
});

test('Test to execute catch block when invalid city name is provided', t => {
  start(func).then(server => {
    t.plan(2);
    request(server)
      .get('/?city=xyz')
      .expect(404)
      .expect('Content-Type', /json/)
      .end((err, res) => {
        t.error(err, 'No error');
        t.deepEqual(res.body.statusMessage, 'City not found.Failed to fetch data');
        t.end();
        server.close();
      });
  }, errHandler(t));
});



