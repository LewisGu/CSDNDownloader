import requests
import parsel
import tomd
import os
import re

head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"
        }

class CSDN_URL_Analysis():
    def __init__(self,url):
        if len(url) == 1:
            url = url[0]
        self.url = url
        self.gen_md_by_one_url()

    def gen_md_by_one_url(self):
        # 核心功能代码
        self.get_csdn_texts()
        self.save_md_file_from_html()

    def get_csdn_texts(self):
        html=requests.get(url=self.url,headers=head).text
        page=parsel.Selector(html)
        #创建解释器
        title = page.css(".title-article::text").get()
        res = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
        restr = ''
        res.sub(restr, title)
        content=page.css("article").get()
        content=re.sub("<a.*?a>","",content)
        content = re.sub("<br>", "", content)
        text = tomd.Tomd(content).markdown
        self.title = title
        self.text = text
            
    def save_md_file_from_html(self):
        #转换为markdown 文件
        filename = self.title+".md"
        currentWD = os.getcwd()
        filenameWithD = currentWD + "\\" + filename
        with open(filenameWithD,mode="w",encoding="utf-8") as f:
            f.write("# "+self.title)
            f.write(self.text)

def urlanalysis(urltext):
    # 解析一个或多个url
    reexp_http = 'http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urllist = re.findall(reexp_http, urltext)
    if len(urllist) < 1:
        return [],0
    elif len(urllist) == 1:
        return urllist[0],1
    else:
        no_repeat_url_list = list(set(urllist))
        no_repeat_url_list.sort(key=urllist.index)
        return no_repeat_url_list,len(no_repeat_url_list)

def urltextanalysis(urltext):
    [url_list,urlnum] = urlanalysis(urltext)
    titlelist = []
    if urlnum == 0:
        pass
    elif urlnum == 1:
        a = CSDN_URL_Analysis(url_list)
        titlelist.append(a.title)
    else:
        for url in url_list:
            a = CSDN_URL_Analysis(url)
            # a.gen_md_by_one_url()
            titlelist.append(a.title)
    return titlelist

if __name__ == '__main__':
    # 单url解析
    # urltextanalysis("https://jia666666.blog.csdn.net/article/details/81534260") 
    # 多不重复url解析
    # urltextanalysis("https://jia666666.blog.csdn.net/article/details/81534260https://jia666666.blog.csdn.net/article/details/81534431") 
     # 多重复url解析
    # urltextanalysis("https://jia666666.blog.csdn.net/article/details/81534260https://jia666666.blog.csdn.net/article/details/81534260")
     # 多不重复/重复url解析
    # urltextanalysis("https://jia666666.blog.csdn.net/article/details/81534260https://jia666666.blog.csdn.net/article/details/81534431https://jia666666.blog.csdn.net/article/details/81534260")
    urltextanalysis("urls")