FROM python:3.7-alpine
MAINTAINER Communal Cloud

ENV PYTHONUNBUFFERED 1

#Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#Copy django app to docker container
RUN mkdir /api
WORKDIR /api
COPY ./api /api