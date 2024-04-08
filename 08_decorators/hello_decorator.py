# hello_decorator.py


def info(func):
    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        print(f"Function docstring: {func.__doc__}")
        return func(*args)

    return wrapper


@info
def doubler(number):
    """Doubles the number passed to it"""
    return number * 2


print(doubler(4))
