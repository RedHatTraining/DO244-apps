let methods = require('./methods');

function handle(context) {
    // Parse city_name parameter from query string
    const cityname = context.query.city_name

    // Get weather by city_name, or return an error
    const city = methods.read_weather(cityname);

    if (city === undefined) {
        return { statusCode:404, result: "City not found!!"};
    }

    // Get kelvin temperature from city
    const temp_kelvin = city.main.temp;

    // Convert kelvins to Celisus and Fahrenheit
    // And Build the response
    result = {
        city: cityname,
        temperature: {
            celsius: methods.kelvin_to_celsius(temp_kelvin),
            fahrenheit: methods.kelvin_to_fahrenheit(temp_kelvin),
            kelvin: temp_kelvin
        }
    }

    return { statusCode: 200, result };
}

// Export the function
module.exports = { handle };
