import telebot
import configparser
import json
from telebot import apihelper
import datetime
import re
import calendar
now = datetime.datetime.now()
Token1="948381879:AAEO07_DU1z-CO67NRWIi8HX_jeLNfQVqPo" #Totochka
bot = telebot.TeleBot(Token1)
#@bot.message_handler(commands=['start'])

ye=int(now.year)
print(ye)
chas=int(now.hour)
min=int( now.minute)
print('chas=',chas)
print('min=',min)
mes=int(now.month)
chis=int(now.day)

nomden=calendar.weekday(ye,mes,chis)
kalen={}
kalen={0:"mondey",
         1:"tuesday",
         2:"wednesday",
         3:"thursday",
         4:"friday"}
den=kalen.get(nomden)
print(den)
