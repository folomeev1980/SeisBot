import config
import requests


valut = "https://www.finanz.ru/valyuty/v-realnom-vremeni"
gold="http://gold-today.ru/sberbank_kurs_zolota_segodnya"


valut_response = requests.get(valut)
if valut_response.status_code == 200:
    valut_response.encoding
    'utf-8'
    valut_text = valut_response.text


else:
    print("Нет доступа к сайту finanz")

gold_response = requests.get(gold)
if valut_response.status_code == 200:
    gold_response.encoding
    'utf-8'
    gold_text = gold_response.text


else:
    print("Нет доступа к сайту sberbank")




start_pos=valut_text.find("ММВБ")
end_pos=valut_text.find('class="sub_navigation')
valut_text=valut_text[start_pos:end_pos].strip()
valut_text=config.remove_html_markup(valut_text)
line=[]
res=[]
start_l1=valut_text.find('USD/RUB')
end_l1=valut_text.find('РТС')
start_l2=valut_text.find('EUR/RUB')
end_l2=valut_text.find('Dow')
start_l3=valut_text.find('EUR/USD')
end_l3=start_l3+100
start_l4=valut_text.find('Нефть')
end_l4=valut_text.find('EUR/RUB')
start_l5=valut_text.find('Золото')
end_l5=valut_text.find('EUR/USD')

line.append(valut_text[start_l1:end_l1].strip())
line.append(valut_text[start_l2:end_l2].strip())
line.append(valut_text[start_l3:end_l3].strip())
line.append(valut_text[start_l4:end_l4].strip())
line.append(valut_text[start_l5:end_l5].strip())

d=['&nbsp;','\t\t\t\t\t\t','class="text_right">','a> th> \t\t\t\t\t\t td >','</strong>','</strong>',
       '\xa0', '<','/>','span','\r\n','/a>','group-ib">','  ','class="vertical-offset-10']
for j in range(0,5,1):
        for i in d:
          line[j]=line[j].replace(i, ' ')

d=[',']
for j in range(0,5,1):
        for i in d:
          line[j]=line[j].replace(i, '.')


line[4]=line[4].split(" ")
line[4]=[line[4][0], line[4][1]+line[4][2]]

line2=[]
for j in range(0,4,1):
    line[j]=line[j].strip().split(" ")
    line2.append(line[j][0]+" "+(line[j][1]))
line2.append(line[4][0]+" "+line[4][1])



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
start_pos=gold_text.find("покупка")
end_pos=gold_text.find('Значение курса золота')
gold_text=gold_text[start_pos:end_pos].strip()
gold_text=config.remove_html_markup(gold_text)
line1=(config.remove_html_markup(gold_text)).strip().split(" ")
d=['&nbsp;','\t\t\t\t\t\t','class="text_right">','a> th> \t\t\t\t\t\t td >','</strong>','</strong>',
       '\xa0', '<','/>','span','\r\n','\t','-','  ','class="vertical-offset-10']
for j in range(0,len(line1)):
        for i in d:
          line1[j]=line1[j].replace(i, ' ')

line1[2]=line1[2].split(" ")


line2.append(line1[0]+" "+line1[2][0])
line2.append("продажа "+line1[4])

d=[',']
for j in range(0,7,1):
        for i in d:
          line2[j]=line2[j].replace(i, '.')
line3=[]
for j in line2:
    j=j.split(" ")
    line3.append(j[0]+": "+"{0:.2f}".format(float(j[1])))
valuta='\n'.join(line3)

