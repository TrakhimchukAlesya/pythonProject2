import sqlite3
import telebot
from telebot import types

token = '5414267140:AAFBz-5aqaqriqfpgRKddi-ZSDq0UMHjA0s'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name==None:
        message.from_user.last_name=''
    elif message.from_user.first_name==None:
        message.from_user.last_name=''
    elif message.from_user.first_name==None and message.from_user.last_name==None:
        message.from_user.first_name=message.from_user.username
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    exellent=types.KeyboardButton('Отличное!!!')
    good=types.KeyboardButton('Хорошее:)')
    not_good=types.KeyboardButton('Не очень..')
    very_bad=types.KeyboardButton('Очень плохое:(')
    keyboard.add(exellent, good, not_good, very_bad)
    greetings = f'Привет, {message.from_user.first_name} {message.from_user.last_name}, как твоё настроение?'
    bot.send_message(message.chat.id, greetings, reply_markup=keyboard)

@bot.message_handler()
def user_enter(message):
    if message.text=='Отличное!!!':
        smiley=b'\xF0\x9F\x98\x81'.decode()
        bot.send_message(message.chat.id, f"Как хорошо, вот вам смайлики {smiley} {smiley} {smiley}")
    elif message.text=='Хорошее:)':
        smiley=b'\xF0\x9F\x98\x8A'.decode()
        bot.send_message(message.chat.id, f"Можно и лучше, вот вам смайлики {smiley} {smiley} {smiley}, для улучшения!!!")
    elif message.text=='Не очень..':
        smiley=b'\xF0\x9F\x98\x98'.decode()
        bot.send_message(message.chat.id, f"Расслабься, такое бывает, и помни, бот тебя любит {smiley} {smiley} {smiley}")
    elif message.text=='Очень плохое:(':
        smiley=b'\xF0\x9F\x98\xA4'.decode()
        smiley_1 = b'\xE2\x98\x95'.decode()
        smiley_2 = b'\xF0\x9F\x9B\x80'.decode()
        bot.send_message(message.chat.id, f"Выпусти пар {smiley}, завари  {smiley_1} и прими ванну {smiley_2}")
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю, нажмите /start')

if __name__ == "__main__":
    bot.polling(none_stop=True)