# -*- coding: utf-8 -*-

"""
Module implementing showpersondata.
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from gns3.globalvar import GlobalVar
from gns3.ui.personaldata import persondata

from gns3.ui.showpersondata_ui import Ui_showpersondata


class showpersondata(QDialog, Ui_showpersondata):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(showpersondata, self).__init__(parent)
        self.setupUi(self)
        self.updatas()
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.reject()
        dialog = persondata(self)
        dialog.show()
        dialog.exec_()
    
    def updatas(self):
        userinformation = GlobalVar.getuserinfo(0,GlobalVar.userid)
        self.username.setText(userinformation['username'])
        self.age.setText(str(userinformation['age']))
        self.location.setText(userinformation['location'])
        self.profession.setText(userinformation['profession'])
        self.workplace.setText(userinformation['workplace'])
        self.email.setText(userinformation['email'])
        if userinformation['sex'] == 0:
            self.sex.setText("男")
        else:
            self.sex.setText("女")
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_showpersondata = QtWidgets.QDialog()
    ui = showpersondata()
    ui.show()
    sys.exit(app.exec_())