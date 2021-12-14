import telegram
import crawling_info
import datetime


def send_error(value):
    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=crawling_info.bot(), text='장애 발생',
                    parse_mode='HTML', disable_web_page_preview=True)


def send_telgm(recent, channel):
    send_text = ''
    now = datetime.datetime.now()

    for re in recent:
        send_text += '<b>[ ' + re['title'] + ' ]</b>\n' + re['url'] + '\n\n'

    print("[" + str(now) + "] send_telgm > " + send_text)

    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=channel, text=send_text,
                    parse_mode='HTML', disable_web_page_preview=True)

    recent.clear()
