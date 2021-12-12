from selenium import webdriver
import time
import schedule

import open_chrome
import instagram


driver = open_chrome.connect()
driver = instagram.login(driver)

schedule.clear()
schedule.every().hour.at(":01").do(instagram.run_01, driver, instagram.instar_nike_pages,
                                   instagram.recent_histories, instagram.previous_histories)
schedule.every().hour.at(":31").do(instagram.run_31, driver, instagram.instar_nike_pages,
                                   instagram.recent_histories, instagram.previous_histories)
# schedule.every(10).minutes.do(instagram.run_01, driver, instagram.instar_nike_pages,
#   instagram.recent_histories, instagram.previous_histories)

while True:
    schedule.run_pending()
    time.sleep(1)
