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
const fs = require("fs");
let methodObj = require('./methods');

async function handle(context) {

    const cityname = context.query.city;
    //console.log("1 "+cityname);
    let temp_kelvin,temp_celsius,temp_fahrenheit;
    let cityDetailsJson = {};
    let cityDetailsJsonKey = 'Weather Details';
    cityDetailsJson[cityDetailsJsonKey] = [];
    let isCityNamePresent = false;

      fs.readFile("city.json", function(err, data)
      {
          if (err) throw err;
          let weatherData = JSON.parse(data);
          //console.log("2 "+weatherData);
          for (let i=0; i<weatherData.city.length; i++)
          {
            //console.log("3 "+weatherData.city.length);
            let name = weatherData.city[i]["name"];
            //console.log("4 "+name);
            if(cityname === name)
            {
              //console.log("Cityname found");
              isCityNamePresent = true;
              for (let key in weatherData.city[i])
              {
                //console.log(key);
                if(key === 'main')
                {
                  //console.log("Key main matched");
                  temp_kelvin = weatherData.city[i][key]["temp"];
                  //console.log(temp_kelvin);
                }
              }
              temp_celsius = methodObj.kelvin_to_celsius(temp_kelvin);
              //console.log(temp_celsius);
              temp_fahrenheit = methodObj.kelvin_to_farhenheit(temp_kelvin);
              //console.log(temp_fahrenheit);
              var cityDetails = {
                city: cityname,
              };
              //console.log(cityDetails);
              cityDetailsJson[cityDetailsJsonKey].push(cityDetails);
              //console.log(cityDetailsJson);

              var tempDetails = {
                kelvin: temp_kelvin,
                celsius: temp_celsius,
                fahrenheit: temp_fahrenheit
              };
              //console.log(tempDetails);
              cityDetailsJson[cityDetailsJsonKey].push(tempDetails);
              console.log("Line 71"+JSON.stringify(cityDetailsJson));
            }
          }

          // If city name cannot be found
          if(isCityNamePresent === false)
          {
            var cityDetails = {
              city: namecity,
              message: "City cannot be found!!"
            };
            cityDetailsJson[cityDetailsJsonKey].push(cityDetails);
            console.log("Line 83"+JSON.stringify(cityDetailsJson));
          }
      });
        console.log(cityDetailsJson);
        return { statusCode:200, data: JSON.stringify(cityDetailsJson)};
}

// Export the function
module.exports = { handle };
