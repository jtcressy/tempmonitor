import argparse
import os
from tempmonitor.web import app

try:
    from tempmonitor.daemon import main as dmain
except ImportError:
    print("Daemon unavailable when not running on a raspberrypi! ")


def main():
    parser = argparse.ArgumentParser(description="Start tempmonitor daemon or web server")
    parser.add_argument('--daemon', dest='daemon', action="store_true", help="Start in daemon mode")
    parser.add_argument('--web', dest='web', action="store_true", help="Start in web server mode")
    args = parser.parse_args()
    if args.web:
        app.run(host=os.environ.get("WEBHOST", "0.0.0.0"), port=os.environ.get("WEBPORT", "8080"))
    else:
        dmain()
