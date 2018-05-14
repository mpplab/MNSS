# -*- coding: utf-8 -*-

"""
Module implementing login.
"""

from PyQt5.QtWidgets import QDialog
from gns3.ui.newsystem_ui import Ui_Download


class docu(QDialog, Ui_Download):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(docu, self).__init__(parent)
        self.setupUi(self)
        self.uiButtonBox.accepted.connect(self.accept)
        self.uiButtonBox.rejected.connect(self.reject)