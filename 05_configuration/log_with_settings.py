# log_with_settings.py

import logging
import time

import settings


def main():
    logger = logging.getLogger("example_app")

    logger.info("Program started")
    time.sleep(3)
    logger.info("Done!")


if __name__ == "__main__":
    main()
