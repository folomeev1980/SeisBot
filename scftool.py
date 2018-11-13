import requests
import config



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




vt1='\n'.join(config.vessel_info("VYACHESLAV TIKHONOV",tikhonov_text))
ig='\n'.join(config.vessel_info("IVAN GUBKIN",gubkin_text))

if vt1.rfind('; ">a')>0:
    vt=vt1[0:(vt1.rfind('; ">a'))+1]
else:
    vt=vt1

