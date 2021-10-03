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

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Halo')
    
bot.polling(none_stop=True, interval=2, timeout=90)
