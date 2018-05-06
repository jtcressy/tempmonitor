# tempmonitor

## Installation

1. Install any OS of choice on your raspberry pi and make sure you attach a SenseHAT
2. Install docker with `sudo apt install docker.io` or equivalent comamnd for your OS
3. Clone the repo to the pi and cd into the `tempmonitor` directory
4. Create the influxdb, grafana, and tempmonitor containers with `sudo docker-compose up --no-start`
6. Sense hat display should say "OK"
7. Access grafana UI at http://localhost:3000