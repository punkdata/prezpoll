FROM tiangolo/uwsgi-nginx-flask:flask
MAINTAINER Angel Rivera

RUN pip install flask pymongo


COPY ./app /app

