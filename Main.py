import telebot
import config
import random
from telebot import types
import sercharswer as sa

bot_name = '"Cветящийся дракон"'
bot = telebot.TeleBot(config.TOKEN)
# Действие по команде старт
@bot.message_handler(commands =['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    markup.add(item1, item2)

    username = message.from_user.first_name
    text = f"Привет, {username}! Меня зовут {bot_name} и я бот. \n Выберите действие внизу"
    # reply_markup=markup - добавляет созданную клаиатуру к тексту
    bot.send_message(message.chat.id, text,reply_markup=markup)

# Действие по введенному тексту
@bot.message_handler(content_types =['text'])
def lalala(message):
    username = message.from_user.first_name
    # print(message.text)
    if message.text == '🎲 Рандомное число':
        line_number = str(random.randint(0, 1000))
        bot.send_message(message.chat.id, line_number)
    elif message.text == '😊 Как дела?':
        bot.send_message(message.chat.id, f"У меня все хорошо \nКак у Вас {username}?")
    else:
        if sa.serch(message.text) == 'name':
            bot.send_message(message.chat.id, f"Меня зовут {bot_name}")
        else:
            bot.send_message(message.chat.id, sa.serch(message.text))
bot.polling(none_stop= True)