# encoding=utf-8
import os
import requests


class PicDownloader(object):
    def download(self, urls, title):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        try:
            os.mkdir(title)
        except:
            print('dir has been created')
            return
        i = 0
        for url in urls:
            try:
                req = requests.get(url, headers=headers)
                data = req.content
                file = open(title+'/'+str(i)+'.jpg', 'wb')
                file.write(data)
                file.close()
                print(title + str(i))
            except:
                print('picture save failed')
            i += 1
        print('work ' + title + ' was complete')
