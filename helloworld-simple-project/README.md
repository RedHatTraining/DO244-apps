# hello-quarkus  Project

This project uses Quarkus, the Supersonic Subatomic Java Framework.

If you want to learn more about Quarkus, please visit its website: https://quarkus.io/ .


## Creating a Serverless Function

For Quarkus,
                  kn func create -l quarkus -t http function-name
                  

## Building a Serverless Function

                                kn func build
                                

## Quarkus Dev Mode

In a termainal, chnage drectory to come at the project-directory & execute

                              ./mvnw quarkus:dev

And once the app is successfully up, the banner of QUARKUS appears on the terminal.

## For testing the Quarkus Application

For testing the Quarkus functions locally on your computer by running the Maven tests that are included in the project template.

- We open a new terminal in the project directory and run

                                 ./mvnw test
                                 
And second way is to test the application using unit testing

  - Once the application is up, on the terminal we have to press r to resume testing for the unit test classes mentioned.

## Deploying the Serverless Function

                                 kn func deploy -v
