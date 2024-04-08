# log_levels.py

import logging

logging.basicConfig(filename="log_levels.log", level=logging.WARNING)

logging.debug("Hello debug")
logging.info("Hello info")
logging.warning("Hello warning")
logging.error("Hello error")
logging.critical("Hello critical!")
