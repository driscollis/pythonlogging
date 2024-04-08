# log_rotation.py

from loguru import logger

fmt = "{time} - {name} - {level} - {message}"

logger.add("rotated.log",
           format=fmt,
           level="DEBUG",
           rotation="50 B")
logger.debug("This is a debug message")
logger.info("This is an informational message")
