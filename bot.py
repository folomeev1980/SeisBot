import telebot
import scftool

#main variables
TOKEN = '513308297:AAFxvSsa6hDNk238pON8i3j-nOGSlmygitU'



bot = telebot.TeleBot(TOKEN)





















vt=' '.join(scftool.vessel_info("VYACHESLAV TIKHONOV",scftool.tikhonov_text))
ig=' '.join(scftool.vessel_info("IVAN GUBKIN",scftool.gubkin_text))
@bot.message_handler(commands=['scf'])
def handle_scf(message):
   bot.send_message(message.chat.id, vt)
   bot.send_message(message.chat.id, ig)
@bot.message_handler(commands=['vt'])
def handle_vt(message):
   bot.send_message(message.chat.id, vt)
@bot.message_handler(commands=['ig'])
def handle_ig(message):
   bot.send_message(message.chat.id, ig)




@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):# Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "Привет Это SeisBot, здесь ты можешь узнать:"
                                      "/scf - местоположение судов Компании SCF; "
                                      "/vt  - местоположение Vyacheslav Tikhonov; "
                                      "/ig  - местоположение Ivan Gubkin; ")

# Обработчик команд '/start' и '/help'.



if __name__ == '__main__':
     bot.polling(none_stop=True)
