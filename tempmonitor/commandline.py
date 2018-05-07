import argparse
import os
from tempmonitor.web import app
from tempmonitor import logger_setup

try:
    from tempmonitor.daemon import main as dmain
except ImportError as e:
    print(f"Daemon unavailable when not running on a raspberrypi! {e}")


def main(argv):
    logger = logger_setup()
    parser = argparse.ArgumentParser(description="Start tempmonitor daemon or web server")
    parser.add_argument('--daemon', dest='daemon', action="store_true", help="Start in daemon mode")
    parser.add_argument('--web', dest='web', action="store_true", help="Start in web server mode")
    args = parser.parse_args(argv[1:])
    if args.web:
        app.run(host=os.environ.get("WEBHOST", "0.0.0.0"), port=os.environ.get("WEBPORT", "8080"))
    else:
        try:
            dmain()
        except KeyboardInterrupt:
            logger.info("Keyboard Interrupt. Exiting.")

