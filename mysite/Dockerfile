FROM python:3.10.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /mysite

COPY . /mysite/

RUN apt-get update

COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
