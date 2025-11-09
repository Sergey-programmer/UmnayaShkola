from telebot import TeleBot

bot = TeleBot("8214900835:AAFUHZMvLIbf-6rTlP1q2YirhQCJBK216nQ")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Всё работает!")

bot.polling(non_stop=True)
