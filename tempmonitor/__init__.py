import logging
import sys
from os import environ


def logger_setup(module_name=__name__, log_level=logging.INFO):
    logger = logging.getLogger(module_name)
    loghandler = logging.StreamHandler(stream=sys.stdout)
    logfilehandler = logging.FileHandler(f"{module_name}.log", mode="a", encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    loghandler.setFormatter(formatter)
    logfilehandler.setFormatter(formatter)
    if len(logger.handlers) < 1:
        logger.addHandler(loghandler)
        logger.addHandler(logfilehandler)
    loglevels = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "WARN": logging.WARN,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }
    loglevel = loglevels.get(environ.get("NSABOT_LOGLEVEL", "INFO").upper(), log_level)
    logger.setLevel(loglevel)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            logger.info(f"Logfile location: {handler.baseFilename}")
    return logger


def get_logger(module_name=__name__):
    return logging.getLogger(module_name)
