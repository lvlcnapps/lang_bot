from telebot import TeleBot
from telebot import formatting
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import word
import sentence
import json
import types
import translator
import os

os.system('yc iam create-token > C:"\\"Users\Admin\PycharmProjects"\\"tgbot"\\"venv"\\"token.txt')

bot = TeleBot()

class MyBot():
    def __init__(self):
        print("Started")



    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')

    @bot.message_handler(commands=['new_token'])
    def new_token(message):
        os.system('yc iam create-token > C:"\\"Users\Admin\PycharmProjects"\\"tgbot"\\"venv"\\"token.txt')
        bot.send_message(message.chat.id, 'Новый токен выдан, попробуй /generate')

    @bot.message_handler(commands=['generate'])
    def gen(message):
        sen = sentence.Sentence()

        markup = ReplyKeyboardMarkup(row_width=10)
        markup.row_width = 1
        markup.resize_keyboard = True
        # markup.add(InlineKeyboardMarkup(InlineKeyboardButton("Generate", callback_data="cb_gen")))
        markup.add(KeyboardButton("/generate"))

        cr = sen.createNormalSentence()
        tr = translator.Translator()
        try:
            bot.send_message(message.chat.id, f'{cr}', reply_markup=markup)
            lo = tr.translate(cr)
            if lo[-1] == '.':
                lo = lo[:-1]
            bot.send_message(message.chat.id, formatting.mspoiler(lo), parse_mode='MarkdownV2')
        except BaseException:
            bot.send_message(message.chat.id, "Ошибка")

    # @bot.message_handler()
    # def getUserText(message):
    #     bot.send_message(message.chat.id, "я еду\n" + formatting.mspoiler("אני נוסע"), parse_mode='MarkdownV2')


objBot = MyBot()

timer = 100
check = 0
while True:
    if timer == 1 or check == 0:
        try:
            bot.polling(none_stop=True, skip_pending=True)
        except BaseException:
            check = 1
    timer -= 1
    if timer <= 1:
        timer = 100
        check = 0