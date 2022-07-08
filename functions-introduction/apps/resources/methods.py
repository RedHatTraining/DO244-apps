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

    cityname = (city or "").lower()
    city = weather['city'].get(cityname)

    return city


def kelvin_to_celsius(temperature: float):
    return temperature - 273.15


def kelvin_to_farhenheit(temperature: float):
    return temperature * 1.8 - 459.67
