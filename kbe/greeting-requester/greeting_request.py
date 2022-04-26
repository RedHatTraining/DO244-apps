#!/usr/bin/env python3

"""
Greeting Requester
"""

import requests
import os
import random

url = os.environ.get('BROKER_URL')
greeting = os.environ.get('GREETING')
data = '{"key":"from a curl"}'

for _ in range(5):
    headers = {"Ce-Id": "say-hello",
           "Ce-Specversion": "1.0",
           "Ce-Type": f"{greeting}",
           "Ce-Source": "mycurl",
           "Content-Type": "application/json",
           }    

    req = requests.post(url, data=data, headers=headers)

    print(req.text)
