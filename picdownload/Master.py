# encoding=utf-8
from HomeParser_1 import HomeParser
from HtmlDownloader_1 import HtmlDownloader
from PicDownloader_1 import PicDownloader
from ItemParser_1 import ItemParser
import threading

url = 'http://******'
index = 'http://******'
downloader = HtmlDownloader()
home = HomeParser()
item = ItemParser()
pic_downloader = PicDownloader()

html = downloader.download(url)
urls, titles = home.parser(index, html)
for i in range(0, 100):
    item_html = downloader.download(urls[i])
    item_title = titles[i]
    pic_urls, title = item.parser(item_html, item_title)
    thread = threading.Thread(target=pic_downloader.download, args=(pic_urls, title))
    thread.start()
    thread.join(30)
    print('work ' + str(i) + ' was complete')
# item_html = downloader.download(urls[3])
# pic_urls, title = item.parser(item_html, titles[3])
# pic_downloader.download(pic_urls, title)
