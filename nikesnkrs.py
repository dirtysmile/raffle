from selenium import webdriver
from selenium.webdriver.common.by import By
import time


import open_chrome
import send_telegram
import crawling_info
import simple_logger


logger = simple_logger.set_logger('snkrsLog', 'test.log')
pre_links = []
now_links = []
init_flg = False
url = "https://www.nike.com/kr/launch/?type=upcoming"


def init_link():
    global init_flg
    global pre_links
    logger.info('start init link')

    driver = open_chrome.connect()
    driver.get(url)

    titleAndTime = driver.find_elements(By.CLASS_NAME, "figcaption-content")
    linkAndDay = driver.find_elements(By.CLASS_NAME, "card-link")

    for i in range(len(titleAndTime)):
        tmp_t = titleAndTime[i].text
        tmp_l = linkAndDay[i].text

        if(tmp_t != '' and tmp_t != 'Coming Soon'):
            pre_links.append(
                {'title': tmp_t.split('\n')[1],
                 'url': linkAndDay[i].get_attribute("href"),
                 'time': tmp_t.split('\n')[0],
                 'day': tmp_l.replace('\n', ' ')
                 }
            )

    # del pre_links[0]
    # del pre_links[0]

    init_flg = True
    driver.close()


def check_link():
    logger.info('check link')
    global now_links

    driver = open_chrome.connect()
    driver.get(url)

    titleAndTime = driver.find_elements(By.CLASS_NAME, "figcaption-content")
    linkAndDay = driver.find_elements(By.CLASS_NAME, "card-link")

    for i in range(len(titleAndTime)):
        tmp_t = titleAndTime[i].text
        tmp_l = linkAndDay[i].text

        if(tmp_t != '' and tmp_t != 'Coming Soon'):
            now_links.append(
                {'title': tmp_t.split('\n')[1],
                 'url': linkAndDay[i].get_attribute("href"),
                 'time': tmp_t.split('\n')[0],
                 'day': tmp_l.replace('\n', ' ')
                 }
            )

    compare_link()
    driver.close()


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

#     new가 나왔지?
    new_index = []

    for n_link in new:
        new_index.append(new_link.index(n_link))

    if(len(new_index) > 0):
        for n in new_index:
            pre_links.append(now_links[n])
        send_telegram.send_telgm_for_nike(crawling_info.nikesnkrs_channel())

        now_links = []


def run():
    if(not init_flg):
        init_link()
    else:
        check_link()


def release_notice():
    print('a')
