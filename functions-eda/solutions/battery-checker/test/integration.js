'use strict';
const { start } = require('faas-js-runtime');
const request = require('supertest');

const func = require('..').handle;
const test = require('tape');

const Spec = {
  version: 'ce-specversion',
  type: 'ce-type',
  id: 'ce-id',
  source: 'ce-source'
};

const data = {
  name: 'tiger',
  customerId: '01234'
}

const errHandler = t => err => {
  t.error(err);
  t.end();
};

test('Integration: handles a valid event', t => {
  start(func).then(server => {
    t.plan(0);
    request(server)
      .post('/')
      .send(data)
      .set(Spec.id, '01234')
      .set(Spec.source, '/test')
      .set(Spec.type, 'MyTest')
      .set(Spec.version, '1.0')
      .expect(200)
      .end((err, result) => {
        t.end();
        server.close();
      });
  }, errHandler(t));
});
