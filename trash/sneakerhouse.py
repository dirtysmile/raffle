from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

import send_telegram
import simple_logger
import crawling_info
import time_utils

logger = simple_logger.set_logger('sneakLog', 'test.log')
pre_links = []
now_links = []
init_flg = False


def init_link(driver):
    global init_flg

    logger.info('init_link')

    url = "https://m.cafe.naver.com/ca-fe/web/cafes/29779167/menus/2"
    driver.get(url)
    time.sleep(5)

    links = driver.find_elements(By.CLASS_NAME, "txt_area")
    titles = driver.find_elements(By.CLASS_NAME, "tit")

    for i in reversed(range(len(titles))):
        if(titles[i].text == '댓글'):
            del titles[i]

    del titles[0]
    del titles[0]

    for i in range(len(links)):
        pre_links.append(
            {"title": titles[i].text, "url": links[i].get_attribute("href")})

    # del pre_links[0]
    # del pre_links[0]

    init_flg = True


def check_link(driver):
    logger.info('check link')

    url = "https://m.cafe.naver.com/ca-fe/web/cafes/29779167/menus/2"
    driver.get(url)
    time.sleep(5)

    links = driver.find_elements(By.CLASS_NAME, "txt_area")
    titles = driver.find_elements(By.CLASS_NAME, "tit")

    for i in reversed(range(len(titles))):
        if(titles[i].text == '댓글'):
            del titles[i]

    del titles[0]
    del titles[0]

    for i in range(len(links)):
        now_links.append(
            {"title": titles[i].text, "url": links[i].get_attribute("href")})

    compare_link()


def compare_link():
    logger.info("compare link")
    old_link = []
    new_link = []
    new = []
    find = []

    global pre_links
    global now_links

    for link in pre_links:
        old_link.append(link['url'])

    for link in now_links:
        new_link.append(link['url'])

    new = list(set(new_link)-set(old_link))
    logger.info(new)

    for i in range(len(new)):
        find.append(now_links[i])

    for f in find:
        pre_links.append(f)

    now_links = []

    if(len(find) > 0):
        send_telegram.send_telgm(find, crawling_info.sneakerhouse_channel())


def run(driver):
    if(not init_flg):
        init_link(driver)
    else:
        check_link(driver)
