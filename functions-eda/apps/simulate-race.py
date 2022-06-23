import os
import math
import time
import random
from typing import Dict, List

import click
import requests
from click import secho, echo


TELEMETRY_GATEWAY_URL = os.environ.get(
    "TELEMETRY_GATEWAY_URL",
    "https://gateway-developer-functions-eda.apps.ocp4.example.com/telemetry"
)


class Drone:

    name: str
    color: str
    mode: str
    battery: float
    mode: str
    speed: float

    def __init__(self, name: str, color: str, ability=1):
        self.name = name
        self.color = color
        self.ability = ability
        self.mode = "push"
        self.battery = 99.0
        self.signal = 100.0
        self.speed = 0.0
        self.rand = random.Random(color)

    def move(self):
        if self.mode == "battery":
            self.speed = self.rand.uniform(0, 0.1)
        else:
            self.speed = self.rand.uniform(0.5, 1)

        self._update_status()

        return self.speed + self.ability

    def _update_status(self):

        self.ability += self.rand.uniform(0, 0.01)

        # drains or recovers battery based on speed
        self.battery += (0.5 + math.log(1 - self.speed)) * 10

        if self.battery < 30:
            self.mode = "battery"

        if self.battery < 0:
            self.battery = 0

        if self.battery > 99:
            self.battery = 99

        # Back to push
        if self.battery > 80:
            self.mode = "push"

        self.signal = self.rand.uniform(0, 100)

        self._send_telemetry()

    def _send_telemetry(self):
        data = {
            "droneId": self.name,
            "battery": self.battery,
            "signal": self.signal,
            "speed": self.speed
        }

        echo(f"Sending {self.name} telemetry...", nl=False)
        try:
            r = requests.post(
                TELEMETRY_GATEWAY_URL,
                json=data,
                verify="/etc/pki/tls/certs/ca-bundle.crt"
            )
            if r.ok:
                secho("OK", fg="green", bold=True)
            else:
                secho(
                    f"\nReceived error code from {TELEMETRY_GATEWAY_URL}",
                    fg="red",
                    bold=True
                )
                secho(f"HTTP Error {r.status_code} {r.text}")
        except requests.exceptions.RequestException as err:
            secho(
                f"Could not send telemetry data to {TELEMETRY_GATEWAY_URL}",
                fg="red",
                bold=True
            )
            echo(err)


def race():
    drones = [
        Drone("Drone A", "red", ability=1),
        Drone("Drone B", "green", ability=1),
        Drone("Drone C", "cyan", ability=1),
        Drone("Drone D", "blue", ability=1),
    ]

    progress = [
        {"drone": d, "progress": 0}
        for d in drones
    ]

    while True:
        for p in progress:
            drone: Drone = p["drone"]
            p["progress"] += drone.move()
            time.sleep(0.2)

        progress.sort(key=sort_drone_progress, reverse=True)

        echo_progress(progress)


def sort_drone_progress(drone_progress: Dict):
    return drone_progress["progress"]


def echo_progress(progress: List[Dict]):
    click.clear()
    secho('\n\n== Race progress ==\n', fg="white", bold=True)
    secho('Pos\tDrone\t\tDistance\tBattery', bold=True)

    for i, p in enumerate(progress, start=1):
        drone: Drone = p["drone"]
        drone_progress: float = p["progress"]
        secho(
            f"{i}\t{drone.name}\t\t{drone_progress:.1f}"
            f"\t\t{drone.battery:.0f} %",
            fg=drone.color
        )

    echo("\n")


if __name__ == "__main__":
    echo(f"\nTelemetry Gateway URL: {TELEMETRY_GATEWAY_URL}\n")

    time.sleep(1)

    race()
