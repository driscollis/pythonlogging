# futures_thread_and_process.py

import concurrent.futures
import logging
import logging.config
import logging.handlers
import multiprocessing
import random
import threading
import time
import settings


logging.config.dictConfig(settings.LOGGING_CONFIG)


def logger_thread(queue):
    while True:
        log_record = queue.get()
        if log_record is None:
            break
        logger = logging.getLogger(log_record.name)
        logger.handle(log_record)


def worker_process(q):
    queue_handler = logging.handlers.QueueHandler(q)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(queue_handler)
    levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
              logging.CRITICAL]
    loggers = ['py', 'py.egg', 'py.egg.baby',
               'spam', 'spam.ham', 'spam.ham.eggs']
    for i in range(100):
        lvl = random.choice(levels)
        logger = logging.getLogger(random.choice(loggers))
        logger.log(lvl, 'Message no. %d', i)


def main():
    queue = multiprocessing.Manager().Queue(-1)

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            executor.submit(worker_process, queue)

    listener_process = threading.Thread(
        target=logger_thread,
        args=(queue, ))
    listener_process.start()
    # Do some work here
    time.sleep(3)

    # End the logger listener process and queue
    queue.put(None)
    listener_process.join()


if __name__ == '__main__':
    main()
