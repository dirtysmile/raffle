from selenium import webdriver
import time
import schedule
import sys
import logging

import open_chrome
import instagram
import eomisae
import simple_logger
import sneakerhouse


def handle_exception(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger("rich")

    logger.error("Unexpected exception", exc_info=(
        exc_type, exc_value, exc_traceback))


if __name__ == '__main__':
    logger = simple_logger.set_logger('test.log')
    sys.excepthook = handle_exception

    driver = open_chrome.connect()

    schedule.clear()
    schedule.every(2).minutes.do(eomisae.run)
    schedule.every(2).minutes.do(sneakerhouse.run, driver)
    # schedule.every(10).seconds.do(eomisae.run)

    eomisae.run()
    sneakerhouse.run(driver)

    while True:
        schedule.run_pending()
        time.sleep(1)
