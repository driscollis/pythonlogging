# context_filter.py

import logging
from random import choice


class ContextFilter:
    USERS = ["Mike", "Stephen", "Rodrigo"]
    LANGUAGES = ["Python", "PHP", "Ruby", "Java", "C++"]

    def filter(self, record):
        record.user = choice(ContextFilter.USERS)
        record.language = choice(ContextFilter.LANGUAGES)
        return True


if __name__ == "__main__":
    levels = (
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    )
    logger = logging.getLogger(name="test")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    my_filter = ContextFilter()
    handler.addFilter(my_filter)
    logger.addHandler(handler)

    fmt = "%(asctime)s - %(name)s - %(levelname)-8s User: %(user)-8s Lang: %(language)-8s %(message)s"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.info("This is an info message with %s", "silly parameters")
    for _ in range(10):
        level = choice(levels)
        level_name = logging.getLevelName(level)
        logger.log(level, "A message with %s level", level_name)
