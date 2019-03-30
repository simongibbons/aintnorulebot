FROM python:3.7-alpine AS builder

RUN apk add zip bash

COPY . /app

WORKDIR /app

# Install dependencies
RUN mkdir -p package
RUN pip install -r requirements.txt --target package

ENV PYTHON_PATH /app/package

# Create Archive
RUN ./create_deployment_package.sh
