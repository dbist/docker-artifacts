FROM dbist/apache-phoenix-pqs:4.14.2
LABEL maintainer="artemervits at gmail dot com"

RUN apt-get update
RUN apt-get install -y python3 python3-pip
WORKDIR app/
COPY requirements.txt app/
RUN pip3 install -r app/requirements.txt

EXPOSE 8765
