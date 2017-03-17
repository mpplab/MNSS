# -*- coding: utf-8 -*-

"""
Module implementing NewLogin.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from gns3.qt import QtWidgets, QtCore
from urllib import request
import urllib

import webbrowser
import json
from gns3.globalvar import GlobalVar



from gns3.ui.Ui_Login_ui import Ui_Dialog


class NewLogin(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(NewLogin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open("http://139.196.202.32:8080/secbox/register.jsp")
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        url = "http://139.196.202.32:8080/secbox/loginAction"
        postdata =urllib.parse.urlencode({    
        "username":self.lineEdit.text(),
        "pswd":self.lineEdit_2.text(),
        }).encode('utf-8')
        header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Host":"c.highpin.cn",
        "Referer":"http://c.highpin.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
        }
        req = urllib.request.Request(url,postdata,header)
        page = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(page)
        if data['ret'] == 'success':
            GlobalVar.loginmark = True
            self.destroyed()
        else:
            QMessageBox.information(self,u'输入有误',u'请检查你的输入是否有误！', QMessageBox.Yes | QMessageBox.No)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a = QtWidgets.QMainWindow()
    dialog = NewLogin(a)
    dialog.show()
    exit_code = app.exec_()
