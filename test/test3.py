import logging
import logging.handlers
import sys

from rich.logging import RichHandler

RICH_FORMAT = "[%(filename)s:%(lineno)s] >> %(message)s"
FILE_HANDLER_FORMAT = "[%(asctime)s]\t%(levelname)s\t[%(filename)s:%(funcName)s:%(lineno)s]\t>> %(message)s"


def set_logger(log_path) -> logging.Logger:
    logging.basicConfig(
        level="NOTSET",
        format=RICH_FORMAT,
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    logger = logging.getLogger("rich")

    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(FILE_HANDLER_FORMAT))
    logger.addHandler(file_handler)

    return logger


def handle_exception(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger("rich")

    logger.error("Unexpected exception", exc_info=(
        exc_type, exc_value, exc_traceback))


if __name__ == '__main__':
    logger = set_logger('test.log')
    sys.excepthook = handle_exception

    for i in range(3, -1, -1):
        try:
            num = 1/i
        except:
            raise ZeroDivisionError()
        logger.info(f"1/{i} = {num}")
