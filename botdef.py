def geometry(sourse_int=50, reciver_int=12.5, num_of_chan=480, offset=135, cable_depth=7, gun_depth=6):
    cdpint = reciver_int / 2
    fold = ((reciver_int * num_of_chan) / (2 * sourse_int))
    binint = (reciver_int * num_of_chan) / fold
    headerstatic = ((cable_depth + gun_depth) / 1.5)
    maxofset = offset + reciver_int * (num_of_chan - 1)
    minbinoffset = offset + ((((sourse_int - cdpint) / cdpint) * reciver_int) / 2)
    maxbinoffset = minbinoffset + binint * (fold - 1)

    print("Кратность равна        :    ", fold)
    print("статическая поправка   :    ", int(headerstatic))
    print("Интервал между ОГТ:    :    ", cdpint)
    print("BIN интервал:          :    ", binint)
    print("Минимальный офсет:     :    ", offset)
    print("Максимальный офсет     :    ", maxofset)
    print("Минимальный BIN офсет  :    ", minbinoffset)
    print("Максимальный BIN офсет :    ", maxbinoffset)

