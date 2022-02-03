import requests
from bs4 import BeautifulSoup
import schedule
import time
import numpy as np
import datetime
import logging

import send_telegram
import simple_logger
import crawling_info
import time_utils

# logger = simple_logger.set_logger('eomisaeLog', 'test.log')
logger = logging.getLogger('MyLogger')
eomisae_home = 'https://eomisae.co.kr/dr'
pre_links = []
now_links = []
init_flg = False


def init_link():
    global init_flg
    try:
        # logger.info("start init link")
        res = requests.get(eomisae_home)
        soup = BeautifulSoup(res.content.decode(
            'utf-8', 'replace'), 'html.parser')
        links = soup.select('h3 .pjax')

        for link in links:
            pre_links.append({'title': link.text, 'url': link['href']})

        print(pre_links)

        init_flg = True
        return pre_links
    except:
        print("접속 오류")
        # logger.error("접속 오류")
        # del pre_links[0]
        # del pre_links[0]


def compare_link():
    # logger.info("compare link")
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

    for i in range(len(new)):
        find.append(now_links[i])

    for f in find:
        pre_links.append(f)

    now_links = []

    if(len(find) > 0):
        send_telegram.send_telgm(find, crawling_info.eomisae_channel())


def check_link():
    # logger.info("check link")
    if(time_utils.sleep()):
        return
    try:
        res = requests.get(eomisae_home)
        soup = BeautifulSoup(res.content.decode(
            'utf-8', 'replace'), 'html.parser')
        links = soup.select('h3 .pjax')

        for link in links:
            now_links.append({'title': link.text, 'url': link['href']})

        compare_link()
    except:
        logger.error("접속 에러")


def run():
    if not init_flg:
        init_link()
    else:
        check_link()


if __name__ == "__main__":
    run()

# schedule.clear()
# schedule.every(3).seconds.do(run)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
#     print('.')
