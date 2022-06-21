import os
import logging

import requests
from flask import Flask, request
from flask_cors import CORS
from cloudevents.http import CloudEvent, to_binary


# Start server

app = Flask("gateway")
app.logger.setLevel(logging.INFO)
CORS(app)


# Set vars

broker = os.environ.get(
    "CHANNEL",
    "http://broker-ingress.knative-eventing.svc.cluster.local/developer-functions-eda/drone-events-broker",
)


# Routes

@app.route("/")
def get_index():
    return {
        "_info": "Drone telemetry gateway",
        "endpoints": {
            "/": {
                "method": "GET",
                "description": "This endpoint"
            },
            "/telemetry": {
                "method": "POST",
                "content-type": "application/json",
                "description": "Ingests drone telemetry data",
            }
        }
    }


@app.route("/telemetry", methods=["POST"])
def post_telemetry():
    eventtype = "DroneDataReceived"
    event = CloudEvent({"type": eventtype, "source": "gateway"}, request.json)

    headers, body = to_binary(event)
    headers["Content-Type"] = "application/json"

    app.logger.info(f" Posted {eventtype} event to {broker}")
    r = requests.post(broker, data=body, headers=headers)
    app.logger.info(f"Broker response code: {r.status_code}")
    if not r.ok:
        r.raise_for_status()
        app.logger.error(r.raw)
        app.logger.error(r.text)

    return {"status": "Accepted"}, 202
