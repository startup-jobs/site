FROM debian:jessie
MAINTAINER Robert George <robert@poovelil.org>

RUN apt-get update && apt-get install -y python \
	curl \
	libpq-dev \
	python-dev \
	gcc

RUN  curl -L https://bootstrap.pypa.io/get-pip.py | python

RUN pip install Django
RUN pip install psycopg2 
RUN apt-get purge -y curl
