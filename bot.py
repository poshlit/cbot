import telebot
import tokkk

bot = telebot.TeleBot(tokkk.token)
@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, "Привет.")
    
@bot.message_handler(content_types=['text'])
def send_msg(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'здарова':
        bot.send_message(message.chat.id, 'Здарова, бармалей')
    elif message.text.lower() == 'пока' or message.text.lower() == "прощай":
        bot.send_message(message.chat.id, "Пока, дружище")
    else:
        bot.send_message(message.chat.id, "непон")
bot.polling()
