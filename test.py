import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from progress.bar import Bar
from openpyxl import Workbook, load_workbook

url="https://www.marinetraffic.com/en/ais/details/ships/shipid:348129/mmsi:273350140/imo:9538115/vessel:VYACHESLAV_TIKHONOV"
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
tikhonov_response = requests.get(url,headers=headers)
# tikhonov_response.encoding
# 'utf-8'
# tikhonov_text = tikhonov_response.text
#
#
# print(tikhonov_text)
#
# soup=BeautifulSoup(tikhonov_text,"lxml")
# soup=soup.find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-true")
# print(soup)

def get_ship_info(vessel_name,url):
    res=[]
    res.append(vessel_name)

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x935')
        driver = webdriver.Chrome('chromedriver.exe', options=options)
        driver.get(url)
    except Exception as e:

        driver.quit()

    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")

    tds = soup.find("div",class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-md-true").findAll("p")
    for i in tds:
        if "Position Received" in str(i.text):
           # print(i.text)
            res.append(i.text)
        elif "Area:" in str(i.text):
          #  print(i.text )
            res.append(i.text)
        elif "Status:" in str(i.text):
         #   print(i.text)
            res.append(i.text)

        elif "Speed/Course:" in str(i.text):
         #   print(i.text)
            res.append(i.text)
        else:
            pass
    return res

print(get_ship_info(url))