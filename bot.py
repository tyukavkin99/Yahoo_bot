import telebot
import yfinance as yf
import pandas as pd
import password

key = 'YOUR KEY'

bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Please enter the share number')
    
def get_share(s):
    try:
        s = ''
        share_data = yf.Ticker(s)
        return share_data
    except Exception as e:
        return print('Wrong number')   

    

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'You got' + get_share(str(message.text)))
    
    
    
bot.polling(non_stop = True, interval=0)