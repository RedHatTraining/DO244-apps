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

test('City in response should Not Equal Mumbai if London is passed as query param', t => {
  start(func).then(server => {
    t.plan(2);
    request(server)
      .get('/?city=London')
      .expect(200)
      .expect('Content-Type', /json/)
      .end((err, res) => {
        t.error(err, 'No error');
        t.notEqual(res.body.data.city, 'Mumbai');
        t.end();
        server.close();
      });
  }, errHandler(t));
});



