# -*- coding: utf-8 -*-

"""
Module implementing userlogin.
"""

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from gns3.ui.personaldata import persondata
from gns3.globalvar import GlobalVar
from gns3.ui.userlogin_ui import Ui_userlogin
from gns3.ui.Avatar import Avatar
from gns3.ui.showpersondata import showpersondata
import urllib.request

class userlogin(QDialog, Ui_userlogin):

    def __init__(self, parent=None):
        super(userlogin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.updates()
    
    def on_pushButton_2_clicked(self):
        if GlobalVar.ismodified == 1:
            dialog = showpersondata(self)
            dialog.show()
            dialog.exec_()
        else:
            dialog = persondata(self)
            dialog.show()
            dialog.exec_()
        self.updates()

    def on_pushButton_3_clicked(self):
        dialog = Avatar(self)
        dialog.show()
        dialog.exec_()
        self.updates()
        
    def updates(self):
        if GlobalVar.imagepath == "":
            pass
        else:
            imagepath = urllib.request.pathname2url(GlobalVar.imagepath) 
            realpath = imagepath[3:]
            self.frame.setStyleSheet("border-image: url({});".format(realpath))
        if GlobalVar.dictuser['username'] == "":
            pass
        else:
            self.username.setText("{}".format(GlobalVar.dictuser['username']))
        self.inuselabel.setText("{}K/1G".format(GlobalVar.getuserinuse(0, GlobalVar.userid)))
        self.inuseprogressBar.setValue(int(GlobalVar.getuserinuse(0, GlobalVar.userid)[:1]))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_persondata = QtWidgets.QDialog()
    ui = userlogin()
    ui.show()
    sys.exit(app.exec_())
