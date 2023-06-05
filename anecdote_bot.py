import telebot
import requests


TELEGRAM_API_TOKEN = ''


bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Send a welcome message to the user when they first start or help command is used.
    """
    bot.reply_to(message, "Hi! You can ask me to send you an anecdote by typing /anecdote.")

@bot.message_handler(commands=['anecdote'])
def get_anecdote(message):
    """
    Send a random anecdote to the user.
    """

    response = requests.get("https://api.chucknorris.io/jokes/random")


    bot.reply_to(message, response.json()['value'])


bot.polling()
