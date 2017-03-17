# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userlogin_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userlogin(object):
    def setupUi(self, Ui_userlogin):
        Ui_userlogin.setObjectName("Ui_userlogin")
        Ui_userlogin.resize(300, 350)
        Ui_userlogin.setMinimumSize(QtCore.QSize(300, 350))
        Ui_userlogin.setMaximumSize(QtCore.QSize(300, 350))
        Ui_userlogin.setSizeGripEnabled(True)
        self.pushButton_2 = QtWidgets.QPushButton(Ui_userlogin)
        self.pushButton_2.setGeometry(QtCore.QRect(25, 170, 100, 28))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-width: 1px;\n"
"    background-color: white;\n"
"    border-color: rgb(171,168,165);\n"
"    border-style: outset;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(240,240,240);\n"
"    border-style: inset;\n"
"    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Ui_userlogin)
        self.pushButton_3.setGeometry(QtCore.QRect(175, 170, 100, 28))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border-width: 1px;\n"
"    background-color: white;\n"
"    border-color: rgb(171,168,165);\n"
"    border-style: outset;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(240,240,240);\n"
"    border-style: inset;\n"
"    }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Ui_userlogin)
        self.pushButton_4.setGeometry(QtCore.QRect(25, 230, 100, 28))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border-width: 1px;\n"
"    background-color: white;\n"
"    border-color: rgb(171,168,165);\n"
"    border-style: outset;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(240,240,240);\n"
"    border-style: inset;\n"
"    }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Ui_userlogin)
        self.pushButton_5.setGeometry(QtCore.QRect(175, 230, 100, 28))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    border-width: 1px;\n"
"    background-color: white;\n"
"    border-color: rgb(171,168,165);\n"
"    border-style: outset;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(240,240,240);\n"
"    border-style: inset;\n"
"    }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.username = QtWidgets.QLabel(Ui_userlogin)
        self.username.setGeometry(QtCore.QRect(50, 85, 200, 15))
        self.username.setMinimumSize(QtCore.QSize(80, 0))
        self.username.setMaximumSize(QtCore.QSize(300, 16777215))
        self.username.setSizeIncrement(QtCore.QSize(80, 0))
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.inuseprogressBar = QtWidgets.QProgressBar(Ui_userlogin)
        self.inuseprogressBar.setGeometry(QtCore.QRect(70, 110, 160, 20))
        self.inuseprogressBar.setMinimumSize(QtCore.QSize(160, 20))
        self.inuseprogressBar.setMaximumSize(QtCore.QSize(160, 20))
        self.inuseprogressBar.setAutoFillBackground(False)
        self.inuseprogressBar.setStyleSheet("border-width: 1px;\n"
"background-color: rgb(85, 255, 0);")
        self.inuseprogressBar.setMinimum(0)
        self.inuseprogressBar.setMaximum(104856)
        self.inuseprogressBar.setProperty("value", 0)
        self.inuseprogressBar.setTextVisible(False)
        self.inuseprogressBar.setOrientation(QtCore.Qt.Horizontal)
        self.inuseprogressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.inuseprogressBar.setFormat("")
        self.inuseprogressBar.setObjectName("inuseprogressBar")
        self.inuselabel = QtWidgets.QLabel(Ui_userlogin)
        self.inuselabel.setGeometry(QtCore.QRect(110, 110, 80, 20))
        self.inuselabel.setMinimumSize(QtCore.QSize(80, 20))
        self.inuselabel.setMaximumSize(QtCore.QSize(80, 20))
        self.inuselabel.setObjectName("inuselabel")
        self.frame = QtWidgets.QFrame(Ui_userlogin)
        self.frame.setGeometry(QtCore.QRect(110, 0, 80, 80))
        self.frame.setStyleSheet("border-image: url(:/images/yonghu.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Ui_userlogin)

    def retranslateUi(self, Ui_userlogin):
        _translate = QtCore.QCoreApplication.translate
        Ui_userlogin.setWindowTitle(_translate("Ui_userlogin", "个人信息"))
        self.pushButton_2.setText(_translate("Ui_userlogin", "个人资料"))
        self.pushButton_3.setText(_translate("Ui_userlogin", "修改头像"))
        self.pushButton_4.setText(_translate("Ui_userlogin", "我的收藏"))
        self.pushButton_5.setText(_translate("Ui_userlogin", "我的拓扑"))
        self.username.setText(_translate("Ui_userlogin", "<html><head/><body><p align=\"center\">昵称</p></body></html>"))
        self.inuselabel.setText(_translate("Ui_userlogin", "<html><head/><body><p align=\"center\">0K/1G</p></body></html>"))

import resources_rc
