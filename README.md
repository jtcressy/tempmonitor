# tempmonitor

## Installation

1. Install any OS of choice on your raspberry pi and make sure you attach a SenseHAT
2. Install docker with `sudo apt install docker.io` or equivalent comamnd for your OS
3. Clone the repo to the pi and cd into the `tempmonitor` directory
4. Build the container with `sudo docker build -t tempmonitor:latest .`
5. Run the container with `sudo docker run --device /dev/gpiomem -v ./data:/data tempmonitor`
6. Watch the sensehat display light up with temperature status
7. Access web status at http://localhost:8080