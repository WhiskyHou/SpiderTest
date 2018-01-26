# encoding=utf-8

import requests
from bs4 import BeautifulSoup
import urllib
import json

user_agent = "Dedsec X - 2"
header = {'User-Agent': user_agent}
request = requests.get("http://www.zhihu.com", headers=header)
print(request.text)
# bs = BeautifulSoup(request.text, "html-parser")
# print(bs)
