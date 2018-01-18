# encoding=utf-8
from UrlManager import UrlManager
from HtmlParser import htmlParser
from HtmlDownloader import HtmlDownloader
from DataOutput import DataOutput


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = htmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print(self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
        self.output.output_html()


if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E7%BB%9D%E5%9C%B0%E6%B1%82%E7%94%9F%EF%BC%9A%E5%A4%A7%E9%80%83%E6%9D%80")
