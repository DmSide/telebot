import requests
import telebot
from tele_key import MAIN_TOKEN as token
URL = 'https://api.telegram.org/bot' + token + '/'


proxies = {
    'https': 'socks5://198.50.217.202:1080'
}

TG_PROXY = {
    'http': 'https://103.241.156.250:8080'
}

bot = telebot.TeleBot(token)


def get_updates():
    url = URL + 'get_updates'
    r = requests.get(url, proxies=TG_PROXY)
    return r.json


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


if __name__ == '__main__':
    get_updates()



