FROM gcr.io/spark-operator/spark-py:v3.1.1

USER root:root

RUN mkdir -p /app

COPY ../app/ /app

WORKDIR /app

USER root
