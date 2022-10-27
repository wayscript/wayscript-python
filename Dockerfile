FROM python:3.10 AS base
LABEL org.wayscript.image.authors="founders@wayscript.com"

RUN apt-get update && apt-get -yu dist-upgrade

ENV SRC_DIR /usr/local/src/project
WORKDIR ${SRC_DIR}

RUN pip3 install --upgrade pip

RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ${SRC_DIR}/

RUN pipenv install --system --dev && \
    rm -rf /root/.cache/pip

COPY ./files/ /

COPY ./ ${SRC_DIR}/

RUN chmod u+x /usr/local/bin/*
