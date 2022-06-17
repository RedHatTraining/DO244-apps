# Fraud Inspector

The Fraud Inspector is a simple Flask application that receives a POST request, and prints the content in the console.
This application is the source of the image `quay.io/redhattraining/do244-fraud-inspector:1.0`

## How to build the image

You can use `podman` to build the container image and push it to a registry:

```
$ podman build . -t quay.io/redhattraining/do244-fraud-inspector:1.0
$ podman push quay.io/redhattraining/do244-fraud-inspector:1.0
```

## Installation

The Fraud Inspector is a Python application with Flask so, in order to run in your local machine you need Python + some libraries.

A simple approach is to have different Python virtual environments per project. 
Execute the following command in the root of this project ot install a virtual environment:
 
```
$ python3 -m virtualenv venv
```

Once the virtual environment is installed in the project, you need to activate this new virtual environment. 
Execute the following command to activate it:

```
$ . venv/bin/activate
```

After the activation of the virtual environment you need to install all the requirements for the service (unless you did this step before). 
Execute the following command to install all the required libraries:

```
$ pip install -r requirements.txt
```

## Running the application in local environment

To run the Fraud Inspector application in local, execute the following commands:

```
$ cd src  
$ export FLASK_APP=api.py  
$ flask run 
```
 
## Running the application in a containerized environment
 
In order to run the Fraud Inspector application in containerized environment you need a container image. 
A prebuilt image is available in [quay.io](https://quay.io/repository/redhattraining/do244-fraud-inspector)
 