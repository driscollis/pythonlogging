# settings.py

import logging
import logging.config

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
            "filename": "settings.log",
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
