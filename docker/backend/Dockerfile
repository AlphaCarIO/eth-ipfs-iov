FROM node:8.11.3-jessie

MAINTAINER leo chan <leochan007@163.com>

ENV DEBIAN_FRONTEND noninteractive

RUN npm i -g pm2

WORKDIR /root

RUN git clone https://github.com/AlphaCarIO/alphacar-blockchain-service backend

RUN cd backend && npm i
