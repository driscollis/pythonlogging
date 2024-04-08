# async_logging.py

import asyncio
import logging
import logging.handlers
import random

from queue import SimpleQueue

MESSAGES = ["working hard",
            "taking a nap",
            "ERROR, ERROR, ERROR",
            "processing..."]


async def setup_logging():
    log_queue = SimpleQueue()
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # Create a non-blocking handler
    queue_handler = logging.handlers.QueueHandler(log_queue)
    root.addHandler(queue_handler)

    # Create a blocking handler
    file_handler = logging.FileHandler("queued.log")
    formatter = logging.Formatter(
        ("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    file_handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(
        log_queue, file_handler)
    try:
        listener.start()
        logging.debug("Async logging started")
        while True:
            await asyncio.sleep(60)
    finally:
        logging.debug("Logger is being shut down!")
        listener.stop()


async def task(number):
    logging.info(f"Starting task #{number}")
    await asyncio.sleep(random.randint(1, 5))
    msg = random.choice(MESSAGES)
    logging.info(f"Task {number} is {msg}")
    logging.info(f"Task #{number} is finished")


async def main():
    # initialize the logger
    asyncio.create_task(setup_logging())
    await asyncio.sleep(0.1)

    logging.info("Main function started")

    async with asyncio.TaskGroup() as group:
        for t in range(10):
            group.create_task(task(t))

    logging.info("All work done")


if __name__ == "__main__":
    asyncio.run(main())
