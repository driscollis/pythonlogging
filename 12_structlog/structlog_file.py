# structlog_file.py

import logging
import structlog

from pathlib import Path


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    logger_factory=structlog.WriteLoggerFactory(
            file=Path("app").with_suffix(".log").open("wt")
            )
)
logger = structlog.get_logger()
logger.info("This is an info message")
