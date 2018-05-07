FROM arm32v7/python:3-jessie

# NOTE: MUST RUN WITH --device /dev/gpiomem

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    python3-numpy \
    python3-pil \
    git \
    npm && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip setuptools

COPY . /app

WORKDIR /app
RUN pip3 install -e .
# RUN cd /app/tempmonitor/web/static && npm install && npm run build

# Run container with --web or --daemon, defaults to daemon
CMD ["tempmonitor"]
