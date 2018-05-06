import urllib.request
try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat
    pass
import sys
import os
import time
import datetime
from tempmonitor import get_logger, logger_setup
from influxdb import InfluxDBClient

SAMPLING_RATE = 5  # How frequently to write sensor data to influxdb
INFLUXDB_HOST = os.environ.get("INFLUXDB_HOST", "localhost")
INFLUXDB_PORT = int(os.environ.get("INFLUXDB_PORT", "8086"))
INFLUXDB_USER = os.environ.get("INFLUXDB_USER", "root")
INFLUXDB_PASSWORD = os.environ.get("INFLUXDB_PASSWORD", "root")
INFLUXDB_DBNAME = os.environ.get("INFLUXDB_DBNAME", "sensehat")
INFLUXDB_SESSION = os.environ.get("INFLUXDB_SESSION", "sensehat")
INFLUXDB_RUNNUM = os.environ.get("INFLUXDB_RUNNUM", datetime.datetime.now().strftime("%Y%m%d%H%M"))


def get_data_points(hat: SenseHat, session, run_num):
    logger = get_logger(__name__)
    logger.info("test log")
    temperature = hat.get_temperature()
    humidity = hat.get_humidity()
    pressure = hat.get_pressure()
    timestamp = datetime.datetime.utcnow().isoformat()
    logger.info(
        f"{session} {run_num} Temperature: {round(temperature,1)}{u'u00b0'.encode('utf8')}C Pressure: {round(pressure,3)}mb Humidity: {round(humidity,1)}%")
    datapoints = [
        {
            "measurement": session,
            "tags": {"runNum": run_num,
                     },
            "time": timestamp,
            "fields": {
                "temperaturevalue": temperature, "pressurevalue": pressure, "humidityvalue": humidity
            }
        }
    ]
    return datapoints


def main():
    logger = logger_setup(__name__)
    logger.info("Starting data gathering daemon...")
    hat = SenseHat()
    dbclient = InfluxDBClient(
        INFLUXDB_HOST,
        INFLUXDB_PORT,
        INFLUXDB_USER,
        INFLUXDB_PASSWORD,
        INFLUXDB_DBNAME
    )
    while True:
        data = get_data_points(hat, INFLUXDB_SESSION, INFLUXDB_RUNNUM)
        bResult = dbclient.write_points(data)
        logger.info(f"Write points: {data} Bresult:{bResult}")
        hat.show_message("OK")
        time.sleep(SAMPLING_RATE)

