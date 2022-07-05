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

test('Weather details in response if city name is passed as query param', t => {
  start(func).then(server => {
    t.plan(2);
    request(server)
      .get('/?city=toronto')
      .expect(200)
      .expect('Content-Type', /json/)
      .end((err, res) => {
        t.error(err, 'No error');
        t.deepEqual(city.main.temp,263.19);
        t.end();
        server.close();
      });
  }, errHandler(t));
});
