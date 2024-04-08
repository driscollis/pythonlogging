# structlog_set_level.py

import logging
import structlog

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO)
)
logger = structlog.get_logger()
logger.debug("This is a debug message")
logger.info("Hello %s", "Mike", key=12, my_list=[5, 6, 7])
