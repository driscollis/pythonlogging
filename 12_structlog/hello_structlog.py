# hello_structlog.py

import structlog

logger = structlog.get_logger()
logger.info("Hello %s", "Mike", key=12, my_list=[5, 6, 7])
