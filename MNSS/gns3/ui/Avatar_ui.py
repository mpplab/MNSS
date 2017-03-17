# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Avatar_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Avatar(object):
    def setupUi(self, Ui_Avatar):
        Ui_Avatar.setObjectName("Ui_Avatar")
        Ui_Avatar.resize(364, 410)
        Ui_Avatar.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(Ui_Avatar)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 125, 25))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/imageupdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Ui_Avatar)
        self.frame.setGeometry(QtCore.QRect(50, 60, 265, 265))
        self.frame.setStyleSheet("border-image: url(:/images/yonghu.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(Ui_Avatar)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 350, 90, 28))
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
        self.pushButton_4 = QtWidgets.QPushButton(Ui_Avatar)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 350, 90, 28))
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
        self.label = QtWidgets.QLabel(Ui_Avatar)
        self.label.setGeometry(QtCore.QRect(160, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ui_Avatar)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 191, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Ui_Avatar)

    def retranslateUi(self, Ui_Avatar):
        _translate = QtCore.QCoreApplication.translate
        Ui_Avatar.setWindowTitle(_translate("Ui_Avatar", "更换头像"))
        self.pushButton.setText(_translate("Ui_Avatar", "上传本地图片"))
        self.pushButton_3.setText(_translate("Ui_Avatar", "确定"))
        self.pushButton_4.setText(_translate("Ui_Avatar", "取消"))
        self.label.setText(_translate("Ui_Avatar", "<html><head/><body><p><span style=\" color:#808080;\">请选择图片文件</span></p></body></html>"))
        self.label_2.setText(_translate("Ui_Avatar", "<html><head/><body><p><span style=\" color:#808080;\">文件格式为JPG、PNG、GIF</span></p></body></html>"))

from .import resources_rc
