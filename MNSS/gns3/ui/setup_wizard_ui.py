# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/setup_wizard.ui'
#
# Created: Thu May  5 16:41:20 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupWizard(object):
    def setupUi(self, SetupWizard):
        SetupWizard.setObjectName("SetupWizard")
        SetupWizard.resize(775, 539)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetupWizard.sizePolicy().hasHeightForWidth())
        SetupWizard.setSizePolicy(sizePolicy)
        SetupWizard.setMaximumSize(QtCore.QSize(775, 563))
        SetupWizard.setModal(True)
        SetupWizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        SetupWizard.setOptions(QtWidgets.QWizard.NoBackButtonOnStartPage)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerWizardPage)
        self.uiVMRadioButton.setChecked(True)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.gridLayout.addWidget(self.uiVMRadioButton, 0, 0, 1, 1)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerWizardPage)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.gridLayout.addWidget(self.uiLocalRadioButton, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.uiShowCheckBox = QtWidgets.QCheckBox(self.uiServerWizardPage)
        self.uiShowCheckBox.setChecked(True)
        self.uiShowCheckBox.setObjectName("uiShowCheckBox")
        self.gridLayout.addWidget(self.uiShowCheckBox, 3, 0, 1, 1)
        SetupWizard.addPage(self.uiServerWizardPage)
        self.uiVMWizardPage = QtWidgets.QWizardPage()
        self.uiVMWizardPage.setObjectName("uiVMWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiVMWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiVirtualizationSoftwarLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiVirtualizationSoftwarLabel.setObjectName("uiVirtualizationSoftwarLabel")
        self.verticalLayout.addWidget(self.uiVirtualizationSoftwarLabel)
        self.uiVmwareRadioButton = QtWidgets.QRadioButton(self.uiVMWizardPage)
        self.uiVmwareRadioButton.setChecked(True)
        self.uiVmwareRadioButton.setObjectName("uiVmwareRadioButton")
        self.verticalLayout.addWidget(self.uiVmwareRadioButton)
        self.uiVirtualBoxRadioButton = QtWidgets.QRadioButton(self.uiVMWizardPage)
        self.uiVirtualBoxRadioButton.setObjectName("uiVirtualBoxRadioButton")
        self.verticalLayout.addWidget(self.uiVirtualBoxRadioButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.uiVMwareBannerButton = QtWidgets.QPushButton(self.uiVMWizardPage)
        self.uiVMwareBannerButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/vmware_fusion_banner.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.uiVMwareBannerButton.setIcon(icon)
        self.uiVMwareBannerButton.setIconSize(QtCore.QSize(454, 150))
        self.uiVMwareBannerButton.setFlat(True)
        self.uiVMwareBannerButton.setObjectName("uiVMwareBannerButton")
        self.horizontalLayout_2.addWidget(self.uiVMwareBannerButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.uiGNS3VMDownloadLinkUrlLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiGNS3VMDownloadLinkUrlLabel.setOpenExternalLinks(True)
        self.uiGNS3VMDownloadLinkUrlLabel.setObjectName("uiGNS3VMDownloadLinkUrlLabel")
        self.verticalLayout_2.addWidget(self.uiGNS3VMDownloadLinkUrlLabel)
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.verticalLayout_2.addWidget(self.uiVMNameLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiVMWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.horizontalLayout.addWidget(self.uiVMListComboBox)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiVMWizardPage)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.horizontalLayout.addWidget(self.uiRefreshPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.uiCPULabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiCPULabel.setObjectName("uiCPULabel")
        self.verticalLayout_2.addWidget(self.uiCPULabel)
        self.uiCPUSpinBox = QtWidgets.QSpinBox(self.uiVMWizardPage)
        self.uiCPUSpinBox.setMinimum(1)
        self.uiCPUSpinBox.setMaximum(128)
        self.uiCPUSpinBox.setProperty("value", 1)
        self.uiCPUSpinBox.setObjectName("uiCPUSpinBox")
        self.verticalLayout_2.addWidget(self.uiCPUSpinBox)
        self.uiRAMLabel = QtWidgets.QLabel(self.uiVMWizardPage)
        self.uiRAMLabel.setObjectName("uiRAMLabel")
        self.verticalLayout_2.addWidget(self.uiRAMLabel)
        self.uiRAMSpinBox = QtWidgets.QSpinBox(self.uiVMWizardPage)
        self.uiRAMSpinBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRAMSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRAMSpinBox.setSizePolicy(sizePolicy)
        self.uiRAMSpinBox.setMinimum(512)
        self.uiRAMSpinBox.setMaximum(1000000000)
        self.uiRAMSpinBox.setSingleStep(1024)
        self.uiRAMSpinBox.setProperty("value", 2048)
        self.uiRAMSpinBox.setObjectName("uiRAMSpinBox")
        self.verticalLayout_2.addWidget(self.uiRAMSpinBox)
        SetupWizard.addPage(self.uiVMWizardPage)
        self.uiAddVMsWizardPage = QtWidgets.QWizardPage()
        self.uiAddVMsWizardPage.setObjectName("uiAddVMsWizardPage")
        self.uiAddIOSRouterCheckBox = QtWidgets.QCheckBox(self.uiAddVMsWizardPage)
        self.uiAddIOSRouterCheckBox.setGeometry(QtCore.QRect(9, 9, 469, 22))
        self.uiAddIOSRouterCheckBox.setChecked(True)
        self.uiAddIOSRouterCheckBox.setObjectName("uiAddIOSRouterCheckBox")
        self.uiAddIOUDeviceCheckBox = QtWidgets.QCheckBox(self.uiAddVMsWizardPage)
        self.uiAddIOUDeviceCheckBox.setGeometry(QtCore.QRect(9, 37, 426, 22))
        self.uiAddIOUDeviceCheckBox.setObjectName("uiAddIOUDeviceCheckBox")
        self.uiAddQemuVMcheckBox = QtWidgets.QCheckBox(self.uiAddVMsWizardPage)
        self.uiAddQemuVMcheckBox.setGeometry(QtCore.QRect(9, 65, 219, 22))
        self.uiAddQemuVMcheckBox.setObjectName("uiAddQemuVMcheckBox")
        self.uiAddVirtualBoxVMcheckBox = QtWidgets.QCheckBox(self.uiAddVMsWizardPage)
        self.uiAddVirtualBoxVMcheckBox.setGeometry(QtCore.QRect(9, 93, 249, 22))
        self.uiAddVirtualBoxVMcheckBox.setObjectName("uiAddVirtualBoxVMcheckBox")
        self.uiAddVMwareVMcheckBox = QtWidgets.QCheckBox(self.uiAddVMsWizardPage)
        self.uiAddVMwareVMcheckBox.setGeometry(QtCore.QRect(9, 121, 233, 22))
        self.uiAddVMwareVMcheckBox.setObjectName("uiAddVMwareVMcheckBox")
        self.uiAddDockerVMCheckBox = QtWidgets.QCheckBox(self.uiAddVMsWizardPage)
        self.uiAddDockerVMCheckBox.setGeometry(QtCore.QRect(10, 150, 233, 22))
        self.uiAddDockerVMCheckBox.setObjectName("uiAddDockerVMCheckBox")
        SetupWizard.addPage(self.uiAddVMsWizardPage)

        self.retranslateUi(SetupWizard)
        QtCore.QMetaObject.connectSlotsByName(SetupWizard)

    def retranslateUi(self, SetupWizard):
        _translate = QtCore.QCoreApplication.translate
        SetupWizard.setWindowTitle(_translate("SetupWizard", "Setup Wizard"))
        self.uiServerWizardPage.setTitle(_translate("SetupWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("SetupWizard", "Please choose a server type to run your GNS3 network simulations. The GNS3 VM is strongly recommended on Windows and Mac OS X."))
        self.uiVMRadioButton.setToolTip(_translate("SetupWizard", "Dynamips, IOU, VPCS and Qemu will use this virtual machine."))
        self.uiVMRadioButton.setText(_translate("SetupWizard", "Local GNS3 VM"))
        self.uiLocalRadioButton.setToolTip(_translate("SetupWizard", "Eveything that is supported by your system will run on your computer."))
        self.uiLocalRadioButton.setText(_translate("SetupWizard", "Local server"))
        self.uiShowCheckBox.setText(_translate("SetupWizard", "Don\'t show this again"))
        self.uiVMWizardPage.setTitle(_translate("SetupWizard", "GNS3 VM"))
        self.uiVMWizardPage.setSubTitle(_translate("SetupWizard", "In order to run the GNS3 VM you must first have VMware or VirtualBox installed and the GNS3 VM.ova imported in one of these."))
        self.uiVirtualizationSoftwarLabel.setText(_translate("SetupWizard", "Virtualization software:"))
        self.uiVmwareRadioButton.setToolTip(_translate("SetupWizard", "VMware is recommended to run Qemu based appliances (required for KVM)."))
        self.uiVmwareRadioButton.setText(_translate("SetupWizard", "VMware (recommended)"))
        self.uiVirtualBoxRadioButton.setToolTip(_translate("SetupWizard", "Use VirtualBox if you intend to only use Dynamips, IOU or VPCS."))
        self.uiVirtualBoxRadioButton.setText(_translate("SetupWizard", "VirtualBox"))
        self.uiGNS3VMDownloadLinkUrlLabel.setText(_translate("SetupWizard", "<html><head/><body><p>The GNS3 VM can be <a href=\"https://github.com/GNS3/gns3-gui/releases/download/v1.4.1/GNS3.VM.VMware.Workstation.1.4.1.zip\"><span style=\" text-decoration: underline; color:#0000ff;\">downloaded here</span></a>. Import the VM in your virtualization software and hit refresh.</p></body></html>"))
        self.uiVMNameLabel.setText(_translate("SetupWizard", "VM name:"))
        self.uiRefreshPushButton.setText(_translate("SetupWizard", "&Refresh"))
        self.uiCPULabel.setText(_translate("SetupWizard", "vCPU cores:"))
        self.uiRAMLabel.setText(_translate("SetupWizard", "RAM size:"))
        self.uiRAMSpinBox.setSuffix(_translate("SetupWizard", " MB"))
        self.uiAddVMsWizardPage.setTitle(_translate("SetupWizard", "Add virtual machines"))
        self.uiAddVMsWizardPage.setSubTitle(_translate("SetupWizard", "Now that you have configured the server type you can choose to add one or more virtual machines (VMs) of different types."))
        self.uiAddIOSRouterCheckBox.setText(_translate("SetupWizard", "&Add an IOS router using a real IOS image (supported by Dynamips)"))
        self.uiAddIOUDeviceCheckBox.setText(_translate("SetupWizard", "&Add an IOU (IOS on UNIX) device using a L3 or L2 IOU image"))
        self.uiAddQemuVMcheckBox.setText(_translate("SetupWizard", "&Add a Qemu virtual machine"))
        self.uiAddVirtualBoxVMcheckBox.setText(_translate("SetupWizard", "&Add a VirtualBox virtual machine"))
        self.uiAddVMwareVMcheckBox.setText(_translate("SetupWizard", "&Add a VMware virtual machine"))
        self.uiAddDockerVMCheckBox.setText(_translate("SetupWizard", "&Add a Docker container"))

from . import resources_rc