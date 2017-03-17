# -*- coding: utf-8 -*-

"""
Module implementing error.
"""


from PyQt5.QtWidgets import QDialog
from PyQt5 import  QtWidgets


from gns3.ui.error_ui import Ui_error


class error(QDialog, Ui_error):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(error, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.reject()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_error = QtWidgets.QDialog()
    ui = error()
    ui.show()
    sys.exit(app.exec_())


