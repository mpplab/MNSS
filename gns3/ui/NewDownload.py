# -*- coding: utf-8 -*-

"""
Module implementing NewDownload.
"""

from PyQt5.QtWidgets import QDialog
from gns3.qt import QtWidgets
from gns3.ui.Download_ui import Ui_Download


class NewDownload(QDialog, Ui_Download):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(NewDownload, self).__init__(parent)
        self.setupUi(self)
        self.uiButtonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.reject)
        self.uiButtonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.reject)
        self.uiButtonBox.button(QtWidgets.QDialogButtonBox.Help).clicked.connect(self._helpButtonClickedSlot)
        
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
    dialog = NewDownload(main)
    dialog.show()
    exit_code = app.exec_()
        
