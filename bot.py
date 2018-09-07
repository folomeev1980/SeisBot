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
    update.message.reply_text(str(update.message))



def echo(bot, update):
    update.message.reply_text(config.help)


def vl(bot, update):
    update.message.reply_text(valut.valuta)



def scf(bot, update):
    update.message.reply_text(scftool.vt)
    update.message.reply_text(scftool.ig)

def smng(bot, update):
    update.message.reply_text(smngtool.ep)
    update.message.reply_text(smngtool.ga)
    update.message.reply_text(smngtool.an)
    update.message.reply_text(smngtool.al)
    update.message.reply_text(smngtool.pr)
    update.message.reply_text(smngtool.sha)
    #update.message.reply_text(smngtool.i5)



def ad(bot,update):
    for i in adultsender.linksAdult:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(update.message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(update.message.chat.id, img, reply_to_message_id=update.message.message_id)
        img.close()
    for i in adultsender.linksAdult2:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(update.message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(update.message.chat.id, img, reply_to_message_id=update.message.message_id)
        img.close()
    for i in adultsender.linksAdult3:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(update.message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(update.message.chat.id, img, reply_to_message_id=update.message.message_id)
        img.close()













updater = Updater(TOKEN)
dispatcher = updater.dispatcher

#    Commands

vl_handler = CommandHandler('vl', vl)
dispatcher.add_handler(vl_handler)

scf_handler = CommandHandler('scf', scf)
dispatcher.add_handler(scf_handler)

smng_handler = CommandHandler('smng', smng)
dispatcher.add_handler(smng_handler)


ad_handler = CommandHandler('ad', ad)
dispatcher.add_handler(ad_handler)

update_handler = CommandHandler('update', update)
dispatcher.add_handler(update_handler)

#    Messages

updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))






# ----------------Webhook-----------------------------

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://seisbot.herokuapp.com/" + TOKEN)
updater.idle()


# ---------------------Webhook_end---------------------
















# if __name__ == '__main__':
#  server.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
#  server = Flask(__name__)
# server.run(host='0.0.0.0', port=port)
