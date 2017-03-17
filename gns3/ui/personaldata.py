# -*- coding: utf-8 -*-

"""
Module implementing persondata.
"""

from PyQt5.QtWidgets import QDialog
from PyQt5 import  QtWidgets
from gns3.globalvar import GlobalVar
from PyQt5.QtWidgets import QMessageBox

from gns3.ui.personaldata_ui import Ui_persondata


class persondata(QDialog, Ui_persondata):

    def __init__(self, parent=None):
        super(persondata, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.username.setText(GlobalVar.dictuser['username'])
        self.age.setText(str(GlobalVar.dictuser['age']))
        self.location.setText(GlobalVar.dictuser['location'])
        self.workplace.setText(GlobalVar.dictuser['workplace'])
        self.email.setText(GlobalVar.dictuser['email'])
        list1 = ['在校学生','在职员工','科研人员','其他']
        if GlobalVar.dictuser['profession'] == '':
            self.comboBox_2.setCurrentIndex(list1.index('在校学生'))
        else:
            self.comboBox_2.setCurrentIndex(list1.index(GlobalVar.dictuser['profession']))
        self.comboBox_1.setCurrentIndex(GlobalVar.dictuser['sex'])

    def on_pushButton_clicked(self):
        sex = 0
        if self.comboBox_1.currentText() == "男":
            sex = 0
        else:
            sex = 1
        username = self.username.text()
        age = self.age.text()
        profession = self.comboBox_2.currentText()
        location = self.location.text()
        workplace = self.workplace.text()
        email = self.email.text()
        dictdata = {'username': username, 'sex': sex, 'workplace': workplace, 'location': location, 'profession': profession,'email':email,'age':age}
        GlobalVar.setuserinfo(0, GlobalVar.userid, dictdata)
        GlobalVar.dictuser["username"] = username
        QMessageBox.information(self,u'提示',u'保存成功',QMessageBox.Yes )
        self.reject()
        
    def on_pushButton_2_clicked(self):
        self.reject()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_persondata = QtWidgets.QDialog()
    ui = persondata()
    ui.show()
    sys.exit(app.exec_())

