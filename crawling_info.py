import json

with open('/Users/thkim/info.json') as f:
    json_data = json.load(f)


def get_user_id():
    return json_data['user_id']


def get_user_passwd():
    return json_data['user_passwd']


def get_instagram_bot_token():
    return json_data['instagram_bot_token']


def get_hjreps_id():
    return json_data['hjreps_id']


def eomisae_channel():
    return json_data['eomisae_channel']


def sneakerhouse_channel():
    return json_data['sneakerhouse_channel']


def nikesnkrs_channel():
    return json_data['nikesnkrs_channel']


def bot():
    return json_data['bot']


# print(get_user_id())
# print(get_user_passwd())
# print(get_instagram_bot_token())
# print(channel())
# print(bot())
