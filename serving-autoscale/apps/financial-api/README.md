# Financial API

The Financial API is a small application written in [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com) which returns financial news. 
It Comes with CORS enabled, so it can be used from browsers.

## How it works

The application exposes a `GET` endpoint `/` on port `5000` by default. 
Once a GET request hits the service, the application loads the list of news from the `data/finance.json` file, picks 3 randomly and returns the list sorted by their timestamp.

## Installation

The Financial API is a Python application with Flask so, in order to run in your local machine you need Python + some libraries.

A simple approach is to have different Python virtual environments per project. 
Execute the following command in the root of this project ot install a virtual environment:
 
```
$ python3 -m virtualenv venv
```

Once the virtual environment is installed in the project, you need to activate this new virtual environment. 
Execute the following command to activate it:

```
. venv/bin/activate
```

After the activation of the virtual environment you need to install all the requirements for the service (unless you did this step before). 
Execute the following command to install all the required libraries:

```
pip install -r requirements.txt
```

## Running the application in local environment

To run the Financial API in local, execute the following commands:

```
$ cd src  
$ export FLASK_APP=api.py  
$ flask run 
```
 
## Running the application in a containerized environment
 
In order to run the Financial API in containerized environment you need a container image. 
A prebuilt image is available in [quay.io](https://quay.io/repository/redhattraining/do244-financial-api)
 