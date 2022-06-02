from parliament import Context
from methods import kelvin_to_celsius, kelvin_to_farhenheit, read_json_file


def main(context: Context):
    try:
        city_name = context.request.args.get('city_name')
        json_data = read_json_file()

        temp_kelvin = json_data['city'][city_name]['main']['temp']

        # Conversion of temperature from Kelvin to Celsius
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        print("The temp in celsius is: ", temp_celsius)

        # Conversion of temperature from Kelvin to fahrenheit
        temp_fahrenheit = kelvin_to_farhenheit(temp_kelvin)
        print("The temp in farhenheit is: ", temp_fahrenheit)

        return {"message": json_data['city'][city_name]}, 200

    # If we can not find a city, throw an city not found error.
    except KeyError:
        return {"message": "City cannot be found!"}, 404
