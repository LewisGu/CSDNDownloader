import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

from csdndownloader_ui import Ui_MainWindow
from Function.csdn_url_analysis import *
 
class MyWindow(QMainWindow,Ui_MainWindow):
    """
    主要是UI相关功能代码，涉及信号/槽等
    """
    oneKeyDownloadSignal = pyqtSignal(list)
    logtext = ""
   
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.signal_connect()
        self.initUI()

    def signal_connect(self):
        """
        信号连接
        """
        self.oneKeyDownloadSignal.connect(self.onekey_download)
        self.Download_pbtn.clicked.connect(self.emitOneKeyDownloadSignal)

    def get_rbtn(self):
        if(self.blog_mode_rbtn.isChecked()):
            mode = "blog_mode"
        elif(self.column_mode_rbtn.isChecked()):
            mode = "column_mode"
        else:
            mode = "author_mode"         
        return mode

    def emitOneKeyDownloadSignal(self):
        """
        发射一键下载的信号函数
        """
        pList = []
        mode = self.get_rbtn()
        pList.append(mode)
        pList.append(self.blog_url_te.toPlainText())
        self.oneKeyDownloadSignal.emit(pList)

    def onekey_download(self, list):
        """
        连接一键下载的槽函数
        核心槽函数
        """
        mode = str(list[0])
        text = str(list[1])
        if mode == "blog_mode":
            self.blog_mode_analysis(text)     
        elif mode == "column_mode":
            # TODO
            pass
        else:
            # TODO
            pass

    def blog_mode_analysis(self,text):
        # 单文章模式代码
        titlelist = url_text_analysis(text)
        titlenum = len(titlelist)
        self.MessageBox = QMessageBox(self)
        if titlenum == 0:
            self.MessageBox.critical(self, "错误", "请输入正确的URL")
        elif titlenum == 1:
            titlename = titlelist[0]
            self.MessageBox.information(self, "正确", "文章 《"+titlename+"》 下载成功")
        else:
            titlenames = ""
            for title in titlelist:
                titlenames = titlenames + title + "\n"
            self.MessageBox.information(self, "正确", "文章\n"+titlenames+"下载成功")
        return

    def initUI(self):
        # 显示UI
        self.setWindowIcon(QIcon('CSDNDownloader.png'))
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MyWindow()
    sys.exit(app.exec_())