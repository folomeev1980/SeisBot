import telebot
import scftool

#main variables
TOKEN = '513308297:AAFxvSsa6hDNk238pON8i3j-nOGSlmygitU'



bot = telebot.TeleBot(TOKEN)






















@bot.message_handler(commands=['scf'])

def handle_geom(message):
    bot.send_message(message.chat.id, scftool.vessel_info("VYACHESLAV TIKHONOV",scftool.tikhonov_text))
    bot.send_message(message.chat.id, scftool.vessel_info("IVAN GUBKIN", scftool.gubkin_text))


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "Привет Это новый бот")

# Обработчик команд '/start' и '/help'.



if __name__ == '__main__':
     bot.polling(none_stop=True)
