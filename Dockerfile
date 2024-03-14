FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools

COPY /app /app

ENTRYPOINT [ "python", "/app/server.py" ]