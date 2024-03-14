#!/bin/bash
docker build --tag=shifumi .
docker run -p 1337:1337 --rm --name=shifumi -it shifumi