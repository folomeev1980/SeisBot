import config



#  -----------Переменные---------------------------------------------
#
days = 5  # Колличество дней назад

links = config.adult_input(True, days)  # Выбираем значение Adult: True или False
linksAdult = config.only_adult(days)


days2 = 4  # Колличество дней назад

links2 = config.adult_input(True, days2)  # Выбираем значение Adult: True или False
linksAdult2 = config.only_adult(days2)

days3 = 3  # Колличество дней назад

links3 = config.adult_input(True, days3)  # Выбираем значение Adult: True или False
linksAdult3 = config.only_adult(days3)

days4 = 2  # Колличество дней назад

links4 = config.adult_input(True, days4)  # Выбираем значение Adult: True или False
linksAdult4 = config.only_adult(days4)

days5 = 1  # Колличество дней назад

links5 = config.adult_input(True, days5)  # Выбираем значение Adult: True или False
linksAdult5 = config.only_adult(days5)














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


