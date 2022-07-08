from parliament import Context
from methods import kelvin_to_celsius, kelvin_to_farhenheit, read_weather


def main(context: Context):

    # Parse city_name parameter from query string
    city_name = context.request.args.get("city_name")

    # Get weather by city_name, or return an error
    weather = read_weather(city_name)

    if not weather:
        return {"result": "City cannot be found!"}, 404

    # Get kelvin temperature from city
    temp_kelvin = weather["main"]["temp"]

    # Convert kelvins to Celisus and Fahrenheit
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    temp_fahrenheit = kelvin_to_farhenheit(temp_kelvin)

    # Build the response
    result = {
        "city": weather["name"],
        "temperature": {
            "celsius":temp_celsius,
            "fahrenheit": temp_fahrenheit,
            "kelvin": temp_kelvin
        }
    }

    return {"result": result}, 200
