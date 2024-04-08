# log_exception.py

import logging

logger = logging.getLogger("excepter")
logger.setLevel(logging.INFO)


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logger.exception("An error has occurred!")
    except TypeError:
        logger.exception("Incompatible types!")
    else:
        return result


if __name__ == "__main__":
    divide(1, 0)
