from parliament import Context
from methods import kelvin_to_celsius, kelvin_to_farhenheit, read_cities_weather


def main(context: Context):

    # TODO: Parse city_name parameter from query string
    city_name = context.request.args.get('city_name')

    # TODO: Read cities weather data
    json_data = read_cities_weather()

    # TODO: Get weather by city_name, or return an error
    try:
        city = json_data['city'][city_name]
    except KeyError:
        return {"result": "City cannot be found!"}, 404

    # TODO: Get kelvin temperature from city
    temp_kelvin = city['main']['temp']

    # TODO: Convert kelvins to Celisus and Fahrenheit
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    temp_fahrenheit = kelvin_to_farhenheit(temp_kelvin)

    # Build response
    result = {
        "city": city['name'],
        "temperature": {
            "celsius":temp_celsius,
            "farenheit": temp_fahrenheit,
            "kelvin": city['main']['temp']
        }
    }

    return {"result": result}, 200
