import telegram
import crawling_info


def send_error(value):
    bot = telegram.Bot(crawling_info.get_instagram_bot_token())
    bot.telegram(chat_id=crawling_info.bot(), text=value)


def send_telgm(recent):
    send_text = ''

    for re in recent:
        send_text += '<b>[ ' + re['title'] + ' ]</b>\n' + re['url'] + '\n\n'

    print(send_text)

    telgm_token = crawling_info.get_instagram_bot_token()
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id=crawling_info.channel(), text=send_text,
                    parse_mode='HTML', disable_web_page_preview=True)

    recent.clear()
