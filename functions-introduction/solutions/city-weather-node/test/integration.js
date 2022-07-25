const { start } = require("faas-js-runtime");
const request = require("supertest");

const func = require('..').handle;
const test = require('tape');


test("Weather details in response if city name is passed as query param", t => {
    start(func).then(server => {
        t.plan(2);
        request(server)
            .get('/?city_name=toronto')
            .expect(200)
            .expect('Content-Type', /json/)
            .end((err, res) => {
                t.error(err, "No error");
                t.equal(res.body.result.temperature.fahrenheit, 14.072000000000003);
                t.end();
                server.close();
            });
    }, errorHandler(t));
});


test("Returns `city not found`", t => {
    start(func).then(server => {
        t.plan(2);
        request(server)
            .get('/?city_name=does_not_exist')
            .expect(404)
            .expect('Content-Type', /json/)
            .end((err, res) => {
                t.error(err, "No error");
                t.equal(res.body.result, "City not found!!");
                t.end();
                server.close();
            });
    }, errorHandler(t));
});


test("Integration: responds with error code if neither GET or POST", t => {
    start(func).then(server => {
        t.plan(1);
        request(server)
            .put('/')
            .send({ name: 'tiger' })
            .expect(200)
            .expect('Content-Type', /json/)
            .end((err, res) => {
                t.deepEqual(res.body, { message: 'Route PUT:/ not found', error: 'Not Found', statusCode: 404 });
                t.end();
                server.close();
            });
    }, errorHandler(t));
});


function errorHandler(t) {

    function handle(err) {
        t.error(err);
        t.end();
    };

    return handle;
}
