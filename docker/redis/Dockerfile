FROM redis:4

MAINTAINER leo chan <leochan007@163.com>

ENV DEBIAN_FRONTEND noninteractive

COPY redis.conf /usr/local/etc/redis/redis.conf

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

#CMD ["/bin/bash"]
