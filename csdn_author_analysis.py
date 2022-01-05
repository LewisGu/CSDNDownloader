import requests
import parsel
import tomd
import os
import re

from csdn_url_analysis import *

class author_mode():
    def __init__(self,authorname):
        self.author = authorname
        self.get_all_article()

    # 主要函数
    def get_all_article(self):
        self.get_article_link()
        for url in self.blog_url_list:
            CSDN_URL_Analysis(url)

    def get_article_link(self):
        page=1
        self.blog_url_list = []
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52",
            "Referer": "https://blog.csdn.net/tansty_zh"
            }
        while True:
            link = "https://blog.csdn.net/{}/article/list/{}".format(self.author, page)
            print("现在爬取第", page, "页")
            html = requests.get(url=link, headers=head).text
            cel = parsel.Selector(html)
            name_link = cel.css(".article-list h4 a::attr(href) ").getall()
            print(type(name_link))
            if not name_link:
                break
                #没有文章就退出
            else:
                self.blog_url_list.extend([url for url in name_link])
            page+=1

if __name__ == '__main__':
    print("本项目由tansty开发")
    # name=input("请输入博主的名称：")
    name="qq_36148333"
    author_mode(name)