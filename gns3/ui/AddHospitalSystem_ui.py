# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddHospitalSystem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gns3.globalvar import GlobalVar
globalvar = GlobalVar()

class Ui_AddHospitalSystem(object):
    def setupUi(self, AddHospitalSystem):
        AddHospitalSystem.setObjectName("AddHospitalSystem")
        AddHospitalSystem.resize(404, 175)
        AddHospitalSystem.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddHospitalSystem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(AddHospitalSystem)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label = QtWidgets.QLabel(AddHospitalSystem)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(AddHospitalSystem)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(AddHospitalSystem)
        self.comboBox.setObjectName("comboBox")
        c = ["HIS","LIS","PACS"]
        for b in c:
            for a in globalvar.Gdictionary["{}".format(b)]:
                self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(AddHospitalSystem)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AddHospitalSystem)
        QtCore.QMetaObject.connectSlotsByName(AddHospitalSystem)

    def retranslateUi(self, AddHospitalSystem):
        _translate = QtCore.QCoreApplication.translate
        AddHospitalSystem.setWindowTitle(_translate("AddHospitalSystem", "医院信息系统安装向导"))
        self.pushButton_3.setText(_translate("AddHospitalSystem", "手动下载"))
        self.label.setText(_translate("AddHospitalSystem", "<html><head/><body><p align=\"center\">请选择需要下载的医院信息系统</p></body></html>"))
        self.label_2.setText(_translate("AddHospitalSystem", "医院信息系统："))
        self.comboBox.setItemText(0, _translate("AddHospitalSystem", "HIS"))
        self.comboBox.setItemText(1, _translate("AddHospitalSystem", "LIS"))
        self.comboBox.setItemText(2, _translate("AddHospitalSystem", "PACS"))
        n = 0
        c = ["HIS","LIS","PACS"]
        for a in c:
            for b in globalvar.Gdictionary["{}".format(a)]:
                self.comboBox.setItemText(n, _translate("AddHospitalSystem", "{}".format(b[:-4])))
                n = n + 1
            

