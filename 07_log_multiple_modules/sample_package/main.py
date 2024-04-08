# main.py

import logging.config
import settings
from utils import minimath

logging.config.dictConfig(settings.LOG_CONFIG)


def main():
    log = logging.getLogger(__name__)
    log.debug("Logging is configured.")

    minimath.add(4, 5)


if __name__ == "__main__":
    main()
