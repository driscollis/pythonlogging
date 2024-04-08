# settings.py

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "detailed": {
            "class": "logging.Formatter",
            "format": "%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "thread_and_process.log",
            "mode": "w",
            "formatter": "detailed",
        },
        "pyfile": {
            "class": "logging.FileHandler",
            "filename": "thread_and_process-py.log",
            "mode": "w",
            "formatter": "detailed",
        },
        "errors": {
            "class": "logging.FileHandler",
            "filename": "thread_and_process-errors.log",
            "mode": "w",
            "level": "ERROR",
            "formatter": "detailed",
        },
    },
    "loggers": {"py": {"handlers": ["pyfile"]}},
    "root": {"level": "DEBUG", "handlers": ["console", "file", "errors"]},
}
