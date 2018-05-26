FROM ubuntu:16.04

MAINTAINER leo chan <leochan007@163.com>

ENV DEBIAN_FRONTEND noninteractive

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak

RUN  echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse \n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse \n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse \n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse \n\
##测试版源 \n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse \n\
##源码 \n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse \n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse \n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse \n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse \n\
##测试版源 \n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse \n\
# Canonical 合作伙伴和附加 \n\
deb http://archive.canonical.com/ubuntu/ xenial partner \n" \
    >> /etc/apt/sources.list
    
RUN apt-get update

RUN apt-get install -y apt-utils

WORKDIR /root

ADD *.sh ipfs /root/

RUN chmod +x *.sh && ./install.sh

CMD ["/bin/bash"]
