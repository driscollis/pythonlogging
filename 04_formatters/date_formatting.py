# date.py

import logging

# Create custom logger
logger = logging.getLogger(name="datefmt")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("datefmt.log")

# add handler to logger
logger.addHandler(file_handler)

# add formatter
datefmt = "%a %d %b %Y"
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt=datefmt
)
file_handler.setFormatter(formatter)

logger.debug("Hello debug")
logger.info("Hello info")
