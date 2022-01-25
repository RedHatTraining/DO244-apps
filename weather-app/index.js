/**
 * Your HTTP handling function, invoked with each request. This is an example
 * function that echoes its input to the caller, and returns an error if
 * the incoming request is something other than an HTTP POST or GET.
 *
 * @param {Context} context a context object.
 * @param {object} context.body the request body if any
 * @param {object} context.query the query string deserialzed as an object, if any
 * @param {object} context.log logging object with methods for 'info', 'warn', 'error', etc.
 * @param {object} context.headers the HTTP request headers
 * @param {string} context.method the HTTP request method
 * @param {string} context.httpVersion the HTTP protocol version
 * See: https://github.com/knative-sandbox/kn-plugin-func/blob/main/docs/guides/nodejs.md#the-context-object
 */

const axios = require("axios").default;
const constants = require("./constants");
require('dotenv').config({ path: './env/env.local' });
async function handle(context) {
  const url = constants.BASE_URL;
  const city = context.query.city;
  const apiKey = process.env.API_KEY;
  let weatherData = {};
  const options = {
    params: { q: city , appid: apiKey }
  };
  try {
    const response = await axios.get(url, options);
    weatherData = response.data.main;
    weatherData.city = response.data.name;

    return { statusCode:200, data: weatherData};

  } catch (error) {

    return { statusCode:404, statusMessage: "City not found.Failed to fetch data"};
    
  }
}

module.exports = { handle };
