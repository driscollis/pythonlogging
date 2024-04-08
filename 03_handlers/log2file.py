# log2file.py

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.debug("Hello debug")
logging.info("Hello info")
