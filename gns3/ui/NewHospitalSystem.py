# -*- coding: utf-8 -*-

"""
Module implementing NewHospitalSystem.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from gns3.ui.AddHospitalSystem_ui import Ui_AddHospitalSystem
from ftplib import FTP
from PyQt5.QtWidgets import QMessageBox
from tkinter.filedialog import asksaveasfilename
import os
from tkinter import *
from tkinter import ttk
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QFileDialog  

class NewHospitalSystem(QDialog, Ui_AddHospitalSystem):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(NewHospitalSystem, self).__init__(parent)
        self.setupUi(self)
        self.uiButtonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self._okButtonClickedSlot)
        self.uiButtonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.reject)
        self.uiButtonBox.button(QtWidgets.QDialogButtonBox.Help).clicked.connect(self._helpButtonClickedSlot)
        
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.question(self,u'请访问以下地址',u'ftp://gns3@163.com:gns3**@139.196.202.32:428',QMessageBox.Yes , QMessageBox.No)
        
    def _okButtonClickedSlot(self):
        ftp = FTP()
        ftp.connect("139.196.202.32",428)
        ftp.login("gns3@163.com","gns3**")
#         print (ftp.getwelcome())
        x = str(self.comboBox.currentText())
        print(x)
        ftp.cwd('/MGNS/')
        if "HIS" in x:
            ftp.cwd("HIS")
        elif "LIS" in x:
            ftp.cwd("LIS")
        elif "PACS" in x:
            ftp.cwd("PACS")
        bufsize=1024
        root = Tk()
        root.title("请选择下载路径")
        filename="{}.ovf".format(x)
        fname = QFileDialog.getExistingDirectory(self,"请选择下载路径","C:/")
        try:
            os.chdir(fname)
            file_handle=open(filename,"wb").write
            ftp.retrbinary('RETR ' +  filename,file_handle,bufsize)
            ftp.dir()
        except OSError as e:
            print(e)
        ftp.close()
        root.destroy()
        self.rejected() 
               
    def _helpButtonClickedSlot(self):
        help_text = """<html><p>This dialog helps you to add an appliance template in GNS3. In all cases you must provide your own images.</p>
        <p>You can download appliance template files (.gns3appliance) from <a href="https://gns3.com/marketplace/appliances">the GNS3 website</a></p>
        <p>A template file provides community tested settings to run a specific appliance in GNS3.</p></html>
        """
        QtWidgets.QMessageBox.information(self, "Help for adding a new appliance template", help_text)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    dialog = NewHospitalSystem(main)
    dialog.show()
    exit_code = app.exec_()
