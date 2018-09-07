import telebot
import scftool
import smngtool
import config
import logging
import urllib
import valut
import adultsender

import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


TOKEN = os.environ.get('TOKEN', config.TOKEN)
PORT = int(os.environ.get('PORT', '5000'))





def echo(bot, update):
    update.message.reply_text(config.help)

def vl(bot,update):
    update.message.reply_text(valut.valuta)






updater = Updater(TOKEN)
dispatcher = updater.dispatcher



vl_handler = CommandHandler('vl', vl)
dispatcher.add_handler(vl_handler)




# add handlers
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))






#----------------

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://seisbot.herokuapp.com/" + TOKEN)
updater.idle()
#---------------------

#if __name__ == '__main__':
  #  server.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
  #  server = Flask(__name__)
#server.run(host='0.0.0.0', port=port)
