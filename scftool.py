import requests



scf_tikhonov = "https://www.marinetraffic.com/en/ais/details/ships/shipid:348129/mmsi:273350140/vessel:VYACHESLAV%20TIKHONOV"
scf_gubkin="https://www.marinetraffic.com/en/ais/details/ships/shipid:373676/mmsi:273399120/vessel:IVAN%20GUBKIN"


headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
tikhonov_response = requests.get(scf_tikhonov,headers=headers)
gubkin_response=requests.get(scf_gubkin,headers=headers)

if tikhonov_response.status_code == 200 and gubkin_response.status_code==200:
    tikhonov_response.encoding
    'utf-8'
    tikhonov_text = tikhonov_response.text
    gubkin_response.encoding
    'utf-8'
    gubkin_text = gubkin_response.text



else:
    print("Нет доступа к сайту marinetraffic")

def vessel_info(vessel_name,vessel_text):

    start_pos=vessel_text.find("Position Received:")
    end_pos=vessel_text.find('AIS Source:')
    vessel_text=vessel_text[start_pos:end_pos].strip()
    line=[]
    res=[]
    start_l1=0
    end_l1=vessel_text.find('Vessel')
    start_l2=vessel_text.find('Area:')
    end_l2=vessel_text.find('Latitude')
    start_l3=vessel_text.find('Latitude')
    end_l3=vessel_text.find('Status:')
    start_l4=vessel_text.find('Status:')
    end_l4=vessel_text.find('Speed/Course:')
    start_l5=vessel_text.find('Speed/Course:')
    end_l5=vessel_text.find('AIS')

    line.append(vessel_text[start_l1:end_l1].strip())
    line.append(vessel_text[start_l2:end_l2].strip())
    line.append(vessel_text[start_l3:end_l3].strip())
    line.append(vessel_text[start_l4:end_l4].strip())
    line.append(vessel_text[start_l5:end_l5].strip())

    d=['<strong>','<span>','div','</span>','</strong>','</strong>',
       '</ >', '<','/>','span','\r\n','/','/a>','group-ib">','  ','class="vertical-offset-10']
    for j in range(0,5,1):
        for i in d:
          line[j]=line[j].replace(i, '')


    res.append(vessel_name)
    for i in line:
        if i!=line[2]:
          res.append(i)
    res.append(" ")
    return res




