#! /bin/bash

docker build -t aintnorulebot:latest .
docker run --rm --entrypoint cat aintnorulebot:latest /app/function.zip > function.zip
