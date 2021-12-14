import sys
import logging

import simple_logger


def handle_exception(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger("rich")

    logger.error("Unexpected exception", exc_info=(
        exc_type, exc_value, exc_traceback))


if __name__ == '__main__':
    logger = simple_logger.set_logger('test.log')
    sys.excepthook = handle_exception

    for i in range(3, -1, -1):
        try:
            num = 1/i
        except:
            raise ZeroDivisionError()
        logger.info(f"1/{i} = {num}")
