FROM openjdk:8
LABEL maintainer="artemervits at gmail dot com"

ARG HBASE_VERSION=1.4.10
ARG HBASE_DIR=${pwd}

ENV HBASE_URL "https://www-us.apache.org/dist/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-bin.tar.gz"

RUN wget --no-verbose -O hbase.tar.gz "$HBASE_URL" && \
    mkdir /opt/hbase && \
    tar xf hbase.tar.gz --strip-components=1 -C /opt/hbase && \
    rm hbase.tar.gz

ADD hbase-site.xml /opt/hbase/conf/hbase-site.xml

ENV HBASE_CONF_DIR /opt/hbase/conf
ENV HBASE_CP /opt/hbase/lib
ENV HBASE_HOME /opt/hbase

COPY --chown=root:root hbase-entrypoint.sh /usr/local/bin/
RUN chmod 700 /usr/local/bin/hbase-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/hbase-entrypoint.sh", "-bash"]

EXPOSE 16010
