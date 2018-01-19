# encoding=utf-8
from multiprocessing.managers import BaseManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import htmlParser


class SpiderManager(object):
    def __init__(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        server_addr = 'localhost'
        print("connect to server localhost")
        self.m = BaseManager(address=(server_addr, 8010), authkey="baidu")
        self.m.connect()
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader()
        self.parser = htmlParser()

    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        print("NodeManager told spider end")
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print("spider is parsering "+url.encode('utf-8'))
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError as e:
                print("connect to node failed")
                return
            except Exception as e:
                print("crawl failed")
                return

if __name__ == '__main__':
    spider = SpiderManager()
    spider.crawl()