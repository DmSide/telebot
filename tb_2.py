import telebot
from telebot import apihelper
from tele_key import MAIN_TOKEN as token

import proxyscrape
#
collector = proxyscrape.create_collector('default', 'https')  # Create a collector for http resources
proxy = collector.get_proxy({'country': 'united states'})  # Retrieve a united states proxy

proxy_2 = {
    proxy.type: f"https://{proxy.host}:{proxy.port}"
}

proxy_1 = {
    'https': 'socks5h://198.50.217.202:1080',
    'http': 'socks5h://198.50.217.202:1080'
}

proxy_3 = {
    'https': 'socks5://telegram.vpn99.net:55655',
    'http': 'socks5://telegram.vpn99.net:55655'
}

# ip = '195.201.137.246'
# port = '1080'
#
# apihelper.proxy = {
#   'https': 'socks5://{}:{}'.format(ip, port)
# }
proxy_4 = {'proxy_url': 'socks4://171.103.9.22:4145/'}

proxy_list = [
    "79.143.180.10:15719"
]

proxy_crt = {"https": f"socks5://{proxy_list[0]}"}

bot = telebot.TeleBot(token)
apihelper.proxy = proxy_crt # {'http': 'http://10.10.1.10:3128'}
# apihelper.proxy = {
#   'http', 'socks5://login:pass@12.11.22.33:8000',
#   'https', 'socks5://login:pass@12.11.22.33:8000'
# }


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# bot.polling
# get_me_msg = bot.get_me()

res = bot.get_updates()
last_upd = res[-1]
mess = last_upd.message
print(mess)
#
# REQUEST_KWARGS={
#     'proxy_url': 'socks4://171.103.9.22:4145/',
#     # Optional, if you need authentication:
#     'urllib3_proxy_kwargs': {
#         'assert_hostname': 'False',
#         'cert_reqs': 'CERT_NONE'
#         # 'username': 'user',
#         # 'password': 'password'
#     }
# }