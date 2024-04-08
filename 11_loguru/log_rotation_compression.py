# log_rotation_compression.py

from loguru import logger

fmt = "{time} - {name} - {level} - {message}"

logger.add("compressed.log",
           format=fmt,
           level="DEBUG",
           rotation="50 B",
           compression="zip")
logger.debug("This is a debug message")
logger.info("This is an informational message")
for i in range(10):
    logger.info(f"Log message {i}")
