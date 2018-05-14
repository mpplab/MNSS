# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_ui(object):
    def setupUi(self, login_ui):
        login_ui.setObjectName("login_ui")
        login_ui.resize(555, 315)
        login_ui.setMinimumSize(QtCore.QSize(555, 315))
        login_ui.setMaximumSize(QtCore.QSize(555, 315))
        login_ui.setStyleSheet("")
        login_ui.setSizeGripEnabled(True)
        self.password_label = QtWidgets.QLabel(login_ui)
        self.password_label.setGeometry(QtCore.QRect(230, 160, 72, 16))
        self.password_label.setObjectName("password_label")
        self.checkBox = QtWidgets.QCheckBox(login_ui)
        self.checkBox.setGeometry(QtCore.QRect(400, 190, 91, 19))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("font: 12pt \"Agency FB\";\n"
"color: rgb(86, 118, 162);\n"
"text-decoration: underline;")
        self.checkBox.setObjectName("checkBox")
        self.username_label = QtWidgets.QLabel(login_ui)
        self.username_label.setGeometry(QtCore.QRect(230, 110, 72, 16))
        self.username_label.setObjectName("username_label")
        self.background = QtWidgets.QLabel(login_ui)
        self.background.setGeometry(QtCore.QRect(0, 0, 571, 361))
        self.background.setMinimumSize(QtCore.QSize(571, 361))
        self.background.setStyleSheet("background-image: url(:/images/background.png);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.logo_label = QtWidgets.QLabel(login_ui)
        self.logo_label.setGeometry(QtCore.QRect(40, 105, 160, 160))
        self.logo_label.setStyleSheet("border-image: url(:/images/MNSSlogo.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.username = QtWidgets.QLineEdit(login_ui)
        self.username.setGeometry(QtCore.QRect(300, 106, 181, 24))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(login_ui)
        self.password.setGeometry(QtCore.QRect(300, 154, 181, 24))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.reset_button = QtWidgets.QPushButton(login_ui)
        self.reset_button.setGeometry(QtCore.QRect(390, 230, 90, 30))
        self.reset_button.setStyleSheet("QPushButton{\n"
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
        self.reset_button.setObjectName("reset_button")
        self.login_button = QtWidgets.QPushButton(login_ui)
        self.login_button.setGeometry(QtCore.QRect(280, 230, 90, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton{\n"
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
        self.login_button.setObjectName("login_button")
        self.background.raise_()
        self.password_label.raise_()
        self.checkBox.raise_()
        self.username_label.raise_()
        self.logo_label.raise_()
        self.username.raise_()
        self.password.raise_()
        self.reset_button.raise_()
        self.login_button.raise_()

        self.retranslateUi(login_ui)
        QtCore.QMetaObject.connectSlotsByName(login_ui)

    def retranslateUi(self, login_ui):
        _translate = QtCore.QCoreApplication.translate
        login_ui.setWindowTitle(_translate("login_ui", "登录"))
        self.password_label.setText(_translate("login_ui", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#5676a2;\">密 码：</span></p></body></html>"))
        self.checkBox.setText(_translate("login_ui", "记住账号"))
        self.username_label.setText(_translate("login_ui", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#5676a2;\">用户名：</span></p></body></html>"))
        self.reset_button.setText(_translate("login_ui", "重置"))
        self.login_button.setText(_translate("login_ui", "登录"))

from .import resources_rc
