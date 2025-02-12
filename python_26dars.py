# 12.02.2025
# vohidov
# kiril lotiun telegram bot

from transliterate import to_cyrillic , to_latin
import telebot 


TOKEN = '8041947638:AAFStPB_5wPsEqB7yXdQQpGphQ3jxc1cR8Q'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = (lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg))(msg)
    bot.reply_to(message, javob)

bot.polling()

# matn = input("Matn kiriting:")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))


