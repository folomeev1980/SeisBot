import telebot
import scftool
import smngtool
import config



bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, config.help)
@bot.message_handler(commands=['scf'])
def handle_scf(message):
   bot.send_message(message.chat.id, scftool.vt)
   bot.send_message(message.chat.id, scftool.ig)
@bot.message_handler(commands=['vt'])
def handle_vt(message):
   bot.send_message(message.chat.id, scftool.vt)
@bot.message_handler(commands=['ig'])
def handle_ig(message):
   bot.send_message(message.chat.id, scftool.ig)
@bot.message_handler(commands=['smng'])
def handle_smng(message):
   bot.send_message(message.chat.id, smngtool.ep)
   bot.send_message(message.chat.id, smngtool.ga)
   bot.send_message(message.chat.id, smngtool.an)
   bot.send_message(message.chat.id, smngtool.al)
   bot.send_message(message.chat.id, smngtool.pr)
   bot.send_message(message.chat.id, smngtool.sha)
   bot.send_message(message.chat.id, smngtool.i5)

@bot.message_handler(commands=['adult'])
def handle_adult(message):
    # sendPhoto
    photo ='http://img-f.photosight.ru/395/6788021_thumb.jpg'
    bot.send_photo(message.chat_id, photo)





@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, config.help)





if __name__ == '__main__':
     bot.polling(none_stop=True)
