# code_config.py

import logging
import time


def main():
    """
    The main entry point of the application
    """
    logger = logging.getLogger("example_app")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    file_handler = logging.FileHandler("example.log")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # create the stream handler
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(lineno)d - %(message)s"
    )
    stream_handler.setFormatter(stream_formatter)

    # add handlers to logger object
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info("Program started")

    # Pretend to do some work
    time.sleep(2)

    logger.info("Done!")


if __name__ == "__main__":
    main()
