FROM python:3.7-alpine

ARG BASE_URL="http://genrestest.nntc.pro"
ENV BASE_URL=$BASE_URL

LABEL "test_scenery"="APITests"
LABEL "creator"="ZAUR"

WORKDIR ./usr/tests

VOLUME /allureResults

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN apk update && apk upgrade && apk add bash

COPY . .

CMD pytest -s -v APITests --alluredir=AllureReport

