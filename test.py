import requests
import config


url="https://click.alfabank.ru/wealth-management/showcase/bonds"
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
tikhonov_response = requests.get(url,headers=headers)
tikhonov_response.encoding
'utf-8'
tikhonov_text = tikhonov_response.text
print(tikhonov_text)