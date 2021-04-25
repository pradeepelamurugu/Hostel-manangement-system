FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /hostelapp

ADD . /hostelapp

COPY ./requirements.txt /hostelapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /hostelapp