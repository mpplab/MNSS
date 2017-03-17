# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personaldata_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,  QtWidgets

class Ui_persondata(object):
    def setupUi(self, Ui_persondata):
        Ui_persondata.setObjectName("Ui_persondata")
        Ui_persondata.resize(300, 364)
        Ui_persondata.setMinimumSize(QtCore.QSize(300, 350))
        Ui_persondata.setMaximumSize(QtCore.QSize(99999, 99999))
        Ui_persondata.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Ui_persondata.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(Ui_persondata)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 93, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:solid 1px black opacity 0.4;\n"
"    border-width: 1px;\n"
"    background-color: white;\n"
"    border-color: rgb(171,168,165);\n"
"    border-style: outset;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: rgb(240,240,240);\n"
"    border-style: inset;\n"
"    }")
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(Ui_persondata)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 72, 15))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Ui_persondata)
        self.label_11.setGeometry(QtCore.QRect(30, 260, 41, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Ui_persondata)
        self.label_12.setGeometry(QtCore.QRect(30, 60, 41, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_2 = QtWidgets.QPushButton(Ui_persondata)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 310, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border:solid 1px black opacity 0.4;\n"
"    border-width: 1px;\n"
"    background-color: white;\n"
"    border-color: rgb(171,168,165);\n"
"    border-style: outset;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: rgb(240,240,240);\n"
"    border-style: inset;\n"
"    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.workplace = QtWidgets.QLineEdit(Ui_persondata)
        self.workplace.setGeometry(QtCore.QRect(90, 218, 191, 20))
        self.workplace.setStyleSheet("background-color: transparent")
        self.workplace.setObjectName("workplace")
        self.email = QtWidgets.QLineEdit(Ui_persondata)
        self.email.setGeometry(QtCore.QRect(90, 258, 191, 20))
        self.email.setStyleSheet("background-color: transparent")
        self.email.setObjectName("email")
        self.location = QtWidgets.QLineEdit(Ui_persondata)
        self.location.setGeometry(QtCore.QRect(90, 138, 191, 20))
        self.location.setStyleSheet("background-color: transparent")
        self.location.setObjectName("location")
        self.username = QtWidgets.QLineEdit(Ui_persondata)
        self.username.setEnabled(True)
        self.username.setGeometry(QtCore.QRect(90, 18, 140, 20))
        self.username.setStyleSheet("background-color: transparent")
        self.username.setText("")
        self.username.setFrame(True)
        self.username.setDragEnabled(False)
        self.username.setReadOnly(False)
        self.username.setObjectName("username")
        self.label_9 = QtWidgets.QLabel(Ui_persondata)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 41, 21))
        self.label_9.setObjectName("label_9")
        self.comboBox_2 = QtWidgets.QComboBox(Ui_persondata)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 178, 91, 20))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.age = QtWidgets.QLineEdit(Ui_persondata)
        self.age.setGeometry(QtCore.QRect(90, 58, 140, 20))
        self.age.setStyleSheet("background-color: transparent")
        self.age.setObjectName("age")
        self.comboBox_1 = QtWidgets.QComboBox(Ui_persondata)
        self.comboBox_1.setGeometry(QtCore.QRect(90, 98, 91, 20))
        self.comboBox_1.setStyleSheet("")
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.label = QtWidgets.QLabel(Ui_persondata)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ui_persondata)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Ui_persondata)
        self.label_3.setGeometry(QtCore.QRect(25, 140, 61, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Ui_persondata)

    def retranslateUi(self, Ui_persondata):
        _translate = QtCore.QCoreApplication.translate
        Ui_persondata.setWindowTitle(_translate("Ui_persondata", "编辑资料"))
        self.pushButton.setText(_translate("Ui_persondata", "保存"))
        self.label_10.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">所在单位</span></p></body></html>"))
        self.label_11.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">邮  箱</span></p></body></html>"))
        self.label_12.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">年  龄</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Ui_persondata", "关闭"))
        self.label_9.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">职  业</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Ui_persondata", "在校学生"))
        self.comboBox_2.setItemText(1, _translate("Ui_persondata", "在职员工"))
        self.comboBox_2.setItemText(2, _translate("Ui_persondata", "科研人员"))
        self.comboBox_2.setItemText(3, _translate("Ui_persondata", "其他"))
        self.comboBox_1.setItemText(0, _translate("Ui_persondata", "男"))
        self.comboBox_1.setItemText(1, _translate("Ui_persondata", "女"))
        self.label.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">姓  名</span></p></body></html>"))
        self.label_2.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">性  别</span></p></body></html>"))
        self.label_3.setText(_translate("Ui_persondata", "<html><head/><body><p><span style=\" color:#808080;\">所在地</span></p></body></html>"))

