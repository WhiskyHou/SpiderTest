# encoding=utf-8
from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
from lxml import etree
import re


def schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print(per)


url = 'http://*************'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

r = requests.get(url, headers=headers)
r.encoding = 'gbk'
soup = BeautifulSoup(r.text, 'lxml')
html = soup.find(class_='tpc_content do_not_catch')
print(html.contents)
pic_soup = BeautifulSoup(str(html.contents), 'lxml')
pic_html = pic_soup.find_all('input')
i = 0
for urls in pic_html:
    new_url = urls['src']
    try:
        req = urllib2.Request(url=new_url, headers=headers)
        binary_data = urllib2.urlopen(req).read()
        temp_file = open(str(i)+'.jpg', 'wb')
        temp_file.write(binary_data)
        temp_file.close()
        print(i)
    except:
        print("Pic" + str(i) + "download failed")
    i += 1
