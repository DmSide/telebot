import telebot
from telebot import apihelper
from tele_key import token2
apihelper.proxy = {'http': 'http://10.10.1.10:3128'}
bot = telebot.TeleBot(token2)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()