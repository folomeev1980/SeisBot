import scftool
import smngtool
import config
import logging
import urllib
import valut
import adultsender
import telegram
import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.environ.get('TOKEN', config.TOKEN)
PORT = int(os.environ.get('PORT', '5000'))

def update(bot,update):
    update.message.reply_text(update.message.chat)
def vl(bot, update):
    update.message.reply_text(valut.valuta)

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

#    Commands



print()

