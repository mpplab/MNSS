# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsystem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Download(object):
    def setupUi(self, Download):
        Download.setObjectName("Download")
        Download.resize(426, 200)
        Download.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Download)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Download)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(Download)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout.addWidget(self.uiButtonBox)

        self.retranslateUi(Download)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Download)

    def retranslateUi(self, Download):
        _translate = QtCore.QCoreApplication.translate
        Download.setWindowTitle(_translate("Download", "系统镜像安装说明向导"))
        self.tabWidget.setToolTip(_translate("Download", "<html><head/><body><p>123132</p></body></html>"))
        self.label.setText(_translate("Download", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">请确保已安装VMware Workstation</span></p><p align=\"center\"><span style=\" font-size:18pt;\">版本仅支持12及以上</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Download", "第一步"))
        self.label_2.setText(_translate("Download", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">请手动添加</span></p><p align=\"center\"><span style=\" font-size:18pt;\">下载的医院信息系统及其他系统终端</span></p><p align=\"center\"><span style=\" font-size:18pt;\">至VMware Workstation.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Download", "第二步"))

