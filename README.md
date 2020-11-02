# greendeck_test
Project on Django (Task -1)
CRUD:-  Create, Read, Update and Delete, 

To cover listing of large data sets which bring additional complexity such as pagination when the data sets are too large to be easily held in memory.

Simple but beautiful web-based user interface.
Easy-to-upload JSON or CSV files.
Easy-to-add new information.
Easy-to-deal with all the data.
Get start with minimally one command. 

Get started
Requirements:-

VS CODE:-Visual Studio Code is a lightweight but powerful source code editor

Docker:- Docker is a platform for developers and sysadmins to build, run, and share applications with containers. The use of containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

Django:-Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

Postman:-Postman is a collaboration platform for API development.

Language:-  Python.




Creating Docker Container:-

Create Dockerfile in project directory.
This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory. The parent image is further modified by installing the Python requirements defined in the requirements.txt file.

Create requirements.txt file in project directory.
All the requirements of the project which is required to install are write in this file.
This file is used by the RUN pip install -r requirements.txt command in your Dockerfile.
Dockerfile will install all the requirement witch are mentions in the requirements.txt



Create docker-compose.yml file in project directory.
The docker-compose.yml file describes the services that make our app. In this project those services are a web server and database.This file defines two services: The db service and the web service.



Run this command in Terminal of project directory.

This will create your container.


Creating Django project through Docker, 
   Run this command in Terminal of project directory.

Django project will create.





























For Database connect change in settings.py  the database setting.


To start project run this command. Project will start and show the result.

This is the local server on witch is use to host project






This local server show front page of the project in witch we can add our data



After adding data we click on Add button that will save the input data in database.
On clicking on All Data it will show all the data we have uploaded.
We can Edit or Delete data from clicking on Edit or Delete button.Testing our project on Postman
Data saved through Postman

