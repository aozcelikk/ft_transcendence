FROM nginx:alpine

RUN apk update && apk add openssl

COPY ./certs/* /etc/ssl/certs/

COPY ./conf/default.conf /etc/nginx/conf.d/default.conf
