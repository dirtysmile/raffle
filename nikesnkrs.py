from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime as dt


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

        if(tmp_t != '' and tmp_t != 'Coming Soon' and tmp_t != 'Sold Out'):
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

        if(tmp_t != '' and tmp_t != 'Coming Soon' and tmp_t != 'Sold Out'):
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
    send_link = []

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
            send_link.append(now_links[n])
            pre_links.append(now_links[n])

        send_massage(send_link)

        now_links = []


def send_massage(link):
    coming_soon = []
    draw = []
    send_stirng = 'SNKRS가 업데이트 되었습니다.\n'

    for t in link:
        if t['time'].find('출시') > 0:
            coming_soon.append(t)
        else:
            draw.append(t)

    if len(draw) > 0:
        send_stirng += '<b>[ 응모 예정 ]</b>\n'
        for d in draw:
            send_stirng += d['title']+'\n'

    if len(coming_soon) > 0:
        send_stirng += '\n<b>[ 출시 예정 ]</b>\n'
        for c in coming_soon:
            send_stirng += c['title']+'\n'

    send_stirng += "\n<b>[ URL ]</b>\nhttps://www.nike.com/kr/launch/?type=upcoming"
    send_telegram.send_telgm_string(
        send_stirng, crawling_info.nikesnkrs_channel())


def run():
    if(not init_flg):
        init_link()
    else:
        check_link()


def comming():

    date = dt.datetime.now()

    day = date.day+1
    month = date.month

    day_month = str(month)+'월 '+str(day)+'일'

    tomorrow_filter = []
    draw = []
    coming_soon = []
    send_string = ''

    for l in pre_links:
        if l['day'].split(' ')[0] == str(month)+'월' and l['day'].split(' ')[1] == str(day):
            tomorrow_filter.append(l)

    for t in tomorrow_filter:
        if t['time'].find('출시') > 0:
            coming_soon.append(t)
        else:
            draw.append(t)

    if len(draw) > 0:
        send_string = '<b>[ 응모 예정 ]</b>\n'
        for d in draw:
            send_string += d['title']+'\n'

    if len(coming_soon) > 0:
        send_string += '\n<b>[ 출시 예정 ]</b>\n'
        for c in coming_soon:
            send_string += c['title']+'\n'

    if send_string != '':
        pre_string = day_month + ' 오전 10시 일정입니다.\n\n' + send_string
        send_string = pre_string
        send_string += ' \n < b > [URL] < /b >\nhttps: // www.nike.com/kr/launch /?type = upcoming'
        send_telegram.send_telgm_string(
            send_string, crawling_info.nikesnkrs_channel())
