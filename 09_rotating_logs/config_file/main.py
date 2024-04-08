# main.py

import logging.config
import settings
import time

logging.config.dictConfig(settings.LOGGING_CONFIG)


def main():
    logger = logging.getLogger(__name__)
    logger.debug("Logging is configured.")

    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)


if __name__ == "__main__":
    main()
