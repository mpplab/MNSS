# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmware_vm_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VMwareVMWizard(object):
    def setupUi(self, VMwareVMWizard):
        VMwareVMWizard.setObjectName("VMwareVMWizard")
        VMwareVMWizard.resize(598, 453)
        VMwareVMWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout.addWidget(self.uiLocalRadioButton)
        self.gridLayout_2.addWidget(self.uiServerTypeGroupBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_8.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_8.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        VMwareVMWizard.addPage(self.uiServerWizardPage)
        self.uiVirtualBoxWizardPage = QtWidgets.QWizardPage()
        self.uiVirtualBoxWizardPage.setObjectName("uiVirtualBoxWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiVirtualBoxWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiVMListLabel = QtWidgets.QLabel(self.uiVirtualBoxWizardPage)
        self.uiVMListLabel.setObjectName("uiVMListLabel")
        self.gridLayout.addWidget(self.uiVMListLabel, 0, 0, 1, 1)
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiVirtualBoxWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.gridLayout.addWidget(self.uiVMListComboBox, 0, 1, 1, 1)
        self.uiBaseVMCheckBox = QtWidgets.QCheckBox(self.uiVirtualBoxWizardPage)
        self.uiBaseVMCheckBox.setEnabled(True)
        self.uiBaseVMCheckBox.setObjectName("uiBaseVMCheckBox")
        self.gridLayout.addWidget(self.uiBaseVMCheckBox, 1, 0, 1, 2)
        VMwareVMWizard.addPage(self.uiVirtualBoxWizardPage)

        self.retranslateUi(VMwareVMWizard)
        QtCore.QMetaObject.connectSlotsByName(VMwareVMWizard)

    def retranslateUi(self, VMwareVMWizard):
        _translate = QtCore.QCoreApplication.translate
        VMwareVMWizard.setWindowTitle(_translate("VMwareVMWizard", "新添医院信息系统及其他终端系统向导"))
        self.uiServerWizardPage.setTitle(_translate("VMwareVMWizard", "服务器"))
        self.uiServerWizardPage.setSubTitle(_translate("VMwareVMWizard", "请选择一种服务器类型来运行新的医院信息系统及其他终端系统。"))
        self.uiServerTypeGroupBox.setTitle(_translate("VMwareVMWizard", "服务器类别"))
        self.uiRemoteRadioButton.setText(_translate("VMwareVMWizard", "运行早远端电脑上的医院信息系统及其他终端系统"))
        self.uiLocalRadioButton.setText(_translate("VMwareVMWizard", "运行本地的医院信息系统及其他终端系统"))
        self.uiRemoteServersGroupBox.setTitle(_translate("VMwareVMWizard", "云端服务器"))
        self.uiRemoteServersLabel.setText(_translate("VMwareVMWizard", "路径："))
        self.uiVirtualBoxWizardPage.setTitle(_translate("VMwareVMWizard", "医院信息系统及其他终端系统"))
        self.uiVirtualBoxWizardPage.setSubTitle(_translate("VMwareVMWizard", "请从列表中选择一个医院信息系统及其他终端系统在VMware中实例化。"))
        self.uiVMListLabel.setText(_translate("VMwareVMWizard", "列表："))
        self.uiBaseVMCheckBox.setText(_translate("VMwareVMWizard", "用作链接的基础VM（实验）"))

