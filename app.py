import random
import telebot
import requests
import time
import json
from telebot import types
import taucoin
import logging

bot_token = ''
bot = telebot.TeleBot(token=bot_token, num_threads=8)

# 111
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Halo')


@bot.message_handler(commands=['track'])
def start(message):
    r = requests.get("https://covid19.mathdro.id/api/countries")
    loads = json.loads(r)
    
@bot.message_handler(commands=['about_us'])
def start(message):
    messages_text = """
This bot created to help people to track covid-19 in their countries,
We hope this bot could help people to stay safe and healthy.

We're making more feature as soon as possible.





    
    """
    bot.send_message(message.chat.id,"")

bot.polling(none_stop=True, interval=2, timeout=90)
