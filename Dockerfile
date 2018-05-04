FROM arm32v7/python:3-jessie

# NOTE: MUST RUN WITH --device /dev/gpiomem

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    npm \
    nginx \
    supervisor && \
    pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app
RUN pip3 install .
RUN cd /app/tempmonitor/web/static && npm install && npm run build
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY supervisor-tempmonitor.conf /etc/supervisor/conf.d/

CMD ["supervisord", "-n"]