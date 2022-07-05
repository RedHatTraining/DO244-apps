let methodObj = require('./methods');

function handle(context)
{
    let weatherData;
    let temp_kelvin,temp_celsius,temp_fahrenheit;

    // Parse city_name parameter from query string
    const cityname = context.query.city;

    // Get weather data for the cities
    weatherData = methodObj.readQuotesFile("city.json");

    // Get kelvin temperature from city
    for (let i=0; i<weatherData.city.length; i++)
    {
        if(cityname === weatherData.city[i]["name"])
        {
            temp_kelvin = weatherData.city[i]["main"]["temp"];
        }
    }

    // Convert kelvins to Celisus and Fahrenheit
    temp_celsius = methodObj.kelvin_to_celsius(temp_kelvin);
    temp_fahrenheit = methodObj.kelvin_to_farhenheit(temp_kelvin);

    // Build response
    result = {
        "city": cityname,
        "temperature": {
            "celsius":temp_celsius,
            "farenheit": temp_fahrenheit,
            "kelvin": temp_kelvin
        }
    }
    return { statusCode:200, data: result};
}

// Export the function
module.exports = { handle };
