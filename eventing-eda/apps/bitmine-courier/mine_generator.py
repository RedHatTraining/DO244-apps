#!/usr/bin/env python3

"""
Bitmine Courier
"""

import requests
import os
import random
import json
import time

url = os.environ.get('URL')
mine_count = int(os.environ.get('MINE_COUNT'))


def main():
    for i in range(mine_count):
        headers = {"Ce-Id": f"{i}",
                   "Ce-Specversion": "1.0",
                   "Ce-Type": f"{random_type()}",
                   "Ce-Source": "bitmine",
                   "Content-Type": "application/json",
                   }

        req = requests.post(url, data=bitmine_data_json(), headers=headers)
        print(req.text)
        time.sleep(1)


def random_type():
    return random.choice(["quarkers", "noders"])


def random_bitmine_type():
    return random.choice(["Audamandium",
                          "Aethez",
                          "Karbonadium",
                          "Uruu",
                          "Vybranium",
                          "Transformyum",
                          "Dhiotimoline",
                          "Cryptonite",
                          "Katschin",
                          "Enerqon"])


def random_bitmine_weight():
    return round(random.uniform(0, 10), 2)


def bitmine_data_json():
    data = {}

    data["type"] = random_bitmine_type()
    data["weight"] = random_bitmine_weight()

    return json.dumps(data)


if __name__ == "__main__":
    main()
