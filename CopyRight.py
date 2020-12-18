#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot 
# import datetime
# import signal
# import subprocess
# import re
# import calendar
# import time
# import json

# import modules.beautifier as beautifier
# import modules.crawler as crawler

f_token = open("token.txt")
token = f_token.read()
f_token.close()

path_to_dir = "./"

bot = telebot.TeleBot(token)

markup_yes_no = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = telebot.types.KeyboardButton('Да')
itembtn2 = telebot.types.KeyboardButton('Нет')
markup_yes_no.add(itembtn1, itembtn2)

markup_remove = telebot.types.ReplyKeyboardRemove(selective=False)

markup_getout = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = telebot.types.KeyboardButton('Прервать диалог')
markup_getout.add(itembtn1)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Здравствуйте ! Я умею выводить эту справку и искать \
        первоисточник новостного сообщения. Нажмите на "/" и выберите "search" для поиска первоисточника')

@bot.message_handler(commands=['search'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Пожалуйста, введите текст, первоисточник которого вы хотите найти')
    bot.register_next_step_handler(message, start_search)

def start_search(message):
    # beautifier.run(message.text)
    # result_url = crawler.run(message.text)
    result_url = "test_url"
    bot.send_message(message.chat.id, 'Вероятный первоисточник сообщения находится по ссылке: {}'.format(result_url))

@bot.message_handler(content_types=["text"])
def any_text(message): 
    bot.send_message(message.chat.id, 'Я вас не понимаю, пожалуйста, введите "/help" для получения справки', reply_markup=markup_remove)

if __name__ == '__main__':
    bot.polling(none_stop=True)