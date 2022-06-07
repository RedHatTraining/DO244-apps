#!/bin/bash

# This script uses the HEY program to simulate traffic load for the exercise
# https://github.com/rakyll/hey

export SVC_URL=$(kn service describe financial-news -o url)
./hey -c 50 -z 10s "$SVC_URL?delay=3" | grep responses
