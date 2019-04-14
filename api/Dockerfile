FROM python:3.7-alpine
LABEL Communal Cloud

ENV PYTHONUNBUFFERED 1

#Create a folder for gunicorn can save its log files
RUN mkdir -p /var/log/gunicorn

#Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#Copy django app to docker container
RUN mkdir /api
WORKDIR /api
COPY . /api