const { CloudEvent, HTTP } = require("cloudevents");
const pg = require("pg");

const config = {
  host: 'postgresql-functionia',
  user: "postgres", //this is the db user credential
  password: "postgres",
  database: "functioniadb",
  port: 5432,
  max: 100, // max number of clients in the pool
  idleTimeoutMillis: 30000,
};

const pool = new pg.Pool(config);

/**
 * Your CloudEvent handling function, invoked with each request.
 * This example function logs its input, and responds with a CloudEvent
 * which echoes the incoming event data
 *
 * It can be invoked with 'func emit'
 *
 * @param {Context} context a context object.
 * @param {object} context.body the request body if any
 * @param {object} context.query the query string deserialzed as an object, if any
 * @param {object} context.log logging object with methods for 'info', 'warn', 'error', etc.
 * @param {object} context.headers the HTTP request headers
 * @param {string} context.method the HTTP request method
 * @param {string} context.httpVersion the HTTP protocol version
 * See: https://github.com/knative-sandbox/kn-plugin-func/blob/main/docs/guides/nodejs.md#the-context-object
 * @param {CloudEvent} event the CloudEvent
 */
function handle(context, event) {
  event.data.status = "PROCESSED";

  console.log(JSON.stringify(event, null, 2));

  pool.query("INSERT INTO bitmine_noders (type, weight, status) VALUES ($1, $2, $3)", [event.data.type, event.data.weight, event.data.status], (error, results) => {
    if (error) {
      throw error
    }
    console.log("Bitmine is stored in the DB");
  });
}

module.exports = { handle };
