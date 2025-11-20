import telebot

Token = "8254976645:AAEgEObzFKmsH9z_OoU_Ri7IWnBEO-z_Ns8"

ID = 6855428262
bot = telebot.TeleBot(Token)


@bot.message_handler(func=lambda message: True)
def nimadir(message):
    b = message.from_user
    name = (b.first_name or "Yo'q") + (" " + b.last_name if b.last_name else "")
    username = "@"+b.username if b.username else "(Yo'q)"
    text= message.text or "Yo'q"
    bot.send_message(ID, f"Yangi xabar:\nIsm: {name}\nUsername: {username}\nID: {b.id}\nMatn: {text}")

print("Dastur ishladi")
bot.polling()





