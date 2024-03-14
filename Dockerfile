FROM python:slim

RUN apt update
RUN apt install -y libssl-dev libffi-dev build-essential
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools

COPY /app /app

ENTRYPOINT [ "python", "/app/server.py" ]