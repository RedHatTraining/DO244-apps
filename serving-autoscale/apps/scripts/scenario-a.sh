#!/bin/bash

# This script uses the HEY program to simulate traffic load for the exercise
# https://github.com/rakyll/hey

export SVC_URL=$(kn service describe financial-news -o url)
./hey -c 10 -n 10 $SVC_URL | grep responses
