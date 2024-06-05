# exception_decor.py

import functools


def exception(logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except:
                # log the exception
                err = "There was an exception in  "
                err += function.__name__
                logger.exception(err)

                # re-raise the exception
                raise

        return wrapper

    return decorator
