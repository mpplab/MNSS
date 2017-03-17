# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Download.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Download(object):
    def setupUi(self, Download):
        Download.setObjectName("Download")
        Download.resize(437, 322)
        Download.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Download)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Download)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 81))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 321, 81))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(Download)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout.addWidget(self.uiButtonBox)

        self.retranslateUi(Download)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Download)

    def retranslateUi(self, Download):
        _translate = QtCore.QCoreApplication.translate
        Download.setWindowTitle(_translate("Download", "请下载安装"))
        self.tabWidget.setToolTip(_translate("Download", "<html><head/><body><p>123132</p></body></html>"))
        self.label.setText(_translate("Download", "<html><head/><body><p>在安装医院信息系统之前，请确保已安装VMware Workstation.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Download", "第一步"))
        self.label_2.setText(_translate("Download", "<html><head/><body><p>请手动添加下载的医院信息系统至VMware Workstation.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Download", "第二步"))

