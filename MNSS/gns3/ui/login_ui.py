# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login_ui):
        login_ui.setObjectName("login_ui")
        login_ui.resize(555, 315)
        login_ui.setMinimumSize(QtCore.QSize(555, 315))
        login_ui.setMaximumSize(QtCore.QSize(555, 315))
        login_ui.setStyleSheet("")
        login_ui.setSizeGripEnabled(True)
        self.label_2 = QtWidgets.QLabel(login_ui)
        self.label_2.setGeometry(QtCore.QRect(230, 160, 72, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(login_ui)
        self.checkBox.setGeometry(QtCore.QRect(400, 190, 91, 19))
        self.checkBox.setStyleSheet("font: 9pt \"Agency FB\";\n"
"color: rgb(86, 118, 162);\n"
"text-decoration: underline;")
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(login_ui)
        self.label.setGeometry(QtCore.QRect(230, 110, 72, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(login_ui)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 571, 361))
        self.label_3.setMinimumSize(QtCore.QSize(571, 361))
        self.label_3.setStyleSheet("background-image: url(:/images/background.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(login_ui)
        self.label_4.setGeometry(QtCore.QRect(40, 105, 160, 160))
        self.label_4.setStyleSheet("image: url(:/images/logo.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.userid = QtWidgets.QLineEdit(login_ui)
        self.userid.setGeometry(QtCore.QRect(300, 106, 181, 24))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.userid.setFont(font)
        self.userid.setObjectName("userid")
        self.password = QtWidgets.QLineEdit(login_ui)
        self.password.setGeometry(QtCore.QRect(300, 154, 181, 24))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet("lineedit-password-character:42")
        self.password.setObjectName("password")
        self.pushButton_2 = QtWidgets.QPushButton(login_ui)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 220, 90, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(17, 100, 162, 255), stop:1 rgba(61, 140, 201, 255));\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    font: 75 12pt \"黑体\";\n"
"    color:white;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(149, 187, 209, 255), stop:1 rgba(218, 238, 249, 255));\n"
"    border-style: inset;\n"
"    border-radius: 8px;\n"
"    font: 75 12pt \"黑体\";\n"
"    color:#15589C;\n"
"    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(login_ui)
        self.pushButton_1.setGeometry(QtCore.QRect(280, 220, 90, 30))
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(149, 187, 209, 255), stop:1 rgba(218, 238, 249, 255));\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    font: 75 12pt \"黑体\";\n"
"    color:#15589C;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(17, 100, 162, 255), stop:1 rgba(61, 140, 201, 255));\n"
"    border-style: inset;\n"
"    border-radius: 8px;\n"
"    font: 75 12pt \"黑体\";\n"
"    color:white;\n"
"    }")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_3.raise_()
        self.label_2.raise_()
        self.checkBox.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.userid.raise_()
        self.password.raise_()
        self.pushButton_2.raise_()
        self.pushButton_1.raise_()

        self.retranslateUi(login_ui)

    def retranslateUi(self, login_ui):
        _translate = QtCore.QCoreApplication.translate
        login_ui.setWindowTitle(_translate("login_ui", "登录"))
        self.label_2.setText(_translate("login_ui", "<html><head/><body><p><span style=\" color:#5676a2;\">密     码：</span></p></body></html>"))
        self.checkBox.setText(_translate("login_ui", "记住账号"))
        self.label.setText(_translate("login_ui", "<html><head/><body><p><span style=\" color:#5676a2;\">用户名：</span></p></body></html>"))
        self.pushButton_2.setText(_translate("login_ui", "重置"))
        self.pushButton_1.setText(_translate("login_ui", "登录"))

from .import resources_rc
