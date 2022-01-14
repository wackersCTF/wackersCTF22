FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev ncat

WORKDIR /app

COPY . /app

CMD ncat -klp 1338 -e wrapper.sh
