# more_log_formatting.py

import logging

# Create custom logger
logger = logging.getLogger(name="formatting")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("formatting.log")

# add handler to logger
logger.addHandler(file_handler)

# add formatter
fmt = "%(asctime)s - %(filename)s - %(lineno)d - %(message)s"
# fmt = "%(asctime)s - %(pathname)s - %(module)s - %(message)s"
formatter = logging.Formatter(fmt)
file_handler.setFormatter(formatter)

logger.debug("Hello debug")
logger.info("Hello info")
