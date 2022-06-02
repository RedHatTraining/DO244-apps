import json


def read_json_file(weather: str):

    try:
        with open('./data/city.json') as data_file:
            weather = json.load(data_file)

        return weather

    except FileNotFoundError:
        print("No file exists!!")


def kelvin_to_celsius(temperature: str):

    print("Let's convert the temperature of city from Kelvin to Celsius")
    print()
    temp_celsius = (temperature - 273.15)
    temp_celsius = float(temp_celsius)

    return {"The degree Kelvin is equal to degree Celsius", temp_celsius}


def kelvin_to_farhenheit(temperature: str):

    print("Let's convert the temperature of city from Kelvin to Celsius")
    print()
    temp_fahrenheit = (temperature * 1.8) - 459.67
    temp_fahrenheit = float(temp_fahrenheit)

    return {"The degree Kelvin is equal to degree fahrenheit", temp_fahrenheit}
