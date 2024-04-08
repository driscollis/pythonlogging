# terminal_formatting.py
import sys
from loguru import logger

fmt = ("<red>{time}</red> - "
       "<yellow>{name}</yellow> - "
       "{level} - {message}")

logger.add(sys.stdout, format=fmt, level="DEBUG")
logger.debug("This is a debug message")
logger.info("This is an informational message")
