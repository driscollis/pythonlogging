# settings.py

LOGGING_CONFIG = {
    "version": 1,
    "loggers": {
        "__main__": {
            "handlers": ["rotatorFileHandler", "consoleHandler"],
            "level": "INFO",
        },
    },
    "handlers": {
        "rotatorFileHandler": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file_formatter",
            "filename": "rotating.log",
            "maxBytes": 20,
            "backupCount": 5,
        },
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "formatter": "stream_formatter",
        },
    },
    "formatters": {
        "file_formatter": {
            "format": "%(asctime)s - %(message)s",
        },
        "stream_formatter": {
            "format": "%(asctime)s - %(message)s",
            "datefmt": "%a %d %b %Y",
        },
    },
}
