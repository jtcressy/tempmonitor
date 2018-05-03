FROM arm32v7/python:3-jessie

# NOTE: MUST RUN WITH --device /dev/gpiomem

COPY . /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    nginx \
    supervisor && \
    pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install .

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY supervisor-app.conf /etc/supervisor/conf.d/

CMD ["supervisord", "-n"]