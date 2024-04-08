# threaded_logging.py

import logging
import threading
import time

FMT = "%(relativeCreated)6d %(threadName)s %(message)s"


def worker(message):
    logger = logging.getLogger("main-thread")
    while not message["stop"]:
        logger.debug("Hello from worker")
        time.sleep(0.05)


def main():
    logger = logging.getLogger("main-thread")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("threaded.log")

    formatter = logging.Formatter(FMT)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    msg = {"stop": False}
    thread = threading.Thread(target=worker, args=(msg,))
    thread.start()
    logger.debug("Hello from main function")
    time.sleep(2)
    msg["stop"] = True

    thread.join()


if __name__ == "__main__":
    main()
