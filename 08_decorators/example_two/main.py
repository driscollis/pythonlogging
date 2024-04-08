# main.py

from exception_decor import exception
from exception_logger import logger


@exception(logger)
def zero_divide():
    1 / 0


if __name__ == "__main__":
    zero_divide()
