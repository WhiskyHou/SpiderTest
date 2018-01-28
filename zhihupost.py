# encoding=utf-8
import requests
import lxml
import re
from bs4 import BeautifulSoup

url = "https://zhihu.com"
posturl = "https://www.zhihu.com/api/v3/oauth/sign_in"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
username = '+86******'
password = '******'

s = requests.session()
# r = s.get(url, headers=header)
# soup = BeautifulSoup(r.text, 'lxml')
# token = soup.find(attrs={'name': 'csrf-token'}).get('content')

postdata = {
    'username': username,
    'password': password,
}
login_page = s.post(posturl, data=postdata, headers=header)
home_page = s.get(url, headers=header)
print(home_page.text)