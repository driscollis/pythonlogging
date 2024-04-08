# structlog_exception_json.py

import logging
import structlog

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO)
)
logger = structlog.get_logger()
logger.info("A message before the exception")

try:
    10 / 0
except ZeroDivisionError:
    logger.exception("You cannot divide by zero!")
