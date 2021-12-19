from selenium import webdriver
import time
import schedule
import sys
import logging

import open_chrome
import trash.instagram as instagram
import eomisae
import simple_logger
import trash.sneakerhouse as sneakerhouse
import nikesnkrs
import send_telegram
import hjreps


def handle_exception(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger('ErrorLogger')

    logger.error("Unexpected exception", exc_info=(
        exc_type, exc_value, exc_traceback))
    send_telegram.send_error('프로그램이 종료되었습니다.')


if __name__ == '__main__':
    send_telegram.send_error('프로그램이 시작되었습니다.')
    simple_logger.set_logger('ErrorLogger', 'error.log')
    simple_logger.set_logger('MyLogger', 'test.log')
    sys.excepthook = handle_exception

    driver = open_chrome.connect()

    schedule.clear()
    # [어미새] 2분
    schedule.every(2).minutes.do(eomisae.run)

    # [나이키 SNKRS] 12시 18시 19시
    schedule.every().day.at("12:00:00").do(nikesnkrs.run)
    schedule.every().day.at("18:00:00").do(nikesnkrs.run)
    schedule.every().day.at("19:00:00").do(nikesnkrs.comming)

    # 호랩 출첵
    schedule.every().day.at("00:10:00").do(hjreps.run)

    # [스니커 하우스] 10시 14시 17시 20시
    # schedule.every().day.at("10:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("12:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("14:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("16:00:00").do(sneakerhouse.run, driver)
    # schedule.every().day.at("18:00:00").do(sneakerhouse.run, driver)

    # schedule.every(2).minutes.do(sneakerhouse.run, driver)
    # schedule.every(10).seconds.do(nikesnkrs.run)
    # schedule.every(10).seconds.do(nikesnkrs.comming)

    eomisae.run()
    nikesnkrs.run()
    hjreps.run()
    # sneakerhouse.run(driver)

    while True:
        schedule.run_pending()
        time.sleep(1)
