import telegram
import crawling_info
import datetime
import simple_logger

logger = simple_logger.set_logger('telegramLog', 'test.log')


def send_error(value):
    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=crawling_info.bot(), text=value,
                    parse_mode='HTML', disable_web_page_preview=True)


def send_telgm(recent, channel):
    send_text = ''
    now = datetime.datetime.now()

    for re in recent:
        send_text += '<b>[ ' + re['title'] + ' ]</b>\n' + re['url'] + '\n\n'

    logger.info(send_text)

    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=channel, text=send_text,
                    parse_mode='HTML', disable_web_page_preview=True)

    recent.clear()


def send_telgm_string(value, channel):
    logger.info(value)

    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=channel, text=value,
                    parse_mode='HTML', disable_web_page_preview=True)


def send_telgm_for_nike(channel):
    send_text = '<b>[ SNKRS가 업데이트 되었습니다 ]</b>\n' + \
        'https://www.nike.com/kr/launch/?type=upcoming'

    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=channel, text=send_text,
                    parse_mode='HTML', disable_web_page_preview=True)
