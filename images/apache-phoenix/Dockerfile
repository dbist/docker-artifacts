FROM dbist/apache-hbase:1.4.10 AS hbase
LABEL maintainer="generic13 at gmail dot com"
LABEL version="4.14.3RC1"
ENV REFRESHED_AT 2019_08_07
ARG PHOENIX_VERSION=4.14.3-HBase-1.4
ARG PHOENIX_NAME=apache-phoenix
ENV PHOENIX_URL https://dist.apache.org/repos/dist/dev/phoenix/apache-phoenix-$PHOENIX_VERSION-rc1/bin/apache-phoenix-$PHOENIX_VERSION-bin.tar.gz

RUN wget --no-verbose -O phoenix.tar.gz "$PHOENIX_URL" && \
    mkdir /opt/phoenix && \
    tar xf phoenix.tar.gz --strip-components=1 -C /opt/phoenix && \
    rm phoenix.tar.gz

RUN ln -sv /opt/phoenix/phoenix-*-server.jar /opt/hbase/lib/

ADD hbase-site.xml /opt/hbase/conf/hbase-site.xml
