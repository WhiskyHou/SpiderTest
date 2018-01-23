# encoding=utf-8

import requests
from bs4 import BeautifulSoup

user_agent = "Dedsec X - 2"
header = {'User-Agent': user_agent}
request = requests.get("http://xxhouyi.cn", headers=header)
print(request.text)
bs = BeautifulSoup(request.text, 'html-parser')
print(bs)
