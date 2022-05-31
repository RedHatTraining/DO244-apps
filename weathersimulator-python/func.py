import json
import os
from flask import abort, Flask
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)


DATA_FOLDER = escape(os.environ.get('DATA_FOLDER', 'data'))
ERROR_RESPONSE = int(os.environ.get('ERROR_RESPONSE', 404))


@app.errorhandler(404)
def city_not_found(error):
    return "City cannot be found, failed to fetch the weather details!", 404


@app.route('/weather/<string:city>/<string:nameofcity>')
def get_weather_for_city(city, nameofcity):
    try:
        # Loading the file which has the topic news
        with open('./%s/%s.json' % (DATA_FOLDER, escape(city))) as data_file:
            weather = json.load(data_file)

        return weather['city'][nameofcity]

    # If we can not find a city, throw an city not found error.
    except KeyError:
        abort(ERROR_RESPONSE)
