# main.py

import logging

import other_mod


def main():
    """
    The main entry point of the application
    """
    logger = logging.getLogger(name="test")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("multi.log")
    logger.addHandler(file_handler)
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.info("Program started")
    result = other_mod.add(7, 8)
    logger.info("Done!")
    return result


if __name__ == "__main__":
    main()
