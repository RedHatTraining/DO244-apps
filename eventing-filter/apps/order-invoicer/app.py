from typing import Tuple

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process() -> Tuple[str, int]:

    print()
    print("Received an order to invoice:")
    print(f"  - Customer: {request.json.get('customer')}")
    print(f"  - Amount: {request.json.get('amount')}")
    print()

    return '', 200
