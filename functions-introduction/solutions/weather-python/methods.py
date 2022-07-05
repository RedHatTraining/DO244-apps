from pathlib import Path
import json

def read_weather(city: str):
    weather = {}
    filepath = Path(__file__).parent.joinpath("cities.json")

    try:
        with open(filepath) as data_file:
            weather = json.load(data_file)

    except FileNotFoundError as e:
        print("No cities.json file exists!!")
        raise e

    city = weather['city'].get(city.lower())

    return city



def kelvin_to_celsius(temperature: str):
    temp_celsius = (temperature - 273.15)
    temp_celsius = float(temp_celsius)

    return temp_celsius


def kelvin_to_farhenheit(temperature: str):
    temp_fahrenheit = (temperature * 1.8) - 459.67
    temp_fahrenheit = float(temp_fahrenheit)

    return temp_fahrenheit
