"""
网页下载
"""

from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        """使用urllib.request.urlopen()下载网页内容"""
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read().decode("utf-8")