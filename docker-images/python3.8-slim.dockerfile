FROM python:3.8-slim

WORKDIR    /opt/oracle

RUN        apt-get update && apt-get install -y libaio1 wget unzip gcc \
            && wget https://download.oracle.com/otn_software/linux/instantclient/1916000/instantclient-basiclite-linux.x64-19.16.0.0.0dbru.zip \
            && unzip instantclient-basiclite-linux.*.zip \
            && rm -f instantclient-basiclite-linux.*.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig \
            && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

USER www-data

COPY ./app /app

WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 4000

CMD ["/start.sh"] 
