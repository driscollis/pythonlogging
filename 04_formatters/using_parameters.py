# using_parameters.py

import logging

# Create custom logger
logger = logging.getLogger(name="test")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("params.log")

# add handler to logger
logger.addHandler(file_handler)

# add formatter
formatter = logging.Formatter()
file_handler.setFormatter(formatter)

name = "Mike"
logger.debug("Nice to meet you, %s", name)
