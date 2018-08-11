import telebot
import scftool
import smngtool
import config
import urllib
import adultsender



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

@bot.message_handler(commands=['adult','ad'])
def send_adult(message):
    for i in adultsender.linksAdult:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

@bot.message_handler(commands=['adult2','ad2'])
def send_adult2(message):
    for i in adultsender.linksAdult2:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

@bot.message_handler(commands=['adult3','ad3'])
def send_adult3(message):
    for i in adultsender.linksAdult3:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

@bot.message_handler(commands=['adult4','ad4'])
def send_adult4(message):
    for i in adultsender.linksAdult4:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

@bot.message_handler(commands=['adult5', 'ad5'])
def send_adult5(message):
    for i in adultsender.linksAdult5:
        url = i
        f = open('out.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, config.help)






if __name__ == '__main__':
     bot.polling(none_stop=True, interval=3)
