# encoding=utf-8

import requests
import datetime
import lxml
import os
import win32api
import win32gui
import win32con
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
index_url = "https://bing.ioliu.cn"
index_html = ''
image_html = ''


request = requests.get(url=index_url, headers=headers)
if request.status_code == 200:
    request.encoding = 'utf-8'
    index_html = request.text

index_soup = BeautifulSoup(index_html, 'lxml')
item_html = index_soup.find(class_='item')

item_soup = BeautifulSoup(str(item_html), 'lxml')
item_src = item_soup.find('a')

image_url = index_url + item_src['href']
image_request = requests.get(url=image_url, headers=headers)
if image_request.status_code == 200:
    image_request.encoding = 'utf-8'
    image_html = image_request.text

image_soup = BeautifulSoup(image_html, 'lxml')
pic_src = image_soup.find(class_='target progressive__img progressive--not-loaded')
pic_src = pic_src['data-progressive']

down_request = requests.get(url=pic_src, headers=headers)
data = down_request.content
today = datetime.date.today()
file = open(str(today)+'.jpg', 'wb')
file.write(data)
file.close()


image_path = os.getcwd() + '/' + str(today) + '.jpg'

reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
# 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
# 最后的参数:1表示平铺,拉伸居中等都是0
win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
# 刷新桌面
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, win32con.SPIF_SENDWININICHANGE)
