# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_error(object):
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(331, 177)
        error.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(error)
        self.label.setGeometry(QtCore.QRect(110, 40, 111, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(error)
        self.pushButton.setGeometry(QtCore.QRect(220, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "教程"))
        self.label.setText(_translate("error", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#808080;\">暂无教程！</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("error", "<html><head/><body><p>QPushButton{</p><p>    border-width: 1px;</p><p>    background-color: white;</p><p>    border-color: rgb(171,168,165);</p><p>    border-style: outset;</p><p>    }</p><p><br/></p><p>QPushButton:pressed {</p><p>    background-color: rgb(240,240,240);</p><p>    border-style: inset;</p><p>    }</p></body></html>"))
        self.pushButton.setText(_translate("error", "返回"))

