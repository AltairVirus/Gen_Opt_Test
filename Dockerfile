FROM python:3.7-alpine

LABEL "test_scenery"="APITests"
LABEL "creator"="ZAUR"

WORKDIR ./usr/tests

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip3 install -r requirements.txt

CMD pytest -s -v APITests/*
