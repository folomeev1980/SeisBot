import requests
import config
smng_primakov = "https://www.marinetraffic.com/en/ais/details/ships/shipid:420483/mmsi:273392760/vessel:AKADEMIK%20PRIMAKOV"
smng_geoarctic="https://www.marinetraffic.com/en/ais/details/ships/shipid:350967/mmsi:273458600/vessel:GEO%20ARCTIC"
smng_nemchinov='https://www.marinetraffic.com/en/ais/details/ships/shipid:350868/mmsi:273454600/vessel:AKADEMIK%20NEMCHINOV'
smng_lazarev="https://www.marinetraffic.com/en/ais/details/ships/shipid:350770/mmsi:273450600/vessel:AKADEMIK%20LAZAREV"
smng_rjabinkin='https://www.marinetraffic.com/en/ais/details/ships/shipid:350930/mmsi:273457600/vessel:PROFESSOR%20RJABINKIN'
smng_shatskiy="https://www.marinetraffic.com/en/ais/details/ships/shipid:350821/mmsi:273452600/vessel:AKADEMIK%20SHATSKIY"
smng_iskatel5="https://www.marinetraffic.com/en/ais/details/ships/shipid:350842/mmsi:273453600/vessel:ISKATEL%205"


smng=[smng_primakov,smng_geoarctic,smng_nemchinov,smng_lazarev,smng_rjabinkin,smng_shatskiy,smng_iskatel5]
test=[]
text=[]

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
for i in smng:
 test.append(requests.get(i, headers=headers))
for i in test:
    i.encoding
    'utf-8'
    text.append(i.text)



ep='\n'.join(config.vessel_info("EVGENY PRIMAKOV",text[0]))
ga='\n'.join(config.vessel_info("GEOARCTIC",text[1]))
an='\n'.join(config.vessel_info("AKADEMIK NEMCHINOV",text[2]))
al='\n'.join(config.vessel_info("AKADEMIK LAZAREV",text[3]))
pr='\n'.join(config.vessel_info("PROFFESOR RJABINKIN",text[4]))
sha='\n'.join(config.vessel_info("AKADEMIK SHATSKIY",text[5]))
i5='\n'.join(config.vessel_info("ISKATEL 5",text[6]))

print(i5)