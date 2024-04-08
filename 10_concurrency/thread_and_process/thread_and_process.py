# thread_and_process.py

import logging
import logging.config
import logging.handlers
import random
import threading
import time
import settings

from multiprocessing import Process, Queue


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
    queue = Queue()
    workers = []
    for i in range(5):
        worker = Process(
            target=worker_process,
            name='worker %d' % (i + 1),
            args=(queue,))
        workers.append(worker)
        worker.start()
    listener_process = threading.Thread(
        target=logger_thread,
        args=(queue, ))
    listener_process.start()
    # Do some work here
    time.sleep(3)
    for worker in workers:
        worker.join()
    # End the logger listener process
    queue.put(None)
    listener_process.join()


if __name__ == '__main__':
    main()
