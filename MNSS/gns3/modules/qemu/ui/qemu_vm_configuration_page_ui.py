# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/qemu/ui/qemu_vm_configuration_page.ui'
#
# Created: Mon May 30 11:50:13 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QemuVMConfigPageWidget(object):
    def setupUi(self, QemuVMConfigPageWidget):
        QemuVMConfigPageWidget.setObjectName("QemuVMConfigPageWidget")
        QemuVMConfigPageWidget.resize(574, 523)
        self.verticalLayout = QtWidgets.QVBoxLayout(QemuVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiQemutabWidget = QtWidgets.QTabWidget(QemuVMConfigPageWidget)
        self.uiQemutabWidget.setObjectName("uiQemutabWidget")
        self.uiGeneralSettingsTab = QtWidgets.QWidget()
        self.uiGeneralSettingsTab.setObjectName("uiGeneralSettingsTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiGeneralSettingsTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiRamLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiRamLabel.setObjectName("uiRamLabel")
        self.gridLayout_4.addWidget(self.uiRamLabel, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsTab)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsTab)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsTab)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout_4.addWidget(self.uiCategoryComboBox, 3, 1, 1, 1)
        self.uiRamSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsTab)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setProperty("value", 256)
        self.uiRamSpinBox.setObjectName("uiRamSpinBox")
        self.gridLayout_4.addWidget(self.uiRamSpinBox, 4, 1, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout_4.addWidget(self.uiSymbolLabel, 2, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsTab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout_4.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiConsoleTypeComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsTab)
        self.uiConsoleTypeComboBox.setObjectName("uiConsoleTypeComboBox")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.gridLayout_4.addWidget(self.uiConsoleTypeComboBox, 8, 1, 1, 1)
        self.uiConsoleTypeLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiConsoleTypeLabel.setObjectName("uiConsoleTypeLabel")
        self.gridLayout_4.addWidget(self.uiConsoleTypeLabel, 8, 0, 1, 1)
        self.uiBootPriorityLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiBootPriorityLabel.setObjectName("uiBootPriorityLabel")
        self.gridLayout_4.addWidget(self.uiBootPriorityLabel, 7, 0, 1, 1)
        self.uiQemuListLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiQemuListLabel.setObjectName("uiQemuListLabel")
        self.gridLayout_4.addWidget(self.uiQemuListLabel, 6, 0, 1, 1)
        self.uiConsolePortLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiConsolePortLabel.setObjectName("uiConsolePortLabel")
        self.gridLayout_4.addWidget(self.uiConsolePortLabel, 9, 0, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout_4.addWidget(self.uiCategoryLabel, 3, 0, 1, 1)
        self.uiCPUSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsTab)
        self.uiCPUSpinBox.setMinimum(1)
        self.uiCPUSpinBox.setMaximum(255)
        self.uiCPUSpinBox.setObjectName("uiCPUSpinBox")
        self.gridLayout_4.addWidget(self.uiCPUSpinBox, 5, 1, 1, 1)
        self.uiConsolePortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsTab)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName("uiConsolePortSpinBox")
        self.gridLayout_4.addWidget(self.uiConsolePortSpinBox, 9, 1, 1, 1)
        self.uiBootPriorityComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsTab)
        self.uiBootPriorityComboBox.setObjectName("uiBootPriorityComboBox")
        self.gridLayout_4.addWidget(self.uiBootPriorityComboBox, 7, 1, 1, 1)
        self.uiNameLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout_4.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiQemuListComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuListComboBox.sizePolicy().hasHeightForWidth())
        self.uiQemuListComboBox.setSizePolicy(sizePolicy)
        self.uiQemuListComboBox.setObjectName("uiQemuListComboBox")
        self.gridLayout_4.addWidget(self.uiQemuListComboBox, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(263, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 10, 1, 1, 1)
        self.uiCPULabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiCPULabel.setObjectName("uiCPULabel")
        self.gridLayout_4.addWidget(self.uiCPULabel, 5, 0, 1, 1)
        self.uiDefaultNameFormatLabel = QtWidgets.QLabel(self.uiGeneralSettingsTab)
        self.uiDefaultNameFormatLabel.setObjectName("uiDefaultNameFormatLabel")
        self.gridLayout_4.addWidget(self.uiDefaultNameFormatLabel, 1, 0, 1, 1)
        self.uiDefaultNameFormatLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsTab)
        self.uiDefaultNameFormatLineEdit.setObjectName("uiDefaultNameFormatLineEdit")
        self.gridLayout_4.addWidget(self.uiDefaultNameFormatLineEdit, 1, 1, 1, 1)
        self.uiQemutabWidget.addTab(self.uiGeneralSettingsTab, "")
        self.uiHddTab = QtWidgets.QWidget()
        self.uiHddTab.setObjectName("uiHddTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiHddTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiHdaGroupBox = QtWidgets.QGroupBox(self.uiHddTab)
        self.uiHdaGroupBox.setObjectName("uiHdaGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.uiHdaGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.uiHdaDiskImageLabel = QtWidgets.QLabel(self.uiHdaGroupBox)
        self.uiHdaDiskImageLabel.setObjectName("uiHdaDiskImageLabel")
        self.gridLayout_6.addWidget(self.uiHdaDiskImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiHdaDiskImageLineEdit = QtWidgets.QLineEdit(self.uiHdaGroupBox)
        self.uiHdaDiskImageLineEdit.setObjectName("uiHdaDiskImageLineEdit")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageLineEdit)
        self.uiHdaDiskImageToolButton = QtWidgets.QToolButton(self.uiHdaGroupBox)
        self.uiHdaDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdaDiskImageToolButton.setObjectName("uiHdaDiskImageToolButton")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageToolButton)
        self.uiHdaDiskImageCreateToolButton = QtWidgets.QToolButton(self.uiHdaGroupBox)
        self.uiHdaDiskImageCreateToolButton.setObjectName("uiHdaDiskImageCreateToolButton")
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageCreateToolButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.uiHdaDiskInterfaceLabel = QtWidgets.QLabel(self.uiHdaGroupBox)
        self.uiHdaDiskInterfaceLabel.setObjectName("uiHdaDiskInterfaceLabel")
        self.gridLayout_6.addWidget(self.uiHdaDiskInterfaceLabel, 1, 0, 1, 1)
        self.uiHdaDiskInterfaceComboBox = QtWidgets.QComboBox(self.uiHdaGroupBox)
        self.uiHdaDiskInterfaceComboBox.setObjectName("uiHdaDiskInterfaceComboBox")
        self.gridLayout_6.addWidget(self.uiHdaDiskInterfaceComboBox, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiHdaGroupBox)
        self.uiHdbgroupBox = QtWidgets.QGroupBox(self.uiHddTab)
        self.uiHdbgroupBox.setObjectName("uiHdbgroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiHdbgroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiHdbDiskImageLabel = QtWidgets.QLabel(self.uiHdbgroupBox)
        self.uiHdbDiskImageLabel.setObjectName("uiHdbDiskImageLabel")
        self.gridLayout_7.addWidget(self.uiHdbDiskImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiHdbDiskImageLineEdit = QtWidgets.QLineEdit(self.uiHdbgroupBox)
        self.uiHdbDiskImageLineEdit.setObjectName("uiHdbDiskImageLineEdit")
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageLineEdit)
        self.uiHdbDiskImageToolButton = QtWidgets.QToolButton(self.uiHdbgroupBox)
        self.uiHdbDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdbDiskImageToolButton.setObjectName("uiHdbDiskImageToolButton")
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageToolButton)
        self.uiHdbDiskImageCreateToolButton = QtWidgets.QToolButton(self.uiHdbgroupBox)
        self.uiHdbDiskImageCreateToolButton.setObjectName("uiHdbDiskImageCreateToolButton")
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageCreateToolButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.uiHdbDiskInterfaceLabel = QtWidgets.QLabel(self.uiHdbgroupBox)
        self.uiHdbDiskInterfaceLabel.setObjectName("uiHdbDiskInterfaceLabel")
        self.gridLayout_7.addWidget(self.uiHdbDiskInterfaceLabel, 1, 0, 1, 1)
        self.uiHdbDiskInterfaceComboBox = QtWidgets.QComboBox(self.uiHdbgroupBox)
        self.uiHdbDiskInterfaceComboBox.setObjectName("uiHdbDiskInterfaceComboBox")
        self.gridLayout_7.addWidget(self.uiHdbDiskInterfaceComboBox, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiHdbgroupBox)
        self.uiHdcGroupBox = QtWidgets.QGroupBox(self.uiHddTab)
        self.uiHdcGroupBox.setObjectName("uiHdcGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.uiHdcGroupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.uiHdcDiskImageLabel = QtWidgets.QLabel(self.uiHdcGroupBox)
        self.uiHdcDiskImageLabel.setObjectName("uiHdcDiskImageLabel")
        self.gridLayout_8.addWidget(self.uiHdcDiskImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.uiHdcDiskImageLineEdit = QtWidgets.QLineEdit(self.uiHdcGroupBox)
        self.uiHdcDiskImageLineEdit.setObjectName("uiHdcDiskImageLineEdit")
        self.horizontalLayout_9.addWidget(self.uiHdcDiskImageLineEdit)
        self.uiHdcDiskImageToolButton = QtWidgets.QToolButton(self.uiHdcGroupBox)
        self.uiHdcDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdcDiskImageToolButton.setObjectName("uiHdcDiskImageToolButton")
        self.horizontalLayout_9.addWidget(self.uiHdcDiskImageToolButton)
        self.uiHdcDiskImageCreateToolButton = QtWidgets.QToolButton(self.uiHdcGroupBox)
        self.uiHdcDiskImageCreateToolButton.setObjectName("uiHdcDiskImageCreateToolButton")
        self.horizontalLayout_9.addWidget(self.uiHdcDiskImageCreateToolButton)
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.uiHdcDiskInterfaceLabel = QtWidgets.QLabel(self.uiHdcGroupBox)
        self.uiHdcDiskInterfaceLabel.setObjectName("uiHdcDiskInterfaceLabel")
        self.gridLayout_8.addWidget(self.uiHdcDiskInterfaceLabel, 1, 0, 1, 1)
        self.uiHdcDiskInterfaceComboBox = QtWidgets.QComboBox(self.uiHdcGroupBox)
        self.uiHdcDiskInterfaceComboBox.setObjectName("uiHdcDiskInterfaceComboBox")
        self.gridLayout_8.addWidget(self.uiHdcDiskInterfaceComboBox, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiHdcGroupBox)
        self.uiHddGroupBox = QtWidgets.QGroupBox(self.uiHddTab)
        self.uiHddGroupBox.setObjectName("uiHddGroupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.uiHddGroupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.uiHddDiskImageLabel = QtWidgets.QLabel(self.uiHddGroupBox)
        self.uiHddDiskImageLabel.setObjectName("uiHddDiskImageLabel")
        self.gridLayout_9.addWidget(self.uiHddDiskImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.uiHddDiskImageLineEdit = QtWidgets.QLineEdit(self.uiHddGroupBox)
        self.uiHddDiskImageLineEdit.setObjectName("uiHddDiskImageLineEdit")
        self.horizontalLayout_10.addWidget(self.uiHddDiskImageLineEdit)
        self.uiHddDiskImageToolButton = QtWidgets.QToolButton(self.uiHddGroupBox)
        self.uiHddDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHddDiskImageToolButton.setObjectName("uiHddDiskImageToolButton")
        self.horizontalLayout_10.addWidget(self.uiHddDiskImageToolButton)
        self.uiHddDiskImageCreateToolButton = QtWidgets.QToolButton(self.uiHddGroupBox)
        self.uiHddDiskImageCreateToolButton.setObjectName("uiHddDiskImageCreateToolButton")
        self.horizontalLayout_10.addWidget(self.uiHddDiskImageCreateToolButton)
        self.gridLayout_9.addLayout(self.horizontalLayout_10, 0, 1, 2, 1)
        self.uiHddDiskInterfaceLabel = QtWidgets.QLabel(self.uiHddGroupBox)
        self.uiHddDiskInterfaceLabel.setObjectName("uiHddDiskInterfaceLabel")
        self.gridLayout_9.addWidget(self.uiHddDiskInterfaceLabel, 1, 0, 2, 1)
        self.uiHddDiskInterfaceComboBox = QtWidgets.QComboBox(self.uiHddGroupBox)
        self.uiHddDiskInterfaceComboBox.setObjectName("uiHddDiskInterfaceComboBox")
        self.gridLayout_9.addWidget(self.uiHddDiskInterfaceComboBox, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiHddGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(438, 257, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.uiQemutabWidget.addTab(self.uiHddTab, "")
        self.uiCdromTab = QtWidgets.QWidget()
        self.uiCdromTab.setObjectName("uiCdromTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiCdromTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiCdromGroupBox = QtWidgets.QGroupBox(self.uiCdromTab)
        self.uiCdromGroupBox.setObjectName("uiCdromGroupBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.uiCdromGroupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.uiCdromImageLabel = QtWidgets.QLabel(self.uiCdromGroupBox)
        self.uiCdromImageLabel.setObjectName("uiCdromImageLabel")
        self.gridLayout_10.addWidget(self.uiCdromImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.uiCdromImageLineEdit = QtWidgets.QLineEdit(self.uiCdromGroupBox)
        self.uiCdromImageLineEdit.setObjectName("uiCdromImageLineEdit")
        self.horizontalLayout_11.addWidget(self.uiCdromImageLineEdit)
        self.uiCdromImageToolButton = QtWidgets.QToolButton(self.uiCdromGroupBox)
        self.uiCdromImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiCdromImageToolButton.setObjectName("uiCdromImageToolButton")
        self.horizontalLayout_11.addWidget(self.uiCdromImageToolButton)
        self.gridLayout_10.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.uiCdromGroupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 381, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.uiQemutabWidget.addTab(self.uiCdromTab, "")
        self.uiNetworkTab = QtWidgets.QWidget()
        self.uiNetworkTab.setObjectName("uiNetworkTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiNetworkTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiAdapterTypesComboBox = QtWidgets.QComboBox(self.uiNetworkTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdapterTypesComboBox.sizePolicy().hasHeightForWidth())
        self.uiAdapterTypesComboBox.setSizePolicy(sizePolicy)
        self.uiAdapterTypesComboBox.setObjectName("uiAdapterTypesComboBox")
        self.gridLayout_5.addWidget(self.uiAdapterTypesComboBox, 6, 1, 1, 1)
        self.uiLegacyNetworkingCheckBox = QtWidgets.QCheckBox(self.uiNetworkTab)
        self.uiLegacyNetworkingCheckBox.setObjectName("uiLegacyNetworkingCheckBox")
        self.gridLayout_5.addWidget(self.uiLegacyNetworkingCheckBox, 7, 0, 1, 2)
        self.uiMacAddrLineEdit = QtWidgets.QLineEdit(self.uiNetworkTab)
        self.uiMacAddrLineEdit.setObjectName("uiMacAddrLineEdit")
        self.gridLayout_5.addWidget(self.uiMacAddrLineEdit, 5, 1, 1, 1)
        self.uiPortSegmentSizeLabel = QtWidgets.QLabel(self.uiNetworkTab)
        self.uiPortSegmentSizeLabel.setObjectName("uiPortSegmentSizeLabel")
        self.gridLayout_5.addWidget(self.uiPortSegmentSizeLabel, 3, 0, 1, 1)
        self.uiAdapterTypesLabel = QtWidgets.QLabel(self.uiNetworkTab)
        self.uiAdapterTypesLabel.setObjectName("uiAdapterTypesLabel")
        self.gridLayout_5.addWidget(self.uiAdapterTypesLabel, 6, 0, 1, 1)
        self.uiPortSegmentSizeSpinBox = QtWidgets.QSpinBox(self.uiNetworkTab)
        self.uiPortSegmentSizeSpinBox.setMaximum(128)
        self.uiPortSegmentSizeSpinBox.setSingleStep(4)
        self.uiPortSegmentSizeSpinBox.setObjectName("uiPortSegmentSizeSpinBox")
        self.gridLayout_5.addWidget(self.uiPortSegmentSizeSpinBox, 3, 1, 1, 1)
        self.uiAdaptersLabel = QtWidgets.QLabel(self.uiNetworkTab)
        self.uiAdaptersLabel.setObjectName("uiAdaptersLabel")
        self.gridLayout_5.addWidget(self.uiAdaptersLabel, 0, 0, 1, 1)
        self.uiMacAddrLabel = QtWidgets.QLabel(self.uiNetworkTab)
        self.uiMacAddrLabel.setObjectName("uiMacAddrLabel")
        self.gridLayout_5.addWidget(self.uiMacAddrLabel, 5, 0, 1, 1)
        self.uiPortNameFormatLabel = QtWidgets.QLabel(self.uiNetworkTab)
        self.uiPortNameFormatLabel.setObjectName("uiPortNameFormatLabel")
        self.gridLayout_5.addWidget(self.uiPortNameFormatLabel, 2, 0, 1, 1)
        self.uiAdaptersSpinBox = QtWidgets.QSpinBox(self.uiNetworkTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdaptersSpinBox.sizePolicy().hasHeightForWidth())
        self.uiAdaptersSpinBox.setSizePolicy(sizePolicy)
        self.uiAdaptersSpinBox.setMinimum(0)
        self.uiAdaptersSpinBox.setMaximum(32)
        self.uiAdaptersSpinBox.setObjectName("uiAdaptersSpinBox")
        self.gridLayout_5.addWidget(self.uiAdaptersSpinBox, 0, 1, 1, 1)
        self.uiPortNameFormatLineEdit = QtWidgets.QLineEdit(self.uiNetworkTab)
        self.uiPortNameFormatLineEdit.setText("")
        self.uiPortNameFormatLineEdit.setObjectName("uiPortNameFormatLineEdit")
        self.gridLayout_5.addWidget(self.uiPortNameFormatLineEdit, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 261, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 8, 1, 1, 1)
        self.uiFirstPortNameLabel = QtWidgets.QLabel(self.uiNetworkTab)
        self.uiFirstPortNameLabel.setObjectName("uiFirstPortNameLabel")
        self.gridLayout_5.addWidget(self.uiFirstPortNameLabel, 1, 0, 1, 1)
        self.uiFirstPortNameLineEdit = QtWidgets.QLineEdit(self.uiNetworkTab)
        self.uiFirstPortNameLineEdit.setObjectName("uiFirstPortNameLineEdit")
        self.gridLayout_5.addWidget(self.uiFirstPortNameLineEdit, 1, 1, 1, 1)
        self.uiQemutabWidget.addTab(self.uiNetworkTab, "")
        self.uiAdvancedSettingsTab = QtWidgets.QWidget()
        self.uiAdvancedSettingsTab.setObjectName("uiAdvancedSettingsTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiAdvancedSettingsTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiLinuxBootGroupBox = QtWidgets.QGroupBox(self.uiAdvancedSettingsTab)
        self.uiLinuxBootGroupBox.setObjectName("uiLinuxBootGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiLinuxBootGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiKernelImageLineEdit = QtWidgets.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiKernelImageLineEdit.setObjectName("uiKernelImageLineEdit")
        self.gridLayout_2.addWidget(self.uiKernelImageLineEdit, 1, 1, 1, 1)
        self.uiKernelCommandLineLabel = QtWidgets.QLabel(self.uiLinuxBootGroupBox)
        self.uiKernelCommandLineLabel.setObjectName("uiKernelCommandLineLabel")
        self.gridLayout_2.addWidget(self.uiKernelCommandLineLabel, 2, 0, 1, 1)
        self.uiInitrdLabel = QtWidgets.QLabel(self.uiLinuxBootGroupBox)
        self.uiInitrdLabel.setObjectName("uiInitrdLabel")
        self.gridLayout_2.addWidget(self.uiInitrdLabel, 0, 0, 1, 1)
        self.uiKernelImageLabel = QtWidgets.QLabel(self.uiLinuxBootGroupBox)
        self.uiKernelImageLabel.setObjectName("uiKernelImageLabel")
        self.gridLayout_2.addWidget(self.uiKernelImageLabel, 1, 0, 1, 1)
        self.uiInitrdLineEdit = QtWidgets.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiInitrdLineEdit.setObjectName("uiInitrdLineEdit")
        self.gridLayout_2.addWidget(self.uiInitrdLineEdit, 0, 1, 1, 1)
        self.uiInitrdToolButton = QtWidgets.QToolButton(self.uiLinuxBootGroupBox)
        self.uiInitrdToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiInitrdToolButton.setObjectName("uiInitrdToolButton")
        self.gridLayout_2.addWidget(self.uiInitrdToolButton, 0, 2, 1, 1)
        self.uiKernelImageToolButton = QtWidgets.QToolButton(self.uiLinuxBootGroupBox)
        self.uiKernelImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiKernelImageToolButton.setObjectName("uiKernelImageToolButton")
        self.gridLayout_2.addWidget(self.uiKernelImageToolButton, 1, 2, 1, 1)
        self.uiKernelCommandLineEdit = QtWidgets.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiKernelCommandLineEdit.setObjectName("uiKernelCommandLineEdit")
        self.gridLayout_2.addWidget(self.uiKernelCommandLineEdit, 2, 1, 1, 2)
        self.verticalLayout_2.addWidget(self.uiLinuxBootGroupBox)
        self.uiOptimizationGroupBox = QtWidgets.QGroupBox(self.uiAdvancedSettingsTab)
        self.uiOptimizationGroupBox.setObjectName("uiOptimizationGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiOptimizationGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiActivateCPUThrottlingCheckBox = QtWidgets.QCheckBox(self.uiOptimizationGroupBox)
        self.uiActivateCPUThrottlingCheckBox.setChecked(True)
        self.uiActivateCPUThrottlingCheckBox.setObjectName("uiActivateCPUThrottlingCheckBox")
        self.gridLayout.addWidget(self.uiActivateCPUThrottlingCheckBox, 0, 0, 1, 2)
        self.uiCPUThrottlingLabel = QtWidgets.QLabel(self.uiOptimizationGroupBox)
        self.uiCPUThrottlingLabel.setObjectName("uiCPUThrottlingLabel")
        self.gridLayout.addWidget(self.uiCPUThrottlingLabel, 1, 0, 1, 1)
        self.uiCPUThrottlingSpinBox = QtWidgets.QSpinBox(self.uiOptimizationGroupBox)
        self.uiCPUThrottlingSpinBox.setMinimum(1)
        self.uiCPUThrottlingSpinBox.setMaximum(800)
        self.uiCPUThrottlingSpinBox.setProperty("value", 100)
        self.uiCPUThrottlingSpinBox.setObjectName("uiCPUThrottlingSpinBox")
        self.gridLayout.addWidget(self.uiCPUThrottlingSpinBox, 1, 1, 1, 1)
        self.uiProcessPriorityLabel = QtWidgets.QLabel(self.uiOptimizationGroupBox)
        self.uiProcessPriorityLabel.setObjectName("uiProcessPriorityLabel")
        self.gridLayout.addWidget(self.uiProcessPriorityLabel, 2, 0, 1, 1)
        self.uiProcessPriorityComboBox = QtWidgets.QComboBox(self.uiOptimizationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiProcessPriorityComboBox.sizePolicy().hasHeightForWidth())
        self.uiProcessPriorityComboBox.setSizePolicy(sizePolicy)
        self.uiProcessPriorityComboBox.setObjectName("uiProcessPriorityComboBox")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.uiProcessPriorityComboBox.addItem("")
        self.gridLayout.addWidget(self.uiProcessPriorityComboBox, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiOptimizationGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.uiAdvancedSettingsTab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiQemuOptionsLabel = QtWidgets.QLabel(self.groupBox)
        self.uiQemuOptionsLabel.setObjectName("uiQemuOptionsLabel")
        self.gridLayout_3.addWidget(self.uiQemuOptionsLabel, 0, 0, 1, 1)
        self.uiQemuOptionsLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiQemuOptionsLineEdit.setObjectName("uiQemuOptionsLineEdit")
        self.gridLayout_3.addWidget(self.uiQemuOptionsLineEdit, 0, 1, 1, 1)
        self.uiBaseVMCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.uiBaseVMCheckBox.setEnabled(True)
        self.uiBaseVMCheckBox.setObjectName("uiBaseVMCheckBox")
        self.gridLayout_3.addWidget(self.uiBaseVMCheckBox, 1, 0, 1, 2)
        self.uiACPIShutdownCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.uiACPIShutdownCheckBox.setObjectName("uiACPIShutdownCheckBox")
        self.gridLayout_3.addWidget(self.uiACPIShutdownCheckBox, 2, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.uiQemutabWidget.addTab(self.uiAdvancedSettingsTab, "")
        self.verticalLayout.addWidget(self.uiQemutabWidget)

        self.retranslateUi(QemuVMConfigPageWidget)
        self.uiQemutabWidget.setCurrentIndex(0)
        self.uiProcessPriorityComboBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(QemuVMConfigPageWidget)

    def retranslateUi(self, QemuVMConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        QemuVMConfigPageWidget.setWindowTitle(_translate("QemuVMConfigPageWidget", "QEMU VM configuration"))
        self.uiRamLabel.setText(_translate("QemuVMConfigPageWidget", "RAM:"))
        self.uiSymbolToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiRamSpinBox.setSuffix(_translate("QemuVMConfigPageWidget", " MB"))
        self.uiSymbolLabel.setText(_translate("QemuVMConfigPageWidget", "Symbol:"))
        self.uiConsoleTypeComboBox.setItemText(0, _translate("QemuVMConfigPageWidget", "telnet"))
        self.uiConsoleTypeComboBox.setItemText(1, _translate("QemuVMConfigPageWidget", "vnc"))
        self.uiConsoleTypeLabel.setText(_translate("QemuVMConfigPageWidget", "Console type:"))
        self.uiBootPriorityLabel.setText(_translate("QemuVMConfigPageWidget", "Boot priority:"))
        self.uiQemuListLabel.setText(_translate("QemuVMConfigPageWidget", "Qemu binary:"))
        self.uiConsolePortLabel.setText(_translate("QemuVMConfigPageWidget", "Console port:"))
        self.uiCategoryLabel.setText(_translate("QemuVMConfigPageWidget", "Category:"))
        self.uiNameLabel.setText(_translate("QemuVMConfigPageWidget", "Name:"))
        self.uiCPULabel.setText(_translate("QemuVMConfigPageWidget", "vCPUs:"))
        self.uiDefaultNameFormatLabel.setText(_translate("QemuVMConfigPageWidget", "Default name format:"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.uiGeneralSettingsTab), _translate("QemuVMConfigPageWidget", "General settings"))
        self.uiHdaGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "HDA (Primary Master)"))
        self.uiHdaDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image:"))
        self.uiHdaDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHdaDiskImageCreateToolButton.setText(_translate("QemuVMConfigPageWidget", "Create..."))
        self.uiHdaDiskInterfaceLabel.setText(_translate("QemuVMConfigPageWidget", "Disk interface:"))
        self.uiHdbgroupBox.setTitle(_translate("QemuVMConfigPageWidget", "HDB (Primary Slave)"))
        self.uiHdbDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image:"))
        self.uiHdbDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHdbDiskImageCreateToolButton.setText(_translate("QemuVMConfigPageWidget", "Create..."))
        self.uiHdbDiskInterfaceLabel.setText(_translate("QemuVMConfigPageWidget", "Disk interface:"))
        self.uiHdcGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "HDC (Secondary Master)"))
        self.uiHdcDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image:"))
        self.uiHdcDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHdcDiskImageCreateToolButton.setText(_translate("QemuVMConfigPageWidget", "Create..."))
        self.uiHdcDiskInterfaceLabel.setText(_translate("QemuVMConfigPageWidget", "Disk interface:"))
        self.uiHddGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "HDD (Secondary Slave)"))
        self.uiHddDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image:"))
        self.uiHddDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiHddDiskImageCreateToolButton.setText(_translate("QemuVMConfigPageWidget", "Create..."))
        self.uiHddDiskInterfaceLabel.setText(_translate("QemuVMConfigPageWidget", "Disk interface:"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.uiHddTab), _translate("QemuVMConfigPageWidget", "HDD"))
        self.uiCdromGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "CD/DVD-ROM"))
        self.uiCdromImageLabel.setText(_translate("QemuVMConfigPageWidget", "Image:"))
        self.uiCdromImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.uiCdromTab), _translate("QemuVMConfigPageWidget", "CD/DVD"))
        self.uiLegacyNetworkingCheckBox.setText(_translate("QemuVMConfigPageWidget", "Use the legacy networking mode"))
        self.uiPortSegmentSizeLabel.setText(_translate("QemuVMConfigPageWidget", "Segment size:"))
        self.uiAdapterTypesLabel.setText(_translate("QemuVMConfigPageWidget", "Type:"))
        self.uiAdaptersLabel.setText(_translate("QemuVMConfigPageWidget", "Adapters:"))
        self.uiMacAddrLabel.setText(_translate("QemuVMConfigPageWidget", "Base MAC:"))
        self.uiPortNameFormatLabel.setToolTip(_translate("QemuVMConfigPageWidget", "<html><head/><body><p>{0} - the port number, from 0 to the number of adapters-1.</p><p>{1} - the segment number, from 0 to the number of segments-1.</p><p>{port0} - named alias for {0}.</p><p>{port1} - the port number, from 1 to the number of adapters.</p><p>{segment0} - named alias for {1}.</p><p>{segment1} - the segment number, from 1 to the number of segments.</p></body></html>"))
        self.uiPortNameFormatLabel.setText(_translate("QemuVMConfigPageWidget", "Name format:"))
        self.uiFirstPortNameLabel.setText(_translate("QemuVMConfigPageWidget", "First port name:"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.uiNetworkTab), _translate("QemuVMConfigPageWidget", "Network"))
        self.uiLinuxBootGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "Linux boot specific settings"))
        self.uiKernelCommandLineLabel.setText(_translate("QemuVMConfigPageWidget", "Kernel command line:"))
        self.uiInitrdLabel.setText(_translate("QemuVMConfigPageWidget", "Initial RAM disk (initrd):"))
        self.uiKernelImageLabel.setText(_translate("QemuVMConfigPageWidget", "Kernel image:"))
        self.uiInitrdToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiKernelImageToolButton.setText(_translate("QemuVMConfigPageWidget", "&Browse..."))
        self.uiOptimizationGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "Optimizations"))
        self.uiActivateCPUThrottlingCheckBox.setText(_translate("QemuVMConfigPageWidget", "Activate CPU throttling"))
        self.uiCPUThrottlingLabel.setText(_translate("QemuVMConfigPageWidget", "Percentage of CPU allowed:"))
        self.uiCPUThrottlingSpinBox.setSuffix(_translate("QemuVMConfigPageWidget", " %"))
        self.uiProcessPriorityLabel.setText(_translate("QemuVMConfigPageWidget", "Process priority:"))
        self.uiProcessPriorityComboBox.setItemText(0, _translate("QemuVMConfigPageWidget", "Realtime"))
        self.uiProcessPriorityComboBox.setItemText(1, _translate("QemuVMConfigPageWidget", "Very high"))
        self.uiProcessPriorityComboBox.setItemText(2, _translate("QemuVMConfigPageWidget", "High"))
        self.uiProcessPriorityComboBox.setItemText(3, _translate("QemuVMConfigPageWidget", "Normal"))
        self.uiProcessPriorityComboBox.setItemText(4, _translate("QemuVMConfigPageWidget", "Low"))
        self.uiProcessPriorityComboBox.setItemText(5, _translate("QemuVMConfigPageWidget", "Very low"))
        self.groupBox.setTitle(_translate("QemuVMConfigPageWidget", "Additional settings"))
        self.uiQemuOptionsLabel.setText(_translate("QemuVMConfigPageWidget", "Options:"))
        self.uiBaseVMCheckBox.setText(_translate("QemuVMConfigPageWidget", "Use as a linked base VM"))
        self.uiACPIShutdownCheckBox.setText(_translate("QemuVMConfigPageWidget", "Enable ACPI shutdown (experimental)"))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.uiAdvancedSettingsTab), _translate("QemuVMConfigPageWidget", "Advanced settings"))
