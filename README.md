# Time Availability API
- Working internationally comes with its own set of challenges, among them is the challenge of figuring out when people are available. This API can be used to calculate the best meeting slots across time zones

## How to use and Test this application
- Clone or download the repo. In the root folder terminal, run the command `make start` to start up the program server, and run migrations.
- To test the API visit `http://127.0.0.1:8000/api/timeslot` and test with a sample data. An example is shown below:


https://user-images.githubusercontent.com/51092098/176506710-6ae5adb7-bafa-4401-9a19-3de1f7425117.mov


- You can also test the API route above via postman. 
- To run functions tests only, run `make test`
- To shut down the container, run `make down`

## Steps taken to reduce latency
- I avoided the use of third-party APIs, as this could generally slow down response time.
- I made good use of inbuilt and third-party libraries.
- Most of the clean-up logic was done with simple and efficient algorithms.

## Technologies
* [Python 3](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration
