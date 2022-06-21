     # python image
     FROM python:3.8

     ENV PYTHONUNBUFFERED 1

     # create a root directory in the container
     RUN mkdir /timecalender

     # Set the working directory
     WORKDIR /timecalender

     # Copy current directory contents into the container working directory
     ADD . /timecalender/

     # Install any needed dependencies
     COPY ./requirements.txt .
     RUN pip install -r requirements.txt
