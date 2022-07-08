# Create Serverless Functions by using the kn CLI

To create a serverless function using kn CLI:

$ kn func create -l python -t http function-name

## Using runtime language as 'Python'

The Weather Serverless Function is created using kn CLI.
The function is based out of 'Python as a runtime language' and some additional libraries.

## Installation

# Create the Python virtual environment
$ python3 -m venv .venv
# Activate the virtual environment
$ source .venv/bin/activate
# Install dev dependencies
$ pip install -r requirements.txt

## Testing the function

Navigate to the folder for your function that contains the test_func.py file.

Run the tests.

$ python3 test_func.py

## Building the function

$ kn func build -v -i image-name

## Deploying the function

$ kn func deploy image-name

