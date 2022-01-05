from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
from UI import MainWindowUI

from GlobalConfig import *
from csdn_url_analysis import *

class WidgetLogic(QWidget):
    oneKeyDownloadSignal = pyqtSignal(list) # 下载模式 输入内容
    clearLogSignal = pyqtSignal()
    saveLogSignal = pyqtSignal()

    def __init__(self, parent=None):
        # UI初始化
        super().__init__(parent)
        self.__ui = MainWindowUI.Ui_Form()
        self.__ui.setupUi(self)
        self.__ui.retranslateUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 保持窗口最前
        self.signal_connect()

        # 全局模式初始化
        self.downloadtype = self.blog_mode
        self.input = blank

    def signal_connect(self):
        """
        信号连接
        """
        """
        信号与槽连接
        """
        # 一键下载
        #toggled信号与槽函数绑定
        self.__ui.blog_mode_rbtn.toggled.connect(self.blog_mode_editable)
        self.__ui.column_mode_rbtn.toggled.connect(self.column_mode_editable)
        self.__ui.author_mode_rbtn.toggled.connect(self.author_mode_editable)

        self.__ui.Download_pbtn.clicked.connect(self.oneKeyDownloadSignal_handler)
        self.oneKeyDownloadSignal.connect(self.onekey_download)


    """当模式选择后，部分输入框变灰"""
    def blog_mode_editable(self,able:bool = True):
        self.__ui.column_url_le.setText(blank)
        self.__ui.column_url_le.setDisabled(able)
        self.__ui.author_le.setText(blank)
        self.__ui.author_le.setDisabled(able)
        self.downloadtype = self.blog_mode

    def column_mode_editable(self,able:bool = True):
        self.__ui.blog_url_te.setPlainText(blank)
        self.__ui.blog_url_te.setDisabled(able)
        self.__ui.author_le.setText(blank)
        self.__ui.author_le.setDisabled(able)
        self.downloadtype = self.column_mode

    def author_mode_editable(self,able:bool = True):
        self.__ui.column_url_le.setText(blank)
        self.__ui.column_url_le.setDisabled(able)
        self.__ui.blog_url_te.setPlainText(blank)
        self.__ui.blog_url_te.setDisabled(able)
        self.downloadtype = self.author_mode

    # 已改写
    def oneKeyDownloadSignal_handler(self):
        """
        一键下载按钮控件点击触发的槽
        """
        download_config = []
        download_config.append(self.downloadtype)
        
        self.get_input_text()
        MessageBox = QMessageBox(self)
        if not self.inputtext:
            # 校验
            MessageBox.critical(self, "错误", "请输入内容")
            return
        else:
            download_config.append(self.inputtext)
            # 发射信号，传输配置(类型及输入)
            self.oneKeyDownloadSignal.emit(download_config)

    def get_input_text(self):
        if self.downloadtype == blog_mode:
            self.inputtext = self.__ui.blog_url_te.toPlainText() # 获取输入 eg
        elif self.downloadtype == blog_mode:
            self.inputtext = self.__ui.column_url_le.text() # 获取输入 eg
        else:
            self.inputtext = self.__ui.column_url_le.text() # 获取输入 eg
    
    def onekey_download(self, list):
        """
        连接一键下载的槽函数
        核心槽函数
        """
        mode = list[0]
        text = str(list[1])
        if mode == blog_mode:
            self.blog_mode_analysis(text)     
        elif mode == column_mode:
            # TODO
            pass
        else: # mode == author_mode
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

    # 已改写
    def blog_write(self, msg: str):
        """将提示消息写入log_tb"""
        # TODO 显示接收时间
        if self.receive_show_flag:
            self.__ui.log_tb.setText(msg)

    def info_write(self, info: str, mode: int): 
        """
        将接收到或已发送的消息写入ReceivePlainTextEdit
        :param info: 接收或发送的消息
        :param mode: 模式，接收/发送
        :return: None
        """
        if self.receive_show_flag:
            if mode == self.InfoRec:
                self.__ui.ReceivePlainTextEdit.appendHtml(
                    f'<font color="blue">{info}</font>'
                )
                self.ReceiveCounter += 1
                self.counter_signal.emit(self.SendCounter, self.ReceiveCounter)
            elif mode == self.InfoSend:
                self.__ui.ReceivePlainTextEdit.appendHtml(
                    f'<font color="green">{info}</font>'
                )
            self.__ui.ReceivePlainTextEdit.appendHtml("\n")
        else:
            if mode == self.InfoRec:
                self.ReceiveCounter += 1
                self.counter_signal.emit(self.SendCounter, self.ReceiveCounter)

    blog_mode = 0
    column_mode = 1
    author_mode = 2


if __name__ == "__main__":
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = WidgetLogic()
    window.show()
    sys.exit(app.exec_())
