FROM arm32v7/python:3-jessie

# NOTE: MUST RUN WITH --device /dev/gpiomem

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    npm && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip setuptools

COPY . /app

WORKDIR /app
RUN pip3 install .
RUN cd /app/tempmonitor/web/static && npm install && npm run build

# Run container with --web or --daemon, defaults to daemon
CMD ["tempmonitor"]
