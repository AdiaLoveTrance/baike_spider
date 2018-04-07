"""
从百度百科python词条开始，爬取1000个词条页面，得到词条URL、词条名和词条简介，输出并保存为HTML文档
程序入口、爬虫调度器，
"""

import url_manager, html_downloader, html_parser, html_outputer
import time


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        """调用url管理、网页下载、网页解析和结果输出"""
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                # time.sleep(1)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except Exception as e:
                print("craw failed", new_url, e)
        self.outputer.output_html()





if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/%E5%8C%BB%E7%96%97%E4%BF%9D%E9%99%A9/637613"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)