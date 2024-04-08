# log_with_config.py

import logging
import logging.config
import time


def main():
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("example_app")

    logger.info("Program started")
    time.sleep(3)
    logger.info("Done!")


if __name__ == "__main__":
    main()
