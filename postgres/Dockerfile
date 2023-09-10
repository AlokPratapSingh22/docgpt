FROM postgres:15

RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y make \
    && apt-get install -y git \
    && apt-get install -y postgresql-server-dev-15 \
    && apt-get install -y postgresql-common \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && git clone --branch v0.4.1 https://github.com/pgvector/pgvector.git \
    && cd pgvector \
    && export PG_CONFIG=/usr/lib/postgresql/15/bin/pg_config \
    && make install

# Comment out below 3 lines.
# RUN mkdir -p /etc/postgresql/15/main/
# RUN echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf
# RUN echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf

EXPOSE 5432
