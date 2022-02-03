import datetime as dt
import schedule
import time
import simple_logger

logger = simple_logger.set_logger('timeUtils', 'test.log')
sleep_hour = [21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8]


def sleep():
    sleep_flg = False
    x = dt.datetime.now()
    if x.hour in sleep_hour:
        sleep_flg = True
        logger.info('sleep...10 minutes')
        time.sleep(600)
    return sleep_flg
