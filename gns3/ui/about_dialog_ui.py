# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        AboutDialog.resize(442, 371)
        self.gridLayout_2 = QtWidgets.QGridLayout(AboutDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiLogoLabel = QtWidgets.QLabel(self.tab)
        self.uiLogoLabel.setMinimumSize(QtCore.QSize(400, 200))
        self.uiLogoLabel.setStyleSheet("border-image: url(:/images/MNSS.png);")
        self.uiLogoLabel.setText("")
        self.uiLogoLabel.setObjectName("uiLogoLabel")
        self.verticalLayout_2.addWidget(self.uiLogoLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.uiAboutTextLabel = QtWidgets.QLabel(self.tab)
        self.uiAboutTextLabel.setOpenExternalLinks(True)
        self.uiAboutTextLabel.setObjectName("uiAboutTextLabel")
        self.verticalLayout_2.addWidget(self.uiAboutTextLabel)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTeamTextEdit = QtWidgets.QTextEdit(self.tab_4)
        self.uiTeamTextEdit.setReadOnly(True)
        self.uiTeamTextEdit.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.uiTeamTextEdit.setObjectName("uiTeamTextEdit")
        self.verticalLayout.addWidget(self.uiTeamTextEdit)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.vboxlayout.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "关于"))
        self.uiAboutTextLabel.setText(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:16pt; font-weight:600;\">MNSS %VERSION%</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:16pt; font-weight:600;\">Under GPL v3 license</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:16pt; font-weight:600;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AboutDialog", "MNSS版本"))
        self.uiTeamTextEdit.setHtml(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">    经过课题组多年的研究与积淀，医学网络系统仿真软件</span>MNSS<span style=\" font-family:\'宋体\';\">的功能和生态不断完善，各个功能模块得到多项课题资助，并积累了一定的知识产权，其中</span><span style=\" font-family:\'宋体\'; font-weight:600;\">医学信息模块</span><span style=\" font-family:\'宋体\';\">得到江苏省现代教育技术研究重点项目《面向医学信息学的虚拟网络实验平台的开发研究》的资助（</span>2012<span style=\" font-family:\'宋体\';\">年）；</span><span style=\" font-family:\'宋体\'; font-weight:600;\">云端资源分配模块</span><span style=\" font-family:\'宋体\';\">得到江苏省现代教育技术研究重点项目《基于</span>ELM<span style=\" font-family:\'宋体\';\">的分布式医学虚拟网络实验平台的开发研究与设计》的资助（</span>2016<span style=\" font-family:\'宋体\';\">年）；</span><span style=\" font-family:\'宋体\'; font-weight:600;\">安全存储模块</span><span style=\" font-family:\'宋体\';\">获得软件著作权</span>2<span style=\" font-family:\'宋体\';\">项：《医学隐私保护安全云存储系统》（软著登字第</span>1845816<span style=\" font-family:\'宋体\';\">号，</span>2017SR260532<span style=\" font-family:\'宋体\';\">），《医学隐私保护安全云存储管理控制端》（软著登字第</span>1845812<span style=\" font-family:\'宋体\';\">号，</span>2017SR260528<span style=\" font-family:\'宋体\';\">）；</span><span style=\" font-family:\'宋体\'; font-weight:600;\">云端调度服务模块</span><span style=\" font-family:\'宋体\';\">获得发明专利</span>2<span style=\" font-family:\'宋体\';\">项：《一种基于状态机实现访问控制的云平台服务方法及系统》（发明专利号：</span>ZL201610551889.1<span style=\" font-family:\'宋体\';\">），《一种分布式集群负载均衡并行调度系统及方法》（发明专利号：</span>ZL201610480848.8<span style=\" font-family:\'宋体\';\">）；</span><span style=\" font-family:\'宋体\'; font-weight:600;\">隐私保护推荐系统模块</span><span style=\" font-family:\'宋体\';\">得到江苏省现代教育技术研究重点项目《面向个性化学习推荐系统的差分隐私模型研究及其在</span>MNSS<span style=\" font-family:\'宋体\';\">中的应用》的资助（</span>2017<span style=\" font-family:\'宋体\';\">年）；</span><span style=\" font-family:\'宋体\'; font-weight:600;\">教学效果智能分析模块</span><span style=\" font-family:\'宋体\';\">获得软件著作权</span>2<span style=\" font-family:\'宋体\';\">项：《基于安全云的教育教学统计分析与智能决策系统》（软著登字第</span>1843400<span style=\" font-family:\'宋体\';\">号，</span>2017SR258116<span style=\" font-family:\'宋体\';\">），《基于安全云的教学管理通信系统》（软著登字第</span>1841494<span style=\" font-family:\'宋体\';\">号，</span>2017SR256210<span style=\" font-family:\'宋体\';\">）；</span><span style=\" font-family:\'宋体\'; font-weight:600;\">微教学模块</span><span style=\" font-family:\'宋体\';\">得到江苏省高校实验室研究会项目《面向</span>MNSS<span style=\" font-family:\'宋体\';\">的虚拟仿真实验微教学体系研究及系统开发》的资助（</span>2017<span style=\" font-family:\'宋体\';\">年）。</span> </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("AboutDialog", "关于我们"))
        self.textEdit_2.setHtml(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    iMNSS源自于2012年徐州医科大学构建的医学网络系统仿真软件<span style=\" font-weight:600;\">MNSS（Medical Network System Simulator）</span>，该软件在引入新的平台架构的基础上，整合了GNS3 GUI、Dynamips、Dynagen、QEMU、GNU Health、OpenLIS、OpenSourcePACS等众多优秀开源/底层软件，实现构建、设计和测试医院网络与系统的虚拟教学仿真环境，软件提供非常简单的方法来设计和模拟任何规模的网络架构，而不需要硬件。此外，由于该软件具有桥接到真实网络的功能，可以作为医院测试与部署新系统、完成网络改造、快速排查网络故障的有效工具，非常适合于医院的信息中心（信息科）使用。随后，基于MNSS不断MNSSware、MNSSexam、MNSSpaper等工具与系统，自2017年10月起上线iMNSS，作为众多工具与系统的统一入口。</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AboutDialog", "关于iMNSS"))
        self.textEdit.setHtml(_translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2012年3月：构建医学网络系统仿真软件MNSS。 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2014年5月：构建在线试题资源库MNSSexam。 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2017年2月：构建在线视频教育平台MNSSware。 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2017年5月：构建MNSSpaper，用于下载论文资源。 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2017年7月：构建医学信息工具库MNSStools。 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2017年9月：构建安全存储服务MNSSstorage。 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2017年10月：构建MNSS系列模块的统一门户iMNSS。 </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("AboutDialog", "iMNSS大事件"))

from .import resources_rc
