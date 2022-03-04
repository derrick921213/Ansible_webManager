FROM alpine:latest
WORKDIR /code
COPY . /code
RUN apk upgrade --no-cache && apk update --no-cache && apk add --no-cache bash python3 py3-pip && pip3 install pipenv && cd /code && pipenv --python 3.9 
SHELL ["/bin/bash"]


