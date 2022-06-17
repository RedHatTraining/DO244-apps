import os
from typing import Dict, Tuple

from flask import Flask, request

from producer.events import EventsProducer

app = Flask(__name__)

invoicing_sink_url = os.environ.get('INVOICING_SINK')
fraud_sink_url = os.environ.get('FRAUD_SINK')


@app.route('/order/process', methods=['POST'])
def report() -> Tuple[str, int]:

    print(f"INVOICING_SINK: {invoicing_sink_url}")
    print(f"FRAUD_SINK: {fraud_sink_url}")

    if not invoicing_sink_url:
        return '{"message": "INVOICING_SINK env variable is required"}', 500

    if not fraud_sink_url:
        return '{"message": "FRAUD_SINK env variable is required"}', 500

    invoicing_producer = EventsProducer(invoicing_sink_url)
    fraud_producer = EventsProducer(fraud_sink_url)

    event = {'event': 'OrderWasCreated'}

    fraud_score = calculate_fraud_score(int(request.json.get('amount')))

    if fraud_score == 'low':
        invoicing_producer.emit(
            {**event, **request.json},
            generate_custom_ce_headers(fraud_score)
        )
    else:
        fraud_producer.emit(
            {**event, **request.json},
            generate_custom_ce_headers(fraud_score)
        )

    return '', 202


def calculate_fraud_score(amount) -> str:
    if amount < 100:
        return 'low'

    return 'high'


def generate_custom_ce_headers(fraud_score: str) -> Dict[str, str]:
    return {'fraudscore': fraud_score}
