import telebot
from decouple import config
from weather import getCurrentWeather

BOT_TOKEN = "6067594989:AAHgfY4SSYQ9kuDYloRs9pCI5PUys3LBxFA"
greeting = ["hello", "hi", "welcome", "اهلاً"]
whoAreYou = ["who", 'what']
weather = ["weather", "الطقس"]
botName = "food_order"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help!"])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome to food order bot please chose the category")


# answering every message not just commands
def isMsg(message):
    return True


@bot.message_handler(func=isMsg)
def reply(message):
    words = message.text.split()

    if words[0].lower() in weather:
        report = getCurrentWeather()
        return bot.reply_to(message.chat.id, report or "failed to get weather !!")
    if words[0].lower() in greeting:
        return bot.reply_to(message, "hey how is it going")
    else:
        return bot.reply_to(message, "That is not command of mine")


bot.polling()
