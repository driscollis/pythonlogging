# main.py

import gzip
import logging.config
import os
import shutil
import time

import settings

logging.config.dictConfig(settings.LOGGING_CONFIG)


def namer(filename):
    return f"{filename}.gz"


def rotator(source, destination):
    with open(source, "rb") as f_source:
        with gzip.open(destination, "wb") as f_dest:
            shutil.copyfileobj(f_source, f_dest)
    os.remove(source)


def main():
    logger = logging.getLogger(__name__)

    for handler in logger.handlers:
        if handler.name == "rotatorFileHandler":
            handler.namer = namer
            handler.rotator = rotator

    logger.debug("Logging is configured.")

    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)


if __name__ == "__main__":
    main()
