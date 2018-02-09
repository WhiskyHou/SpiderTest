# encoding=utf-8
from bs4 import BeautifulSoup

class ItemParser(object):
    def parser(self, html, title):
        if html is None:
            return
        soup = BeautifulSoup(html, 'lxml')
        contents = soup.find(class_='tpc_content do_not_catch')
        if contents is None:
            return None, None
        soup2 = BeautifulSoup(str(contents.contents), 'lxml')
        pic_contents = soup2.find_all('input')
        pic_urls = []
        for content in pic_contents:
            pic_urls.append(content['src'])
        return pic_urls, title
