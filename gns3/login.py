# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from gns3.ui.login_ui import Ui_login_ui
from PyQt5.QtWidgets import QMessageBox
import winreg
from gns3.globalvar import GlobalVar
from gns3.login_authentication import user
import os
import threading

class login(QDialog, Ui_login_ui):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(login, self).__init__(parent)
        self.setupUi(self)
        self.newuser = user()
        self.networkmark = False
        self.login_button.clicked.connect(self.login_button_clicked)
        self.reset_button.clicked.connect(self.reset_button_clicked)
        try:
            keytoo = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\MNSS")
            value1,type1 = winreg.QueryValueEx(keytoo, "username")
            value2,type2 = winreg.QueryValueEx(keytoo, "userpassword")
            self.username.setText(value1)
            self.password.setText(value2)
            self.checkBox.setChecked(True)
        except WindowsError as e :
            pass
    
    def login_button_clicked(self):
        self.networkjudgment()
        if self.networkmark:
            newjob = threading.Thread(target=GlobalVar().getdict)
            newjob.start()
            while GlobalVar.loginmark == False:
                if self.newuser.login_mark(self.username.text(),self.password.text()) == True:
                    GlobalVar.loginmark = True
                else:
                    QMessageBox.information(self,u'错误',u'请检查用户名和密码是否有误',QMessageBox.Yes )
                    break
            if GlobalVar.loginmark == True:
                if self.checkBox.isChecked():
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")
                    newKey = winreg.CreateKey(key,"MNSS")
                    winreg.SetValueEx(newKey ,"username",0 ,winreg.REG_SZ ,"{}".format(self.username.text()))
                    winreg.SetValueEx(newKey ,"userpassword",0 ,winreg.REG_SZ ,"{}".format(self.password.text()))
                    self.reject()
                else:
                    self.reject()

    def reset_button_clicked(self):
        self.username.setText("")
        self.password.setText("")

    def networkjudgment(self):
        mark = os.system('ping www.baidu.com -n 2')
        if mark == 0:
            self.networkmark = True
        else:
            QMessageBox.information(self, u'警告', u'请检查网络是否通畅', QMessageBox.Yes)