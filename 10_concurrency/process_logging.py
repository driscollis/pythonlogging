# process_logging.py

import logging
import logging.handlers
import multiprocessing
import time

from random import choice
from random import randint


LEVELS = [logging.DEBUG,
          logging.INFO,
          logging.WARNING,
          logging.ERROR,
          logging.CRITICAL]

LOGGERS = ["py_worker", "php_worker"]

MESSAGES = ["working hard",
            "taking a nap",
            "ERROR, ERROR, ERROR",
            "processing..."]


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("processed.log")
    formatter = logging.Formatter(
        ("%(asctime)s - %(processName)-10s - %(levelname)s - %(message)s")
    )
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)


def listener_process(queue, configurer):
    configurer()
    while True:
        try:
            log_record = queue.get()
            if log_record is None:
                break
            logger = logging.getLogger(log_record.name)
            logger.handle(log_record)
        except Exception:
            import sys, traceback
            print("Error occurred in listener", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

def worker_configurer(queue):
    queue_handler = logging.handlers.QueueHandler(queue)
    root = logging.getLogger()
    root.addHandler(queue_handler)
    root.setLevel(logging.DEBUG)

def worker_process(queue, configurer):
    configurer(queue)
    name = multiprocessing.current_process().name
    print(f"Worker started: {name}")
    for _ in range(10):
        time.sleep(randint(1, 5))
        logger = logging.getLogger(choice(LOGGERS))
        level = choice(LEVELS)
        message = choice(MESSAGES)
        logger.log(level, message)
    print(f"Worker finished: {name}")


def main():
    queue = multiprocessing.Queue(-1)
    listener = multiprocessing.Process(
        target=listener_process,
        args=(queue, setup_logging)
    )
    listener.start()
    workers = []
    for _ in range(10):
        worker = multiprocessing.Process(
            target=worker_process,
            args=(queue, worker_configurer)
        )
        workers.append(worker)
        worker.start()
    for task in workers:
        task.join()

    queue.put_nowait(None)
    listener.join()

if __name__ == '__main__':
    main()
