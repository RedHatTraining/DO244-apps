from os import environ
from time import time

import requests
from parliament import Context


def main(context: Context):
    payload = {'ping': time()}

    r = requests.post(
        environ.get('BROKER_URL'),
        headers={
            'Ce-Id': 'ping-pong',
            'Ce-Specversion': '1.0',
            'Ce-Type': 'ping',
            'Ce-Source': 'some-source',
            'Content-Type': 'application/json'
        },
        json=payload
    )

    return {
               'payload': payload,
               'broker': environ.get('BROKER_URL'),
               'status_code': r.status_code,
           }, 200
