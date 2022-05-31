import json
import os
import random
from flask import abort, Flask, jsonify
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)


DATA_FOLDER = escape(os.environ.get('DATA_FOLDER', 'data'))
ERROR_RESPONSE = int(os.environ.get('ERROR_RESPONSE', 404))


@app.errorhandler(404)
def topicNotFound(error):
    return "Unable to find the specific topic", 404


@app.route('/weather/<string:topic>/<string:nameofcity>')
def getWeatherForCity(topic,nameofcity):
    try:
        # Loading the file which has the topic news
        with open('./%s/%s.json' % (DATA_FOLDER, escape(topic))) as topicFile:
            weather = json.load(topicFile)
            print(weather['city'][nameofcity])

        return weather['city'][nameofcity]

    # If we can not find a file for the topic, we throw an error
    except IOError:
        abort(ERROR_RESPONSE)
