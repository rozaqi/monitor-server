import telebot
import subprocess
import json
from telebot import types

# config vars
with open('config.json') as f:
    token = json.load(f)

bot = telebot.TeleBot(token['telegramToken'])



@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo, apa kabarmu?')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='/start'))
    markup.add(types.InlineKeyboardButton(text='/help'))


@bot.message_handler(regexp='alhamdulillah')
def text(message):
    # membalas pesan
    bot.reply_to(message, 'senang mendengarnya')

@bot.message_handler(commands=['help'])
def help(message):
    # membalas pesan
    bot.reply_to(message, 
    '''
    Daftar Perintah Monitoring
    1. ls 
    2. pwd
    3. free
    4. uptime
    5. koneksi
    6. last
    7. whoami
    ''')

@bot.message_handler(regexp='rozaqi')
def text(message):
    # membalas pesan
    bot.reply_to(message, 'halo apa kabar abdul')

@bot.message_handler(regexp='ls')
def text(message):
    ls = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8') 
    # membalas pesan
    bot.reply_to(message, ls)

@bot.message_handler(regexp='free')
def text(message):
    free = subprocess.run(['free'], stdout=subprocess.PIPE).stdout.decode('utf-8') 
    # membalas pesan
    bot.reply_to(message, free)

@bot.message_handler(regexp='pwd')
def text(message):
    pwd = subprocess.run(['pwd'], stdout=subprocess.PIPE).stdout.decode('utf-8') 
    # membalas pesan
    bot.reply_to(message, pwd)

@bot.message_handler(regexp='uptime')
def text(message):
    uptime = subprocess.run(['uptime'], stdout=subprocess.PIPE).stdout.decode('utf-8') 
    # membalas pesan
    bot.reply_to(message, uptime)

@bot.message_handler(regexp='koneksi')
def text(message):
    koneksi = subprocess.run(["ping", "-c", "4", "8.8.8.8"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # membalas pesan
    bot.reply_to(message, koneksi)

@bot.message_handler(regexp='last')
def text(message):
    last = subprocess.run(["last"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # membalas pesan
    bot.reply_to(message, last)

@bot.message_handler(regexp='whoami')
def text(message):
    whoami = subprocess.run(["whoami"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # membalas pesan
    bot.reply_to(message, whoami)


print('Bot Telegram sedang running')
bot.polling()
