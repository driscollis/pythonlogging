# other_mod.py

import logging


def add(x, y):
    logger = logging.getLogger(name="test")
    logger.info("added %s and %s to get %s", x, y, x + y)
    return x + y
