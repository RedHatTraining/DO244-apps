import json
import os
import random
import time

from flask import Flask, abort, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = './data/finance.json'
DEFAULT_DELAY = 0
NUM_OF_RESULTS = 3
ERROR_RESPONSE = int(os.environ.get('ERROR_RESPONSE', 404))


def sort_by_timestamp(element):
    return element['timestamp']


@app.route('/')
def get_financial_news():
    try:
        time.sleep(int(request.args.get('delay', default=DEFAULT_DELAY)))

        with open(DATA_FILE) as news_file:
            news = json.load(news_file)

        random_selection = random.sample(news['data'], NUM_OF_RESULTS)
        random_selection.sort(key=sort_by_timestamp)

        return jsonify(random_selection)

    except IOError:
        abort(ERROR_RESPONSE)
