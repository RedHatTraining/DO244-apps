from parliament import Context
from methods import kelvin_to_celsius, kelvin_to_farhenheit, read_json_file


def main(context: Context):
    try:
        city_name = context.request.args.get('city_name')
        json_data = read_json_file()

        # Retrieving the temperature in degrees kelvin of the city
        temp_kelvin = json_data['city'][city_name]['main']['temp']

        # Conversion of temperature from Kelvin to Celsius
        temp_celsius = kelvin_to_celsius(temp_kelvin)

        # Conversion of temperature from Kelvin to fahrenheit
        temp_fahrenheit = kelvin_to_farhenheit(temp_kelvin)

        temperature_dict = {"celsius":temp_celsius, "farenheit": temp_fahrenheit,
        "kelvin": json_data['city'][city_name]['main']['temp']}

        info_dict = {"city": json_data['city'][city_name]['name'],
        "temperature": temperature_dict}

        return {"message": info_dict}, 200

    # If we can not find a city, throw city not found error.
    except KeyError:
        return {"message": "City cannot be found!"}, 404