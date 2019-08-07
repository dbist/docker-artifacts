FROM dbist/apache-phoenix-pqs:4.14.3RC1
LABEL maintainer="generic13 at gmail dot com"
LABEL version="4.14.3RC1"
ENV REFRESHED_AT 2019_08_07

RUN apt-get update
RUN apt-get install -y python3 python3-pip
WORKDIR app/
COPY requirements.txt app/
RUN pip3 install -r app/requirements.txt

EXPOSE 8765
