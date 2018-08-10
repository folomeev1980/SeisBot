import config



#  -----------Переменные---------------------------------------------
#
days = 1  # Колличество дней назад

links = config.adult_input(True, days)  # Выбираем значение Adult: True или False
linksAdult = config.only_adult(days)

#   -------------Тело программы---------------------------------------
'''
if len(linksAdult) > 1:
    try:
        pic_download(links, linksAdult, picDist, rotation)
    except:
        print("Скачивание и запись файлов прошла с ошибками")
       

else:
    print("")
'''


