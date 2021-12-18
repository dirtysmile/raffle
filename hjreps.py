from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import crawling_info
import simple_logger
import open_chrome


logger = simple_logger.set_logger('hjrepsLog', 'test.log')


def run():
    logger.info('run attendance check')
    url = "https://www.hjreps.com/"
    driver = open_chrome.connect()
    driver.get(url)

    driver.find_element_by_name('mb_id').send_keys(
        crawling_info.get_hjreps_id())
    driver.find_element_by_name('mb_password').send_keys(
        crawling_info.get_user_passwd())

    driver.find_element_by_xpath(
        '//*[@id="miso_sidelogin"]/div/div[1]/button').submit()
    driver.find_element_by_xpath(
        '//*[@id="thema_wrapper"]/div/aside[1]/section/div[1]/div[3]/a[3]').click()

    time.sleep(60)

    driver.find_element_by_xpath('//*[@id="talk_submit"]').click()
    time.sleep(60)
    driver.quit()
