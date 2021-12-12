from selenium import webdriver
import time


def connect():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    chromedriver = '/usr/local/Cellar/chromedriver/chromedriver'
    driver = webdriver.Chrome(chromedriver)

    time.sleep(10)
    return driver
