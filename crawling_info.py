import json

with open('/Users/thkim/info.json') as f:
    json_data = json.load(f)


def get_user_id():
    return json_data['user_id']


def get_user_passwd():
    return json_data['user_passwd']


def get_instagram_bot_token():
    return json_data['instagram_bot_token']


def channel():
    return json_data['channel']


def bot():
    return json_data['bot']


# print(get_user_id())
# print(get_user_passwd())
# print(get_instagram_bot_token())
# print(channel())
# print(bot())
