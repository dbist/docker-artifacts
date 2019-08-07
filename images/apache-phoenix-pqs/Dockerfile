FROM dbist/apache-phoenix:4.14.3RC1 AS phoenix
LABEL maintainer="generic13 at gmail dot com"
LABEL version="4.14.3RC1"
ENV REFRESHED_AT 2019_08_07

COPY --chown=root:root pqs-entrypoint.sh /usr/local/bin/
RUN chmod 700 /usr/local/bin/pqs-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/pqs-entrypoint.sh", "-bash"]

EXPOSE 8765
