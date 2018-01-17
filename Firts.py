# encoding=utf-8
import sys
import requests
from bs4 import BeautifulSoup
import json
from lxml import etree
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

user_agent = 'Dedsec Home'
headers = {'User-Agent': user_agent}
request = requests.get("http://www.seputu.com/", headers=headers)

soup = BeautifulSoup(request.text, 'html.parser')
content = []

for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if h2!=None:
        list = []
        h2_title = h2.string
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            print href, box_title
            list.append({'链接': href, '标题': box_title})
        content.append({'title': h2_title, 'content': list})
with open('book.json', 'wb') as fp:
    json.dump(content, fp=fp, indent=4, ensure_ascii=False)


def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print(per)


html = etree.HTML(request.text)
http_href = html.xpath('.//a/@href')
i = 0
for url in http_href:
    urllib.urlretrieve(url, 'content'+str(i)+'.html', Schedule)
    i += 1
