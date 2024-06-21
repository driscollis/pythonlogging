# log_with_dict_config.py

import logging
import logging.config
import time


def main():
    log_config_dict = {
        "version": 1,
        "loggers": {
            "example_app": {
                "handlers": ["fileHandler", "consoleHandler"],
                "level": "INFO",
            },
        },
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "file_formatter",
                "filename": "dictconfig.log",
            },
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "formatter": "stream_formatter",
            },
        },
        "formatters": {
            "file_formatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "stream_formatter": {
                "format": "%(asctime)s - %(filename)s - %(lineno)s - %(message)s",
                "datefmt": "%a %d %b %Y",
            },
        },
    }
    logging.config.dictConfig(log_config_dict)
    logger = logging.getLogger("example_app")

    logger.info("Program started")
    time.sleep(3)
    logger.info("Done!")


if __name__ == "__main__":
    main()
