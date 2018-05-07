FROM arm32v7/python:3-stretch

# NOTE: MUST RUN WITH --device /dev/gpiomem

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    python3 \
    python3-pip \
    git \
    npm && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip setuptools

COPY . /app

WORKDIR /app
RUN apt-get update && \
    apt-get install -y \
    python3-pil \
    python3-numpy && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install -e .
# RUN cd /app/tempmonitor/web/static && npm install && npm run build

# Run container with --web or --daemon, defaults to daemon
CMD ["tempmonitor"]
