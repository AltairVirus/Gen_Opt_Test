FROM python:3.7-alpine

ENV BASE_URL="http://genrestest.nntc.pro"

LABEL "test_scenery"="APITests"
LABEL "creator"="ZAUR"

WORKDIR ./usr/tests

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN apk update && apk upgrade && apk add bash

COPY . .

CMD pytest -s -v APITests --alluredir=AllureResult

