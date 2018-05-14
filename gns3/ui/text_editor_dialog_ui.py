# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_editor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextEditorDialog(object):
    def setupUi(self, TextEditorDialog):
        TextEditorDialog.setObjectName("TextEditorDialog")
        TextEditorDialog.resize(457, 333)
        TextEditorDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(TextEditorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTextSettingsGroupBox = QtWidgets.QGroupBox(TextEditorDialog)
        self.uiTextSettingsGroupBox.setObjectName("uiTextSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiTextSettingsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiColorLabel = QtWidgets.QLabel(self.uiTextSettingsGroupBox)
        self.uiColorLabel.setObjectName("uiColorLabel")
        self.gridLayout.addWidget(self.uiColorLabel, 0, 0, 1, 1)
        self.uiColorPushButton = QtWidgets.QPushButton(self.uiTextSettingsGroupBox)
        self.uiColorPushButton.setText("")
        self.uiColorPushButton.setObjectName("uiColorPushButton")
        self.gridLayout.addWidget(self.uiColorPushButton, 0, 1, 1, 1)
        self.uiRotationLabel = QtWidgets.QLabel(self.uiTextSettingsGroupBox)
        self.uiRotationLabel.setObjectName("uiRotationLabel")
        self.gridLayout.addWidget(self.uiRotationLabel, 2, 0, 1, 1)
        self.uiRotationSpinBox = QtWidgets.QSpinBox(self.uiTextSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRotationSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRotationSpinBox.setSizePolicy(sizePolicy)
        self.uiRotationSpinBox.setMinimum(-360)
        self.uiRotationSpinBox.setMaximum(360)
        self.uiRotationSpinBox.setObjectName("uiRotationSpinBox")
        self.gridLayout.addWidget(self.uiRotationSpinBox, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.uiTextSettingsGroupBox)
        self.uiApplyColorToAllItemsCheckBox = QtWidgets.QCheckBox(TextEditorDialog)
        self.uiApplyColorToAllItemsCheckBox.setObjectName("uiApplyColorToAllItemsCheckBox")
        self.verticalLayout.addWidget(self.uiApplyColorToAllItemsCheckBox)
        self.uiApplyRotationToAllItemsCheckBox = QtWidgets.QCheckBox(TextEditorDialog)
        self.uiApplyRotationToAllItemsCheckBox.setObjectName("uiApplyRotationToAllItemsCheckBox")
        self.verticalLayout.addWidget(self.uiApplyRotationToAllItemsCheckBox)
        self.uiApplyTextToAllItemsCheckBox = QtWidgets.QCheckBox(TextEditorDialog)
        self.uiApplyTextToAllItemsCheckBox.setObjectName("uiApplyTextToAllItemsCheckBox")
        self.verticalLayout.addWidget(self.uiApplyTextToAllItemsCheckBox)
        self.uiPlainTextEdit = QtWidgets.QPlainTextEdit(TextEditorDialog)
        self.uiPlainTextEdit.setObjectName("uiPlainTextEdit")
        self.verticalLayout.addWidget(self.uiPlainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiFontPushButton = QtWidgets.QPushButton(TextEditorDialog)
        self.uiFontPushButton.setObjectName("uiFontPushButton")
        self.horizontalLayout.addWidget(self.uiFontPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(TextEditorDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(TextEditorDialog)
        self.uiButtonBox.accepted.connect(TextEditorDialog.accept)
        self.uiButtonBox.rejected.connect(TextEditorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TextEditorDialog)

    def retranslateUi(self, TextEditorDialog):
        _translate = QtCore.QCoreApplication.translate
        TextEditorDialog.setWindowTitle(_translate("TextEditorDialog", "文本编辑"))
        self.uiTextSettingsGroupBox.setTitle(_translate("TextEditorDialog", "文本属性设置"))
        self.uiColorLabel.setText(_translate("TextEditorDialog", "颜色："))
        self.uiRotationLabel.setText(_translate("TextEditorDialog", "旋转："))
        self.uiRotationSpinBox.setToolTip(_translate("TextEditorDialog", "Rotation can be ajusted on the scene for a selected item while\n"
"editing (notes only) with ALT and \'+\' (or P) / ALT and \'-\' (or M)"))
        self.uiRotationSpinBox.setSuffix(_translate("TextEditorDialog", "°"))
        self.uiApplyColorToAllItemsCheckBox.setText(_translate("TextEditorDialog", "将颜色应用到所有选中的项目"))
        self.uiApplyRotationToAllItemsCheckBox.setText(_translate("TextEditorDialog", "将旋转应用到所有选定的项目"))
        self.uiApplyTextToAllItemsCheckBox.setText(_translate("TextEditorDialog", "将下面的文本应用到所有选定的项目"))
        self.uiFontPushButton.setText(_translate("TextEditorDialog", "选择字体"))

from .import resources_rc
