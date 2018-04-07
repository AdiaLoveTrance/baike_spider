"""
网页解析
"""

from bs4 import BeautifulSoup
import re
from urllib import parse


class HtmlParser(object):
    new_urls = set()  # 解析出的URL集合

    def __get_new_urls(self, page_url, soup):
        """根据网页内容，解析出网页中词条URL"""
        links = soup.find_all('a', href=re.compile(r"/item/.+"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            HtmlParser.new_urls.add(new_full_url)
        return HtmlParser.new_urls

    def __get_new_data(self, page_url, soup):
        """根据网页内容，解析出词条名和词条简介"""
        res_data = dict()

        res_data['url'] = page_url

        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # summary_node = soup.find('div', class_="lemma-summary")
        # res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        """返回解析出的新URL集合和词条名、词条简介"""
        if (page_url is None) or (html_cont is None):
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        return new_urls, new_data