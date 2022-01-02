from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox
import re
import parsel
import tomd
import requests
class CSDN():
    def __init__(self):
        self.windows = QMainWindow()
        self.windows.resize(450, 300)
        self.windows.setWindowTitle("轻松获取csdn文章--by tansty")
        self.setup_ui()
        self.set_connect()
    def set_connect(self):
        #设置建立联系
        self.button.clicked.connect(self.gen_file)
    def setup_ui(self):
        #设置ui界面的建立
        self.button = QPushButton(self.windows)
        self.button.resize(100, 100)
        self.button.move(150, 150)
        self.button.setText("获取文章")
        self.text = QPlainTextEdit(self.windows)
        self.text.setPlaceholderText("请输入需要获取文章的链接")
        self.text.resize(450, 100)
    def gen_file(self):
        self.spider_csdn()
        self.gen_md_file()
    def spider_csdn(self):
        # 目标文章的链接
        title_url=self.text.toPlainText()
        self.MessageBox = QMessageBox(self.windows)
        if not title_url:
            MessageBox.critical(self.windows, "错误", "请输入网址")
            return
        head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"
        }
        html=requests.get(url=title_url,headers=head).text
        page=parsel.Selector(html)
        #创建解释器
        self.title=page.css(".title-article::text").get()
        res = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
        restr = ''
        res.sub(restr, self.title)
        content=page.css("article").get()
        content=re.sub("<a.*?a>","",content)
        content = re.sub("<br>", "", content)
        self.texts=tomd.Tomd(content).markdown

    def gen_md_file(self):
        #转换为markdown 文件
        filename = self.title+".md"
        with open(filename,mode="w+",encoding="utf-8") as f:
            f.write("# "+self.title)
            f.write(self.texts)
            self.MessageBox.information(self.windows,"正确","获取文章完成")

if __name__ == '__main__':
    app = QApplication()
    csdn=CSDN()
    csdn.windows.show()
    app.exec_()
