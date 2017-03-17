# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from gns3.qt import QtWidgets
from gns3.ui.file_editor_dialog_ui import Ui_FileEditorDialog

import logging
log = logging.getLogger(__name__)


class FileEditorDialog(QtWidgets.QDialog, Ui_FileEditorDialog):
    """
    This dialog allow user to detect error in his GNS3 installation.

    If you want to add a test add a method starting by check. The
    check return a tuple result and a message in case of failure.
    """

    def __init__(self, node, path, parent=None):

        if parent is None:
            from gns3.main_window import MainWindow
            parent = MainWindow.instance()

        super().__init__(parent)
        self.setupUi(self)

        self._node = node
        self._path = path

        self.setWindowTitle(node.name() + " " + os.path.basename(path))

        self.uiRefreshButton.pressed.connect(self._refreshSlot)
        self.accepted.connect(self._acceptedCallback)

        self._refreshSlot()

    def _acceptedCallback(self):
        text = self.uiFileTextEdit.toPlainText()
        self._node.httpPost("/files" + self._path, None, body=text)

    def _refreshSlot(self):
        self._node.httpGet("/files" + self._path, self._getCallback)

    def _getCallback(self, result, error=False, raw_body=None, **kwargs):
        if not error:
            self.uiFileTextEdit.setText(raw_body)
