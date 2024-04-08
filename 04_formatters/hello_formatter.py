# hello_formatter.py

import logging

# Create custom logger
logger = logging.getLogger(name="test")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test_formatter.log")

# add handler to logger
logger.addHandler(file_handler)

# add formatter
formatter = logging.Formatter()
file_handler.setFormatter(formatter)

logger.debug("Hello debug")
logger.info("Hello info")
