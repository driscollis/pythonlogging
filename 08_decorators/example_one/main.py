# main.py

from exception_decor import exception


@exception
def zero_divide():
    1 / 0


if __name__ == "__main__":
    zero_divide()
