FROM python:3.10.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /mysite

COPY . /mysite/

RUN apt-get update

RUN apk add --update --no-cache --virtual build-deps gcc python3-dev musl-dev bash gcc libc-dev linux-headers postgresql-dev postgresql-client libffi-dev gettext

COPY ./requirements.txt .

RUN pip3 install --upgrade pip && \
pip3 install --no-cache-dir -r requirements.txt
