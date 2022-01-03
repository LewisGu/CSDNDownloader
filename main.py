import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot

#这个test_pyqt是ui文件对应的py文件的文件名
from csdndownloader_ui import Ui_MainWindow
from csdn_url_analysis import *
 
#我的Form是用的QWidget作为基类
class MyWindow(QMainWindow,Ui_MainWindow):

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
        titlelist = urltextanalysis(text)
        titlenum = len(titlelist)
        self.MessageBox = QMessageBox(self)
        if titlenum == 0:
            self.MessageBox.critical(self, "错误", "请输入正确的URL")
        elif titlenum == 1:
            titlename = titlelist[0]
            self.MessageBox.information(self, "正确", "文章"+titlename+"下载成功")
        else:
            titlenames = ""
            for title in titlelist:
                titlenames = titlenames + title + "\n"
            self.MessageBox.information(self, "正确", "文章\n"+titlenames+"下载成功")
        return

    def initUI(self):
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MyWindow()
    sys.exit(app.exec_())