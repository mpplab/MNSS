# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/server_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerPreferencesPageWidget(object):
    def setupUi(self, ServerPreferencesPageWidget):
        ServerPreferencesPageWidget.setObjectName("ServerPreferencesPageWidget")
        ServerPreferencesPageWidget.resize(550, 606)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServerPreferencesPageWidget.sizePolicy().hasHeightForWidth())
        ServerPreferencesPageWidget.setSizePolicy(sizePolicy)
        ServerPreferencesPageWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ServerPreferencesPageWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiServerPreferenceTabWidget = QtWidgets.QTabWidget(ServerPreferencesPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerPreferenceTabWidget.sizePolicy().hasHeightForWidth())
        self.uiServerPreferenceTabWidget.setSizePolicy(sizePolicy)
        self.uiServerPreferenceTabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.uiServerPreferenceTabWidget.setObjectName("uiServerPreferenceTabWidget")
        self.uiLocalTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalTabWidget.sizePolicy().hasHeightForWidth())
        self.uiLocalTabWidget.setSizePolicy(sizePolicy)
        self.uiLocalTabWidget.setObjectName("uiLocalTabWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.uiLocalTabWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.uiGeneralSettingsGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiGeneralSettingsGroupBox.setObjectName("uiGeneralSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralSettingsGroupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout.addWidget(self.uiLocalServerPathLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout.addWidget(self.uiLocalServerToolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.uiUbridgePathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLabel.setObjectName("uiUbridgePathLabel")
        self.gridLayout.addWidget(self.uiUbridgePathLabel, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiUbridgePathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLineEdit.setObjectName("uiUbridgePathLineEdit")
        self.horizontalLayout_5.addWidget(self.uiUbridgePathLineEdit)
        self.uiUbridgeToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiUbridgeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiUbridgeToolButton.setObjectName("uiUbridgeToolButton")
        self.horizontalLayout_5.addWidget(self.uiUbridgeToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout.addWidget(self.uiLocalServerHostLabel, 5, 0, 1, 1)
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout.addWidget(self.uiLocalServerHostComboBox, 6, 0, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout.addWidget(self.uiLocalServerPortLabel, 7, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 3080)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout.addWidget(self.uiLocalServerPortSpinBox, 8, 0, 1, 1)
        self.uiConsoleConnectionsToAnyIPCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiConsoleConnectionsToAnyIPCheckBox.setObjectName("uiConsoleConnectionsToAnyIPCheckBox")
        self.gridLayout.addWidget(self.uiConsoleConnectionsToAnyIPCheckBox, 10, 0, 1, 1)
        self.uiLocalServerAuthCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerAuthCheckBox.setObjectName("uiLocalServerAuthCheckBox")
        self.gridLayout.addWidget(self.uiLocalServerAuthCheckBox, 9, 0, 1, 1)
        self.gridLayout_6.addWidget(self.uiGeneralSettingsGroupBox, 1, 0, 1, 2)
        self.uiLocalServerAutoStartCheckBox = QtWidgets.QCheckBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalServerAutoStartCheckBox.sizePolicy().hasHeightForWidth())
        self.uiLocalServerAutoStartCheckBox.setSizePolicy(sizePolicy)
        self.uiLocalServerAutoStartCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiLocalServerAutoStartCheckBox.setChecked(False)
        self.uiLocalServerAutoStartCheckBox.setObjectName("uiLocalServerAutoStartCheckBox")
        self.gridLayout_6.addWidget(self.uiLocalServerAutoStartCheckBox, 0, 0, 1, 1)
        self.uiConsolePortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName("uiConsolePortRangeGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiConsolePortRangeGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiConsoleStartPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(" TCP")
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2000)
        self.uiConsoleStartPortSpinBox.setObjectName("uiConsoleStartPortSpinBox")
        self.gridLayout_4.addWidget(self.uiConsoleStartPortSpinBox, 0, 0, 1, 1)
        self.uiConsolePortRangeLabel = QtWidgets.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName("uiConsolePortRangeLabel")
        self.gridLayout_4.addWidget(self.uiConsolePortRangeLabel, 0, 1, 1, 1)
        self.uiConsoleEndPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(" TCP")
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 5000)
        self.uiConsoleEndPortSpinBox.setObjectName("uiConsoleEndPortSpinBox")
        self.gridLayout_4.addWidget(self.uiConsoleEndPortSpinBox, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout_6.addWidget(self.uiConsolePortRangeGroupBox, 2, 0, 1, 2)
        self.uiUDPPortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName("uiUDPPortRangeGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiUDPStartPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(" UDP")
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10000)
        self.uiUDPStartPortSpinBox.setObjectName("uiUDPStartPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtWidgets.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName("uiUDPPortRangeLabel")
        self.horizontalLayout_8.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(" UDP")
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName("uiUDPEndPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout_6.addWidget(self.uiUDPPortRangeGroupBox, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 4, 0, 1, 1)
        self.uiGeneralSettingsGroupBox.raise_()
        self.uiConsolePortRangeGroupBox.raise_()
        self.uiUDPPortRangeGroupBox.raise_()
        self.uiLocalServerAutoStartCheckBox.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiLocalTabWidget, "")
        self.uiGNS3VMTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGNS3VMTabWidget.sizePolicy().hasHeightForWidth())
        self.uiGNS3VMTabWidget.setSizePolicy(sizePolicy)
        self.uiGNS3VMTabWidget.setObjectName("uiGNS3VMTabWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiGNS3VMTabWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiEnableVMCheckBox = QtWidgets.QCheckBox(self.uiGNS3VMTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEnableVMCheckBox.sizePolicy().hasHeightForWidth())
        self.uiEnableVMCheckBox.setSizePolicy(sizePolicy)
        self.uiEnableVMCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiEnableVMCheckBox.setChecked(False)
        self.uiEnableVMCheckBox.setObjectName("uiEnableVMCheckBox")
        self.verticalLayout.addWidget(self.uiEnableVMCheckBox)
        self.uiVirtualizationGroupBox = QtWidgets.QGroupBox(self.uiGNS3VMTabWidget)
        self.uiVirtualizationGroupBox.setObjectName("uiVirtualizationGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiVirtualizationGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiVmwareRadioButton = QtWidgets.QRadioButton(self.uiVirtualizationGroupBox)
        self.uiVmwareRadioButton.setChecked(False)
        self.uiVmwareRadioButton.setObjectName("uiVmwareRadioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(ServerPreferencesPageWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.uiVmwareRadioButton)
        self.gridLayout_7.addWidget(self.uiVmwareRadioButton, 0, 0, 1, 1)
        self.uiVirtualBoxRadioButton = QtWidgets.QRadioButton(self.uiVirtualizationGroupBox)
        self.uiVirtualBoxRadioButton.setObjectName("uiVirtualBoxRadioButton")
        self.buttonGroup.addButton(self.uiVirtualBoxRadioButton)
        self.gridLayout_7.addWidget(self.uiVirtualBoxRadioButton, 0, 1, 1, 1)
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiVirtualizationGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.buttonGroup.addButton(self.uiRemoteRadioButton)
        self.gridLayout_7.addWidget(self.uiRemoteRadioButton, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(166, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.uiVirtualizationGroupBox)
        self.uiLocalGNS3VMSettingsGroupBox = QtWidgets.QGroupBox(self.uiGNS3VMTabWidget)
        self.uiLocalGNS3VMSettingsGroupBox.setObjectName("uiLocalGNS3VMSettingsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiLocalGNS3VMSettingsGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiVMNameLabel = QtWidgets.QLabel(self.uiLocalGNS3VMSettingsGroupBox)
        self.uiVMNameLabel.setObjectName("uiVMNameLabel")
        self.gridLayout_2.addWidget(self.uiVMNameLabel, 0, 0, 1, 1)
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiLocalGNS3VMSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.gridLayout_2.addWidget(self.uiVMListComboBox, 0, 1, 1, 1)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiLocalGNS3VMSettingsGroupBox)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.gridLayout_2.addWidget(self.uiRefreshPushButton, 0, 2, 1, 1)
        self.uiHeadlessCheckBox = QtWidgets.QCheckBox(self.uiLocalGNS3VMSettingsGroupBox)
        self.uiHeadlessCheckBox.setObjectName("uiHeadlessCheckBox")
        self.gridLayout_2.addWidget(self.uiHeadlessCheckBox, 1, 0, 1, 2)
        self.uiShutdownCheckBox = QtWidgets.QCheckBox(self.uiLocalGNS3VMSettingsGroupBox)
        self.uiShutdownCheckBox.setObjectName("uiShutdownCheckBox")
        self.gridLayout_2.addWidget(self.uiShutdownCheckBox, 2, 0, 1, 2)
        self.uiAdjustLocalServerIPCheckBox = QtWidgets.QCheckBox(self.uiLocalGNS3VMSettingsGroupBox)
        self.uiAdjustLocalServerIPCheckBox.setObjectName("uiAdjustLocalServerIPCheckBox")
        self.gridLayout_2.addWidget(self.uiAdjustLocalServerIPCheckBox, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.uiLocalGNS3VMSettingsGroupBox)
        self.uiRemoteGNS3VMSettingsGroupBox = QtWidgets.QGroupBox(self.uiGNS3VMTabWidget)
        self.uiRemoteGNS3VMSettingsGroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.uiRemoteGNS3VMSettingsGroupBox.setFlat(False)
        self.uiRemoteGNS3VMSettingsGroupBox.setObjectName("uiRemoteGNS3VMSettingsGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.uiRemoteGNS3VMSettingsGroupBox)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.uiRemoteGNS3VMSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.uiServersComboBox = QtWidgets.QComboBox(self.uiRemoteGNS3VMSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiServersComboBox.setSizePolicy(sizePolicy)
        self.uiServersComboBox.setObjectName("uiServersComboBox")
        self.horizontalLayout_4.addWidget(self.uiServersComboBox)
        self.uiAddServerPushButton = QtWidgets.QPushButton(self.uiRemoteGNS3VMSettingsGroupBox)
        self.uiAddServerPushButton.setObjectName("uiAddServerPushButton")
        self.horizontalLayout_4.addWidget(self.uiAddServerPushButton)
        self.verticalLayout.addWidget(self.uiRemoteGNS3VMSettingsGroupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.uiServerPreferenceTabWidget.addTab(self.uiGNS3VMTabWidget, "")
        self.uiRemoteTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteTabWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteTabWidget.setSizePolicy(sizePolicy)
        self.uiRemoteTabWidget.setObjectName("uiRemoteTabWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiRemoteTabWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiRemoteServersTreeWidget = QtWidgets.QTreeWidget(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersTreeWidget.setSizePolicy(sizePolicy)
        self.uiRemoteServersTreeWidget.setColumnCount(4)
        self.uiRemoteServersTreeWidget.setObjectName("uiRemoteServersTreeWidget")
        self.uiRemoteServersTreeWidget.headerItem().setText(0, "Protocol")
        self.uiRemoteServersTreeWidget.headerItem().setText(1, "Host")
        self.uiRemoteServersTreeWidget.headerItem().setText(2, "Port")
        self.gridLayout_5.addWidget(self.uiRemoteServersTreeWidget, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAddRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiAddRemoteServerPushButton.setObjectName("uiAddRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiAddRemoteServerPushButton)
        self.uiDeleteRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiDeleteRemoteServerPushButton.setEnabled(False)
        self.uiDeleteRemoteServerPushButton.setObjectName("uiDeleteRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiDeleteRemoteServerPushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 2, 0, 1, 1)
        self.uiRemoteServersTreeWidget.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiRemoteTabWidget, "")
        self.verticalLayout_2.addWidget(self.uiServerPreferenceTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(ServerPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ServerPreferencesPageWidget)
        self.uiServerPreferenceTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ServerPreferencesPageWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiServerPreferenceTabWidget, self.uiLocalServerAutoStartCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAutoStartCheckBox, self.uiLocalServerPathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPathLineEdit, self.uiLocalServerToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerToolButton, self.uiUbridgePathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiUbridgePathLineEdit, self.uiUbridgeToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiUbridgeToolButton, self.uiLocalServerHostComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerHostComboBox, self.uiLocalServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPortSpinBox, self.uiLocalServerAuthCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAuthCheckBox, self.uiConsoleConnectionsToAnyIPCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleConnectionsToAnyIPCheckBox, self.uiConsoleStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleStartPortSpinBox, self.uiConsoleEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleEndPortSpinBox, self.uiUDPStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPStartPortSpinBox, self.uiUDPEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPEndPortSpinBox, self.uiRestoreDefaultsPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRestoreDefaultsPushButton, self.uiEnableVMCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiEnableVMCheckBox, self.uiHeadlessCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiHeadlessCheckBox, self.uiShutdownCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiShutdownCheckBox, self.uiRemoteServersTreeWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServersTreeWidget, self.uiAddRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiAddRemoteServerPushButton, self.uiDeleteRemoteServerPushButton)

    def retranslateUi(self, ServerPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        ServerPreferencesPageWidget.setWindowTitle(_translate("ServerPreferencesPageWidget", "Server"))
        self.uiGeneralSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "General settings"))
        self.uiLocalServerPathLabel.setText(_translate("ServerPreferencesPageWidget", "Server path:"))
        self.uiLocalServerToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiUbridgePathLabel.setText(_translate("ServerPreferencesPageWidget", "Ubridge path:"))
        self.uiUbridgeToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiConsoleConnectionsToAnyIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Allow console connections to any local IP address"))
        self.uiLocalServerAuthCheckBox.setText(_translate("ServerPreferencesPageWidget", "Protect server with password (recommended)"))
        self.uiLocalServerAutoStartCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable local server"))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Console port range (5900 => 6000 is shared with VNC)"))
        self.uiConsolePortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "UDP tunneling port range"))
        self.uiUDPPortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiLocalTabWidget), _translate("ServerPreferencesPageWidget", "Local server"))
        self.uiEnableVMCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable the GNS3 VM"))
        self.uiVirtualizationGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Virtualization software"))
        self.uiVmwareRadioButton.setToolTip(_translate("ServerPreferencesPageWidget", "VMware is recommended to run Qemu based appliances (required for KVM)."))
        self.uiVmwareRadioButton.setText(_translate("ServerPreferencesPageWidget", "VMware"))
        self.uiVirtualBoxRadioButton.setToolTip(_translate("ServerPreferencesPageWidget", "Use VirtualBox if you intend to run Dynamips, IOU or VPCS appliances."))
        self.uiVirtualBoxRadioButton.setText(_translate("ServerPreferencesPageWidget", "VirtualBox"))
        self.uiRemoteRadioButton.setToolTip(_translate("ServerPreferencesPageWidget", "Use remote if your VM is run on a remote server (e.g. ESXi or dedicated server)."))
        self.uiRemoteRadioButton.setText(_translate("ServerPreferencesPageWidget", "Remote"))
        self.uiLocalGNS3VMSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Local GNS3 VM"))
        self.uiVMNameLabel.setText(_translate("ServerPreferencesPageWidget", "VM name:"))
        self.uiRefreshPushButton.setText(_translate("ServerPreferencesPageWidget", "&Refresh"))
        self.uiHeadlessCheckBox.setText(_translate("ServerPreferencesPageWidget", "Start VM in headless mode"))
        self.uiShutdownCheckBox.setText(_translate("ServerPreferencesPageWidget", "ACPI shutdown VM when closing GNS3"))
        self.uiAdjustLocalServerIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Adjust the local server IP to be in the same subnet"))
        self.uiRemoteGNS3VMSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Remote GNS3 VM"))
        self.label.setText(_translate("ServerPreferencesPageWidget", "Server:"))
        self.uiAddServerPushButton.setText(_translate("ServerPreferencesPageWidget", "Add server"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiGNS3VMTabWidget), _translate("ServerPreferencesPageWidget", "GNS3 VM server"))
        self.uiRemoteServersTreeWidget.headerItem().setText(3, _translate("ServerPreferencesPageWidget", "User"))
        self.uiAddRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Add"))
        self.uiDeleteRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Delete"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiRemoteTabWidget), _translate("ServerPreferencesPageWidget", "Remote servers"))
        self.uiRestoreDefaultsPushButton.setText(_translate("ServerPreferencesPageWidget", "Restore defaults"))
