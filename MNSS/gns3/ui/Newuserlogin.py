# -*- coding: utf-8 -*-

"""
Module implementing NewDownload.
"""

from PyQt5.QtWidgets import QDialog
from gns3.qt import QtWidgets
from gns3.ui.Ui_userlogin import Ui_userlogin
 

class Newuserlogin(QDialog, Ui_userlogin):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Newuserlogin, self).__init__(parent)
        self.setupUi(self)
    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    dialog = Newuserlogin(main)
    dialog.show()
    exit_code = app.exec_()
        