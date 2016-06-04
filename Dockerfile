FROM tiangolo/uwsgi-nginx-flask:flask
MAINTAINER Angel Rivera

RUN pip install --upgrade pip
RUN pip install flask pymongo


COPY ./app /app

