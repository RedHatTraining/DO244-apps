from rich.progress import (
    Progress, TextColumn, BarColumn,
    TaskProgressColumn
)
import math
import time
import random


class Drone:

    name: str
    color: str
    mode: str
    battery: float
    mode: str
    speed: float

    def __init__(self, name, color, ability=1):
        self.name = name
        self.color = color
        self.ability = ability
        self.mode = "push"
        self.battery = 99
        self.speed = 0
        self.rand = random.Random(color)

    def move(self):
        if self.mode == "battery":
            self.speed = self.rand.uniform(0, 0.5)
        else:
            self.speed = self.rand.uniform(0, 1)

        self._update_status()

        return self.speed + self.ability

    def _update_status(self):

        self.ability += self.rand.uniform(0, 0.01)

        # drains or recovers battery based on speed
        self.battery += 0.5 + math.log(1 - self.speed)

        if self.battery < 0:
            self.battery = 0
            self.mode = "battery"

        if self.battery > 99:
            self.battery = 99
            self.mode = "push"

        if self.battery < 30:
            self.mode = "battery"

        # Back to push
        if self.battery > 80:
            self.mode = "push"


def race():
    drones = [
        Drone("Drone 1", "red", ability=1.11),
        Drone("Drone 2", "green", ability=1.41),
        Drone("Drone 3", "cyan", ability=0.86),
        Drone("Drone 5", "blue", ability=0.77),
        Drone("Drone 6", "white", ability=1.10),
    ]

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=50),
        TaskProgressColumn("[progress.percentage]{task.percentage:>3.0f} / 100 laps"),
    ) as progress:

        tasks = [
            progress.add_task(formatted_drone(d), total=10000)
            for d in drones
        ]

        while not progress.finished:
            for i, task in enumerate(tasks):
                drone = drones[i]
                advance = drone.move()
                progress.update(
                    task,
                    description=formatted_drone(drone),
                    advance=advance
                )

            time.sleep(0.05)


def formatted_drone(drone: Drone):
    if drone.mode == "push":
        mode = "( 🚀 Pushing  )"
    else:
        mode = "(⚡ Recharging)"

    return f"[bold {drone.color}]{drone.name}[/] - 🔋{drone.battery:.0f}% - {mode}"


race()
