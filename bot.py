import telebot
import scftool
import smngtool
import config
import urllib
import valut
import adultsender

import os
from telegram.ext import Updater, MessageHandler, Filters



TOKEN = os.environ.get('TOKEN', config.TOKEN)
PORT = int(os.environ.get('PORT', '5000'))





def echo(bot, update):
    update.message.reply_text('Bot answer: ' + update.message.text)


updater = Updater(TOKEN)

# add handlers
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))



updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://seisbot.herokuapp.com/" + TOKEN)
updater.idle()


#if __name__ == '__main__':
  #  server.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
  #  server = Flask(__name__)
#server.run(host='0.0.0.0', port=port)
