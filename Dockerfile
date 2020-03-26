FROM python:3.8-slim

WORKDIR /opt/app
COPY . /opt/app

RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    apt-get -y install libsndfile1-dev  && \
    apt-get -y install ffmpeg && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt
