# minimath.py
import logging

module_logger = logging.getLogger(__name__)


def add(x, y):
    module_logger.info("Adding %s and %s", x, y)
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y
