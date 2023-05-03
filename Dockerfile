FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements /requirements

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements/base.txt

COPY ./src /code/src
