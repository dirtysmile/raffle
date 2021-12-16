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
import nikesnkrs


def handle_exception(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger("rich")

    logger.error("Unexpected exception", exc_info=(
        exc_type, exc_value, exc_traceback))


if __name__ == '__main__':
    logger = simple_logger.set_logger('rich', 'test.log')
    sys.excepthook = handle_exception

    driver = open_chrome.connect()

    schedule.clear()
    # [어미새] 2분
    schedule.every(2).minutes.do(eomisae.run)

    # [나이키 SNKRS] 12시 18시
    schedule.every().day.at("12:00:00").do(nikesnkrs.run)
    schedule.every().day.at("18:00:00").do(nikesnkrs.run)

    # [스니커 하우스] 10시 14시 17시 20시
    # schedule.every().day.at("10:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("12:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("14:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("16:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("18:00:00").do(sneakerhouse.run, driver)

    # schedule.every(2).minutes.do(sneakerhouse.run, driver)
    # schedule.every(10).seconds.do(nikesnkrs.run)

    eomisae.run()
    nikesnkrs.run()
    # sneakerhouse.run(driver)

    while True:
        schedule.run_pending()
        time.sleep(1)
