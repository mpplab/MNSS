# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qemu_vm_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QemuVMWizard(object):
    def setupUi(self, QemuVMWizard):
        QemuVMWizard.setObjectName("QemuVMWizard")
        QemuVMWizard.resize(623, 417)
        QemuVMWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout_5.addWidget(self.uiRemoteRadioButton)
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.verticalLayout_5.addWidget(self.uiVMRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout_5.addWidget(self.uiLocalRadioButton)
        self.verticalLayout_3.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiRemoteServersGroupBox)
        QemuVMWizard.addPage(self.uiServerWizardPage)
        self.uiNameWizardPage = QtWidgets.QWizardPage()
        self.uiNameWizardPage.setObjectName("uiNameWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiNameWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiNameWizardPage)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiNameWizardPage)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiLegacyASACheckBox = QtWidgets.QCheckBox(self.uiNameWizardPage)
        self.uiLegacyASACheckBox.setObjectName("uiLegacyASACheckBox")
        self.gridLayout.addWidget(self.uiLegacyASACheckBox, 1, 0, 1, 2)
        QemuVMWizard.addPage(self.uiNameWizardPage)
        self.uiBinaryMemoryWizardPage = QtWidgets.QWizardPage()
        self.uiBinaryMemoryWizardPage.setObjectName("uiBinaryMemoryWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiBinaryMemoryWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiQemuListLabel = QtWidgets.QLabel(self.uiBinaryMemoryWizardPage)
        self.uiQemuListLabel.setObjectName("uiQemuListLabel")
        self.gridLayout_2.addWidget(self.uiQemuListLabel, 0, 0, 1, 1)
        self.uiQemuListComboBox = QtWidgets.QComboBox(self.uiBinaryMemoryWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuListComboBox.sizePolicy().hasHeightForWidth())
        self.uiQemuListComboBox.setSizePolicy(sizePolicy)
        self.uiQemuListComboBox.setObjectName("uiQemuListComboBox")
        self.gridLayout_2.addWidget(self.uiQemuListComboBox, 0, 1, 1, 1)
        self.uiRamLabel = QtWidgets.QLabel(self.uiBinaryMemoryWizardPage)
        self.uiRamLabel.setObjectName("uiRamLabel")
        self.gridLayout_2.addWidget(self.uiRamLabel, 1, 0, 1, 1)
        self.uiRamSpinBox = QtWidgets.QSpinBox(self.uiBinaryMemoryWizardPage)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setProperty("value", 256)
        self.uiRamSpinBox.setObjectName("uiRamSpinBox")
        self.gridLayout_2.addWidget(self.uiRamSpinBox, 1, 1, 1, 1)
        QemuVMWizard.addPage(self.uiBinaryMemoryWizardPage)
        self.uiDiskWizardPage = QtWidgets.QWizardPage()
        self.uiDiskWizardPage.setObjectName("uiDiskWizardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiDiskWizardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiHdaDiskExistingImageRadioButton = QtWidgets.QRadioButton(self.uiDiskWizardPage)
        self.uiHdaDiskExistingImageRadioButton.setChecked(True)
        self.uiHdaDiskExistingImageRadioButton.setObjectName("uiHdaDiskExistingImageRadioButton")
        self.horizontalLayout_3.addWidget(self.uiHdaDiskExistingImageRadioButton)
        self.uiNewImageRadioButton_2 = QtWidgets.QRadioButton(self.uiDiskWizardPage)
        self.uiNewImageRadioButton_2.setChecked(False)
        self.uiNewImageRadioButton_2.setObjectName("uiNewImageRadioButton_2")
        self.horizontalLayout_3.addWidget(self.uiNewImageRadioButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiHdaDiskImageLabel = QtWidgets.QLabel(self.uiDiskWizardPage)
        self.uiHdaDiskImageLabel.setObjectName("uiHdaDiskImageLabel")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageLabel)
        self.uiHdaDiskImageListComboBox = QtWidgets.QComboBox(self.uiDiskWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiHdaDiskImageListComboBox.sizePolicy().hasHeightForWidth())
        self.uiHdaDiskImageListComboBox.setSizePolicy(sizePolicy)
        self.uiHdaDiskImageListComboBox.setObjectName("uiHdaDiskImageListComboBox")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageListComboBox)
        self.uiHdaDiskImageLineEdit = QtWidgets.QLineEdit(self.uiDiskWizardPage)
        self.uiHdaDiskImageLineEdit.setObjectName("uiHdaDiskImageLineEdit")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageLineEdit)
        self.uiHdaDiskImageToolButton = QtWidgets.QToolButton(self.uiDiskWizardPage)
        self.uiHdaDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdaDiskImageToolButton.setObjectName("uiHdaDiskImageToolButton")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageToolButton)
        self.uiHdaDiskImageCreateToolButton = QtWidgets.QToolButton(self.uiDiskWizardPage)
        self.uiHdaDiskImageCreateToolButton.setObjectName("uiHdaDiskImageCreateToolButton")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageCreateToolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        QemuVMWizard.addPage(self.uiDiskWizardPage)
        self.uiInitrdKernelImageWizardPage = QtWidgets.QWizardPage()
        self.uiInitrdKernelImageWizardPage.setObjectName("uiInitrdKernelImageWizardPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiInitrdKernelImageWizardPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiLinuxExistingImageRadioButton = QtWidgets.QRadioButton(self.uiInitrdKernelImageWizardPage)
        self.uiLinuxExistingImageRadioButton.setChecked(True)
        self.uiLinuxExistingImageRadioButton.setObjectName("uiLinuxExistingImageRadioButton")
        self.horizontalLayout_7.addWidget(self.uiLinuxExistingImageRadioButton)
        self.uiNewImageRadioButton_4 = QtWidgets.QRadioButton(self.uiInitrdKernelImageWizardPage)
        self.uiNewImageRadioButton_4.setChecked(False)
        self.uiNewImageRadioButton_4.setObjectName("uiNewImageRadioButton_4")
        self.horizontalLayout_7.addWidget(self.uiNewImageRadioButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.uiInitrdImageListComboBox = QtWidgets.QComboBox(self.uiInitrdKernelImageWizardPage)
        self.uiInitrdImageListComboBox.setObjectName("uiInitrdImageListComboBox")
        self.horizontalLayout_11.addWidget(self.uiInitrdImageListComboBox)
        self.uiInitrdImageLineEdit = QtWidgets.QLineEdit(self.uiInitrdKernelImageWizardPage)
        self.uiInitrdImageLineEdit.setObjectName("uiInitrdImageLineEdit")
        self.horizontalLayout_11.addWidget(self.uiInitrdImageLineEdit)
        self.uiInitrdImageToolButton = QtWidgets.QToolButton(self.uiInitrdKernelImageWizardPage)
        self.uiInitrdImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiInitrdImageToolButton.setObjectName("uiInitrdImageToolButton")
        self.horizontalLayout_11.addWidget(self.uiInitrdImageToolButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.uiKernelImageLabel = QtWidgets.QLabel(self.uiInitrdKernelImageWizardPage)
        self.uiKernelImageLabel.setObjectName("uiKernelImageLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiKernelImageLabel)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.uiKernelImageListComboBox = QtWidgets.QComboBox(self.uiInitrdKernelImageWizardPage)
        self.uiKernelImageListComboBox.setObjectName("uiKernelImageListComboBox")
        self.horizontalLayout_14.addWidget(self.uiKernelImageListComboBox)
        self.uiKernelImageLineEdit = QtWidgets.QLineEdit(self.uiInitrdKernelImageWizardPage)
        self.uiKernelImageLineEdit.setObjectName("uiKernelImageLineEdit")
        self.horizontalLayout_14.addWidget(self.uiKernelImageLineEdit)
        self.uiKernelImageToolButton = QtWidgets.QToolButton(self.uiInitrdKernelImageWizardPage)
        self.uiKernelImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiKernelImageToolButton.setObjectName("uiKernelImageToolButton")
        self.horizontalLayout_14.addWidget(self.uiKernelImageToolButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.uiInitrdLabel = QtWidgets.QLabel(self.uiInitrdKernelImageWizardPage)
        self.uiInitrdLabel.setObjectName("uiInitrdLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiInitrdLabel)
        self.gridLayout_4.addLayout(self.formLayout_2, 1, 0, 1, 1)
        QemuVMWizard.addPage(self.uiInitrdKernelImageWizardPage)

        self.retranslateUi(QemuVMWizard)
        QtCore.QMetaObject.connectSlotsByName(QemuVMWizard)
        QemuVMWizard.setTabOrder(self.uiNameLineEdit, self.uiQemuListComboBox)
        QemuVMWizard.setTabOrder(self.uiQemuListComboBox, self.uiRamSpinBox)
        QemuVMWizard.setTabOrder(self.uiRamSpinBox, self.uiHdaDiskImageLineEdit)
        QemuVMWizard.setTabOrder(self.uiHdaDiskImageLineEdit, self.uiHdaDiskImageToolButton)

    def retranslateUi(self, QemuVMWizard):
        _translate = QtCore.QCoreApplication.translate
        QemuVMWizard.setWindowTitle(_translate("QemuVMWizard", "创建QEMU VM模板"))
        self.uiServerWizardPage.setTitle(_translate("QemuVMWizard", "服务器"))
        self.uiServerWizardPage.setSubTitle(_translate("QemuVMWizard", "请选择服务器类型来运行你的新QEMU虚拟机。"))
        self.uiServerTypeGroupBox.setTitle(_translate("QemuVMWizard", "服务器类型"))
        self.uiRemoteRadioButton.setText(_translate("QemuVMWizard", "运行云端服务器上的Qemu VM"))
        self.uiVMRadioButton.setText(_translate("QemuVMWizard", "运行GNS3 Vm上的Qemy VM"))
        self.uiLocalRadioButton.setText(_translate("QemuVMWizard", "运行本地服务器上的Qemu VM"))
        self.uiRemoteServersGroupBox.setTitle(_translate("QemuVMWizard", "云端服务器"))
        self.uiRemoteServersLabel.setText(_translate("QemuVMWizard", "路径："))
        self.uiNameWizardPage.setTitle(_translate("QemuVMWizard", "QEMU VM名称"))
        self.uiNameWizardPage.setSubTitle(_translate("QemuVMWizard", "请选择您的新QEMU虚拟机一个描述性名称。"))
        self.uiNameLabel.setText(_translate("QemuVMWizard", "名称："))
        self.uiLegacyASACheckBox.setText(_translate("QemuVMWizard", "这是一ge ASA的虚拟机"))
        self.uiBinaryMemoryWizardPage.setTitle(_translate("QemuVMWizard", "QEMU镜像与内存"))
        self.uiBinaryMemoryWizardPage.setSubTitle(_translate("QemuVMWizard", "请检查QEMU二进制是正确设置和虚拟机有足够的内存来工作。 "))
        self.uiQemuListLabel.setText(_translate("QemuVMWizard", "镜像文件："))
        self.uiRamLabel.setText(_translate("QemuVMWizard", "RAM:"))
        self.uiRamSpinBox.setSuffix(_translate("QemuVMWizard", " MB"))
        self.uiDiskWizardPage.setTitle(_translate("QemuVMWizard", "磁盘镜像"))
        self.uiDiskWizardPage.setSubTitle(_translate("QemuVMWizard", "请为虚拟机选择一个基本磁盘映像。"))
        self.uiHdaDiskExistingImageRadioButton.setText(_translate("QemuVMWizard", "导入的镜像"))
        self.uiNewImageRadioButton_2.setText(_translate("QemuVMWizard", "新的镜像"))
        self.uiHdaDiskImageLabel.setText(_translate("QemuVMWizard", "磁盘镜像："))
        self.uiHdaDiskImageToolButton.setText(_translate("QemuVMWizard", "  浏览  "))
        self.uiHdaDiskImageCreateToolButton.setText(_translate("QemuVMWizard", "  创建  "))
        self.uiInitrdKernelImageWizardPage.setTitle(_translate("QemuVMWizard", "Linux启动特异性参数"))
        self.uiInitrdKernelImageWizardPage.setSubTitle(_translate("QemuVMWizard", "请选择一个initrd和内核镜像。"))
        self.uiLinuxExistingImageRadioButton.setText(_translate("QemuVMWizard", "导入的镜像"))
        self.uiNewImageRadioButton_4.setText(_translate("QemuVMWizard", "新的镜像"))
        self.uiInitrdImageToolButton.setText(_translate("QemuVMWizard", "  浏览  "))
        self.uiKernelImageLabel.setText(_translate("QemuVMWizard", "内核（vmlinuz）："))
        self.uiKernelImageToolButton.setText(_translate("QemuVMWizard", "  浏览  "))
        self.uiInitrdLabel.setText(_translate("QemuVMWizard", "初始化内存盘（initrd）："))

