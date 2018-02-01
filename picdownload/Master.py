# encoding=utf-8
import requests
from HomeParser_1 import HomeParser
from HtmlDownloader_1 import HtmlDownloader
from PicDownloader_1 import PicDownloader
from ItemParser_1 import ItemParser

url = 'http://****'
index = 'http://**'
downloader = HtmlDownloader()
home = HomeParser()
item = ItemParser()
pic_downloader = PicDownloader()

html = downloader.download(url)
urls, titles = home.parser(index, html)
for i in range(0, 5):
    item_html = downloader.download(urls[i])
    item_title = titles[i]
    pic_urls, title = item.parser(item_html, item_title)
    pic_downloader.download(pic_urls, title)
# item_html = downloader.download(urls[3])
# pic_urls, title = item.parser(item_html, titles[3])
# pic_downloader.download(pic_urls, title)
