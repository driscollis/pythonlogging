# file_formatting.py

from loguru import logger

fmt = "{time} - {name} - {level} - {message}"

logger.add("formatted.log", format=fmt, level="INFO")
logger.debug("This is a debug message")
logger.info("This is an informational message")
