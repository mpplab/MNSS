# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
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

"""
Configuration page for general preferences.
"""

import os
import shutil
import json

from gns3.qt import QtGui, QtCore, QtWidgets
from gns3.local_config import LocalConfig
from ..ui.general_preferences_page_ui import Ui_GeneralPreferencesPageWidget
from gns3.servers import Servers
from ..settings import GRAPHICS_VIEW_SETTINGS, GENERAL_SETTINGS, STYLES
from ..dialogs.console_command_dialog import ConsoleCommandDialog


class GeneralPreferencesPage(QtWidgets.QWidget, Ui_GeneralPreferencesPageWidget):

    """
    QWidget configuration page for general preferences.
    """

    def __init__(self, parent=None):

        super().__init__()
        self.setupUi(self)
        self._remote_servers = {}
        self._preferences_dialog = parent

        # Display the path of the config file
        config_file_path = LocalConfig.instance().configFilePath()
        self.uiConfigurationFileLabel.setText(config_file_path)

        self.uiProjectsPathToolButton.clicked.connect(self._projectsPathSlot)
        self.uiSymbolsPathToolButton.clicked.connect(self._symbolsPathSlot)
        self.uiImagesPathToolButton.clicked.connect(self._imagesPathSlot)
        self.uiConfigsPathToolButton.clicked.connect(self._configsPathSlot)
        self.uiImportConfigurationFilePushButton.clicked.connect(self._importConfigurationFileSlot)
        self.uiExportConfigurationFilePushButton.clicked.connect(self._exportConfigurationFileSlot)
        self.uiRestoreDefaultsPushButton.clicked.connect(self._restoreDefaultsSlot)
        self.uiTelnetConsolePreconfiguredCommandPushButton.clicked.connect(self._telnetConsolePreconfiguredCommandSlot)
        self.uiSerialConsolePreconfiguredCommandPushButton.clicked.connect(self._serialConsolePreconfiguredCommandSlot)
        self.uiVNCConsolePreconfiguredCommandPushButton.clicked.connect(self._vncConsolePreconfiguredCommandSlot)
        self.uiDefaultLabelFontPushButton.clicked.connect(self._setDefaultLabelFontSlot)
        self.uiDefaultLabelColorPushButton.clicked.connect(self._setDefaultLabelColorSlot)
        self.uiBrowseConfigurationPushButton.clicked.connect(self._browseConfigurationDirectorySlot)
        self._default_label_color = QtGui.QColor(QtCore.Qt.black)
        # self.uiStyleComboBox.addItems(STYLES)

        self.uiCloseConsoleWindowsOnDeleteCheckBox.hide()  # FIXME: not implemented
        self.uiBringConsoleWindowToFrontCheckBox.hide()  # FIXME: not implemented

    def _projectsPathSlot(self):
        """
        Slot to select the projects directory path.
        """

        servers = Servers.instance()
        local_server = servers.localServerSettings()
        directory = local_server["projects_path"]
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "My projects directory", directory, QtWidgets.QFileDialog.ShowDirsOnly)
        if path:
            self.uiProjectsPathLineEdit.setText(path)
            self.uiProjectsPathLineEdit.setCursorPosition(0)

    def _symbolsPathSlot(self):
        """
        Slot to select the symbols directory path.
        """

        servers = Servers.instance()
        local_server = servers.localServerSettings()
        directory = local_server["symbols_path"]
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "My symbols directory", directory, QtWidgets.QFileDialog.ShowDirsOnly)
        if path:
            self.uiSymbolsPathLineEdit.setText(path)
            self.uiSymbolsPathLineEdit.setCursorPosition(0)

    def _imagesPathSlot(self):
        """
        Slot to select the images directory path.
        """

        servers = Servers.instance()
        local_server = servers.localServerSettings()
        directory = local_server["images_path"]
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "My images directory", directory, QtWidgets.QFileDialog.ShowDirsOnly)
        if path:
            self.uiImagesPathLineEdit.setText(path)
            self.uiImagesPathLineEdit.setCursorPosition(0)

    def _configsPathSlot(self):
        """
        Slot to select the configs directory path.
        """

        servers = Servers.instance()
        local_server = servers.localServerSettings()
        directory = local_server["configs_path"]
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "My configs directory", directory, QtWidgets.QFileDialog.ShowDirsOnly)
        if path:
            self.uiConfigsPathLineEdit.setText(path)
            self.uiConfigsPathLineEdit.setCursorPosition(0)

    def _restoreDefaultsSlot(self):
        """
        Slot to restore default settings
        """

        self._populateGeneralSettingWidgets(GENERAL_SETTINGS)
        self._populateGraphicsViewSettingWidgets(GRAPHICS_VIEW_SETTINGS)

    def _telnetConsolePreconfiguredCommandSlot(self):
        """
        Slot to set a chosen pre-configured Telnet console command.
        """

        cmd = self.uiTelnetConsoleCommandLineEdit.text()
        (ok, cmd) = ConsoleCommandDialog.getCommand(self, console_type="telnet", current=cmd)
        if ok:
            self.uiTelnetConsoleCommandLineEdit.setText(cmd)

    def _serialConsolePreconfiguredCommandSlot(self):
        """
        Slot to set a chosen pre-configured serial console command.
        """

        cmd = self.uiSerialConsoleCommandLineEdit.text()
        (ok, cmd) = ConsoleCommandDialog.getCommand(self, console_type="serial", current=cmd)
        if ok:
            self.uiSerialConsoleCommandLineEdit.setText(cmd)

    def _vncConsolePreconfiguredCommandSlot(self):
        """
        Slot to set a chosen pre-configured VNC console command.
        """

        cmd = self.uiVNCConsoleCommandLineEdit.text()
        (ok, cmd) = ConsoleCommandDialog.getCommand(self, console_type="vnc", current=cmd)
        if ok:
            self.uiVNCConsoleCommandLineEdit.setText(cmd)

    def _importConfigurationFileSlot(self):
        """
        Slot to import a configuration file.
        """

        configuration_file_path = LocalConfig.instance().configFilePath()
        directory = os.path.dirname(configuration_file_path)

        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Import configuration file", directory, "Configuration file (*.ini *.conf);;All files (*.*)")
        if not path:
            return

        try:
            with open(path, encoding="utf-8") as f:
                config_file = json.load(f)
            if "type" not in config_file or config_file["type"] != "settings":
                QtWidgets.QMessageBox.critical(self, "Import configuration file", "Not a GNS3 configuration file: {}".format(path))
                return
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "Import configuration file", "Could not load configuration file {}: {}".format(os.path.basename(path), e))
            return
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Import configuration file", "Invalid file: {}".format(e))
            return

        try:
            shutil.copyfile(path, configuration_file_path)
        except (shutil.Error, IOError) as e:
            QtWidgets.QMessageBox.critical(self, "Import configuration file", "Cannot import configuration file: {}".format(e))
            return

        QtWidgets.QMessageBox.information(self, "Configuration file", "Configuration file imported, default settings will be applied after a restart")

        # TODO: implement restart
        # QtCore.QProcess.startDetached(QtWidgets.QApplication.arguments()[0], QtWidgets.QApplication.arguments())
        # QtWidgets.QApplication.quit()
        LocalConfig.instance().setConfigFilePath(configuration_file_path)
        self._preferences_dialog.reject()

    def _browseConfigurationDirectorySlot(self):
        """
        Slot to open a file browser into the configuration directory
        """
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("file://" + LocalConfig.configDirectory()))

    def _exportConfigurationFileSlot(self):
        """
        Slot to export a configuration file.
        """

        configuration_file_path = LocalConfig.instance().configFilePath()
        directory = os.path.dirname(configuration_file_path)

        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export configuration file", directory, "Configuration file (*.ini *.conf);;All files (*.*)")
        if not path:
            return

        try:
            shutil.copyfile(configuration_file_path, path)
        except (shutil.Error, IOError) as e:
            QtWidgets.QMessageBox.critical(self, "Export configuration file", "Cannot export configuration file: {}".format(e))
            return

    def _setDefaultLabelFontSlot(self):
        """
        Slot to select the default label font.
        """

        selected_font, ok = QtWidgets.QFontDialog.getFont(self.uiDefaultLabelStylePlainTextEdit.font(), self)
        if ok:
            self.uiDefaultLabelStylePlainTextEdit.setFont(selected_font)

    def _setDefaultLabelColorSlot(self):
        """
        Slot to select the default label color.
        """

        color = QtWidgets.QColorDialog.getColor(self._default_label_color, self)
        if color.isValid():
            self._default_label_color = color
            self.uiDefaultLabelStylePlainTextEdit.setStyleSheet("color : {}".format(color.name()))

    def _populateGeneralSettingWidgets(self, settings):
        """
        Populates the widgets with the settings.

        :param settings: General settings
        """

        local_server = Servers.instance().localServerSettings()
        self.uiProjectsPathLineEdit.setText(local_server["projects_path"])
        self.uiSymbolsPathLineEdit.setText(local_server["symbols_path"])
        self.uiImagesPathLineEdit.setText(local_server["images_path"])
        self.uiConfigsPathLineEdit.setText(local_server["configs_path"])
        self.uiStatsCheckBox.setChecked(settings["send_stats"])
        self.uiCrashReportCheckBox.setChecked(local_server["report_errors"])
        self.uiLaunchNewProjectDialogCheckBox.setChecked(settings["auto_launch_project_dialog"])
        self.uiAutoScreenshotCheckBox.setChecked(settings["auto_screenshot"])
        self.uiCheckForUpdateCheckBox.setChecked(settings["check_for_update"])
        self.uiLinkManualModeCheckBox.setChecked(settings["link_manual_mode"])
        self.uiExperimentalFeaturesCheckBox.setChecked(settings["experimental_features"])
        self.uiSlowStartAllSpinBox.setValue(settings["slow_device_start_all"])
        self.uiTelnetConsoleCommandLineEdit.setText(settings["telnet_console_command"])
        self.uiTelnetConsoleCommandLineEdit.setCursorPosition(0)
        # index = self.uiStyleComboBox.findText(settings["style"])
        # if index != -1:
        #     self.uiStyleComboBox.setCurrentIndex(index)
        self.uiSerialConsoleCommandLineEdit.setText(settings["serial_console_command"])
        self.uiSerialConsoleCommandLineEdit.setCursorPosition(0)
        self.uiCloseConsoleWindowsOnDeleteCheckBox.setChecked(settings["auto_close_console"])
        self.uiBringConsoleWindowToFrontCheckBox.setChecked(settings["bring_console_to_front"])
        self.uiDelayConsoleAllSpinBox.setValue(settings["delay_console_all"])

        self.uiVNCConsoleCommandLineEdit.setText(settings["vnc_console_command"])
        self.uiVNCConsoleCommandLineEdit.setCursorPosition(0)

    def _populateGraphicsViewSettingWidgets(self, settings):
        """
        Populates the widgets with the settings.

        :param settings: Graphics view settings
        """

        self.uiSceneWidthSpinBox.setValue(settings["scene_width"])
        self.uiSceneHeightSpinBox.setValue(settings["scene_height"])
        self.uiRectangleSelectedItemCheckBox.setChecked(settings["draw_rectangle_selected_item"])
        self.uiDrawLinkStatusPointsCheckBox.setChecked(settings["draw_link_status_points"])

        qt_font = QtGui.QFont()
        if qt_font.fromString(settings["default_label_font"]):
            self.uiDefaultLabelStylePlainTextEdit.setFont(qt_font)
        qt_color = QtGui.QColor(settings["default_label_color"])
        if qt_color.isValid():
            self._default_label_color = qt_color
            self.uiDefaultLabelStylePlainTextEdit.setStyleSheet("color : {}".format(qt_color.name()))

    def loadPreferences(self):
        """
        Loads the general preferences.
        """

        from ..main_window import MainWindow
        general_settings = MainWindow.instance().settings()
        self._populateGeneralSettingWidgets(general_settings)

        graphics_view_settings = MainWindow.instance().uiGraphicsView.settings()
        self._populateGraphicsViewSettingWidgets(graphics_view_settings)

    def savePreferences(self):
        """
        Saves the general preferences.
        """

        new_local_server_settings = {"images_path": self.uiImagesPathLineEdit.text(),
                                     "projects_path": self.uiProjectsPathLineEdit.text(),
                                     "symbols_path": self.uiSymbolsPathLineEdit.text(),
                                     "configs_path": self.uiConfigsPathLineEdit.text(),
                                     "report_errors": self.uiCrashReportCheckBox.isChecked()}
        Servers.instance().setLocalServerSettings(new_local_server_settings)

        new_general_settings = {"auto_launch_project_dialog": self.uiLaunchNewProjectDialogCheckBox.isChecked(),
                                "auto_screenshot": self.uiAutoScreenshotCheckBox.isChecked(),
                                "style": "Classic",
                                "experimental_features": self.uiExperimentalFeaturesCheckBox.isChecked(),
                                "check_for_update": self.uiCheckForUpdateCheckBox.isChecked(),
                                "link_manual_mode": self.uiLinkManualModeCheckBox.isChecked(),
                                "slow_device_start_all": self.uiSlowStartAllSpinBox.value(),
                                "telnet_console_command": self.uiTelnetConsoleCommandLineEdit.text(),
                                "serial_console_command": self.uiSerialConsoleCommandLineEdit.text(),
                                "vnc_console_command": self.uiVNCConsoleCommandLineEdit.text(),
                                "auto_close_console": self.uiCloseConsoleWindowsOnDeleteCheckBox.isChecked(),
                                "bring_console_to_front": self.uiBringConsoleWindowToFrontCheckBox.isChecked(),
                                "delay_console_all": self.uiDelayConsoleAllSpinBox.value(),
                                "send_stats": self.uiStatsCheckBox.isChecked()}

        from ..main_window import MainWindow
        MainWindow.instance().setSettings(new_general_settings)

        new_graphics_view_settings = {"scene_width": self.uiSceneWidthSpinBox.value(),
                                      "scene_height": self.uiSceneHeightSpinBox.value(),
                                      "draw_rectangle_selected_item": self.uiRectangleSelectedItemCheckBox.isChecked(),
                                      "draw_link_status_points": self.uiDrawLinkStatusPointsCheckBox.isChecked(),
                                      "default_label_font": self.uiDefaultLabelStylePlainTextEdit.font().toString(),
                                      "default_label_color": self._default_label_color.name()}
        MainWindow.instance().uiGraphicsView.setSettings(new_graphics_view_settings)
