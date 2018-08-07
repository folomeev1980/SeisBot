import telebot

#main variables
TOKEN = '513308297:AAFxvSsa6hDNk238pON8i3j-nOGSlmygitU'



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)

#test
#test2