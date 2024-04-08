# catching_exceptions.py

from loguru import logger

@logger.catch
def silly_function(x, y, z):
    return 1 / (x + y + z)

def main():
    fmt = "{time:HH:mm:ss} - {name} - {level} - {message}"
    logger.add("exception.log", format=fmt, level="INFO")
    logger.info("Application starting")
    silly_function(0, 0, 0)
    logger.info("Finished!")

if __name__ == "__main__":
    main()
