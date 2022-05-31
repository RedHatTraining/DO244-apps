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

## Running the function in local

$ export FLASK_APP=func.py
$ flask run

## Testing the function

Navigate to the URL on the browser: http://127.0.0.1:5000/weather/city/{nameofcity}
And enter the name of the city of which you want to check the weather details.

## Building the function

$ kn func build -v -i image-name

## Deploying the function

$ kn func deploy image-name

