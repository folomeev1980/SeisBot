import telebot
import scftool
import smngtool
import config
#main variables


bot = telebot.TeleBot(config.TOKEN)




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




@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):# Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "Привет Это SeisBot, здесь ты можешь узнать:\n"
                                      "\n"
                                      "/scf - местоположение судов Компании SCF;\n"
                                      "/vt  - местоположение Vyacheslav Tikhonov;\n"
                                      "/ig  - местоположение Ivan Gubkin;\n"
                                      "/smng- местоположение судов Компании SMNG;\n")

# Обработчик команд '/start' и '/help'.



if __name__ == '__main__':
     bot.polling(none_stop=True)
