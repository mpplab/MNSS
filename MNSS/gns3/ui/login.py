# -*- coding: utf-8 -*-

"""
Module implementing login.
"""

from PyQt5.QtWidgets import QDialog
from gns3.ui.login_ui import Ui_login
from PyQt5 import QtWidgets
from gns3.globalvar import GlobalVar
from PyQt5.QtWidgets import QMessageBox
import winreg 

class login(QDialog, Ui_login):
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
        self.pushButton_1.clicked.connect(self.on_pushButton_1_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        try:
            keytoo = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\MNSS")
            value1,type1 = winreg.QueryValueEx(keytoo, "userid")
            value2,type2 = winreg.QueryValueEx(keytoo, "userpassword")
            self.userid.setText(value1)
            self.password.setText(value2)
            self.checkBox.setChecked(True)
        except WindowsError as e :
            pass
    
    def on_pushButton_1_clicked(self):
        while GlobalVar.loginmark == False:
            if GlobalVar.denlu(0, self.userid.text(), self.password.text()) == "success":
                GlobalVar.loginmark = True
                GlobalVar.userid = str(self.userid.text())
                GlobalVar.password = str(self.password.text())
                s = self.userid.text()
                pos = s.rfind("@")
                GlobalVar.userid1 = s[:pos]
                GlobalVar.ismodified = GlobalVar.getuserismodified(0,self.userid.text())
                GlobalVar.dictuser = GlobalVar.getuserinfo(0,self.userid.text())
                GlobalVar.imagename = GlobalVar.dictuser['imagename']
                GlobalVar.createfolder(0)
            else:
                QMessageBox.information(self,u'错误',u'请检查用户名和密码是否有误',QMessageBox.Yes )
                break
        if GlobalVar.loginmark == True:
            if self.checkBox.isChecked():
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer") 
                newKey = winreg.CreateKey(key,"MNSS")
                winreg.SetValueEx(newKey ,"userid",0 ,winreg.REG_SZ ,"{}".format(self.userid.text()))
                winreg.SetValueEx(newKey ,"userpassword",0 ,winreg.REG_SZ ,"{}".format(self.password.text()))
                self.reject()
            else:
                self.reject()
    
    def on_pushButton_2_clicked(self):
        self.userid.setText("")
        self.password.setText("")
          
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_login = QtWidgets.QDialog()
    ui = login()
    ui.show()
    sys.exit(app.exec_())