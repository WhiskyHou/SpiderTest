# encoding=utf-8
from bs4 import BeautifulSoup


class HomeParser(object):
    def parser(self, index, html):
        if html is None:
            return None
        soup = BeautifulSoup(html, 'lxml')
        contents = soup.find_all(class_='tal')
        urls = []
        titles = []
        for content in contents:
            soup2 = BeautifulSoup(str(content.contents), 'lxml')
            data = soup2.find('a')
            urls.append(index + data['href'])
            titles.append(data.string)
        return urls, titles
