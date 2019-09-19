FROM dbist/apache-phoenix:4.14.3 AS phoenix
LABEL maintainer="artemervits at gmail dot com"

COPY --chown=root:root pqs-entrypoint.sh /usr/local/bin/
RUN chmod 700 /usr/local/bin/pqs-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/pqs-entrypoint.sh", "-bash"]

EXPOSE 8765
