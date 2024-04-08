# two_handlers.py

import logging

# Create custom logger
logger = logging.getLogger(name="test")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("two_handlers.log")
stream_handler = logging.StreamHandler()

# add handler to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug("Hello debug")
logger.info("Hello info")
