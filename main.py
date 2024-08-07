import telebot

bot = telebot.TeleBot("7216699424:AAEyP0m5oY85LGm_WlVzQ74gEdJsPCXwygo")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=["my_skin_type"])
def new_handler(message):
    bot.send_message(message.chat.id,"[Find your skin type](https://skintypesolutions.com/pages/skin-type-quiz)", parse_mode='markdown')

@bot.message_handler(commands=["oily"])
def oily_handler(message):
    bot.send_message(message.chat.id, "Best Cleanser for Oily Skin: CeraVe Foaming Facial Cleanser, $19")



bot.infinity_polling()