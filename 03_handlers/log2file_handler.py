# log2file_handler.py

import logging

# Create custom logger
logger = logging.getLogger(name="test")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test_handler.log")

# add handler to logger
logger.addHandler(file_handler)

logger.debug("Hello debug")
logger.info("Hello info")
