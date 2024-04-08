# log_formatting.py

import logging

# Create custom logger
logger = logging.getLogger(name="test")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("formatted.log")

# add handler to logger
logger.addHandler(file_handler)

# add formatter
formatter = logging.Formatter(("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
file_handler.setFormatter(formatter)

logger.debug("Hello debug")
logger.info("Hello info")
