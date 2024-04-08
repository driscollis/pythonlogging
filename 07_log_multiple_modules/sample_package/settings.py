# settings.py

LOG_CONFIG = {
    "version": 1,
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
            "level": "WARNING",
            "propagate": False,
        },
        "utils.minimath": {
            "handlers": ["fileHandler", "default"],
            "level": "DEBUG",
            "propagate": False,
        },
        "__main__": {  # if __name__ == '__main__'
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "file_formatter",
            "filename": "settings.log",
        },
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "stream_formatter",
        },
    },
    "formatters": {
        "file_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "stream_formatter": {
            "format": "%(asctime)s - %(name)s - %(filename)s - %(lineno)s - %(message)s",
            "datefmt": "%a %d %b %Y",
        },
    },
}
