# encoding=utf-8
import requests
import lxml
import re
from bs4 import BeautifulSoup

url = "https://gitee.com/login"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
username = '*******'
password = '*******'

s = requests.session()
r = s.get(url, headers=header)
soup = BeautifulSoup(r.text, 'lxml')
token = soup.find(attrs={'name': 'csrf-token'}).get('content')

postdata = {
    'authenticity_token': token,
    'user[login]': username,
    'user[password]': password,
    'user[remember_me]': 0,
    'commit': '登 录'
}
login_page = s.post(url, data=postdata, headers=header)
settings_page = s.get('https://gitee.com/profile', headers=header)
print(settings_page.text)
