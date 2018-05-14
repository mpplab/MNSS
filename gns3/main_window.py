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
Main window for the GUI.
"""

import traceback
import sys
import os
import time
import shutil
import json
import glob
import logging
import subprocess
import requests
import threading

from .local_config import LocalConfig
from .modules import MODULES
from .modules.module_error import ModuleError
from .modules.vpcs import VPCS
from .qt import QtGui, QtCore, QtWidgets, QtSvg
from .servers import Servers
from .gns3_vm import GNS3VM
from .node import Node
from .ui.main_window_ui import Ui_MainWindow
from .dialogs.about_dialog import AboutDialog
from .dialogs.new_project_dialog import NewProjectDialog
from .dialogs.preferences_dialog import PreferencesDialog
from .dialogs.snapshots_dialog import SnapshotsDialog
from .dialogs.export_debug_dialog import ExportDebugDialog
from .dialogs.doctor_dialog import DoctorDialog
from .dialogs.setup_wizard import SetupWizard
from .settings import GENERAL_SETTINGS
from .utils.progress_dialog import ProgressDialog
from .utils.process_files_worker import ProcessFilesWorker
from .utils.wait_for_connection_worker import WaitForConnectionWorker
from .utils.wait_for_vm_worker import WaitForVMWorker
from .utils.export_project_worker import ExportProjectWorker
from .utils.import_project_worker import ImportProjectWorker
from .utils.message_box import MessageBox
from .ports.port import Port
from .items.node_item import NodeItem
from .items.link_item import LinkItem
from .items.shape_item import ShapeItem
from .items.image_item import ImageItem
from .items.note_item import NoteItem
from .topology import Topology
from .project import Project
from .http_client import HTTPClient
from .progress import Progress
from .update_manager import UpdateManager
from .utils.analytics import AnalyticsClient
from .dialogs.appliance_wizard import ApplianceWizard
from .dialogs.new_appliance_dialog import NewApplianceDialog
from .registry.appliance import ApplianceError
from PyQt5.QtCore import Qt
from gns3.login import login
from PyQt5.QtGui import QPixmap
from gns3.globalvar import GlobalVar
from gns3.download import wget,newthreading
from gns3.document import docu
log = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    """
    Main window implementation.

    :param parent: parent widget
    """

    # signal to tell the view if the user is adding a link or not
    adding_link_signal = QtCore.pyqtSignal(bool)

    # signal to tell a new project was created
    project_new_signal = QtCore.pyqtSignal(str)

    # signal to tell the windows is ready to load his first project
    ready_signal = QtCore.pyqtSignal()

    # mouse move
    mousematch = True

    SUPPORTED_IMAGE_FORMATS = [
        "svg",
        "bmp",
        "jpeg",
        "jpg",
        "gif",
        "pbm",
        "pgm",
        "png",
        "ppm",
        "xbm",
        "xpm"
    ]

    def mousePressEvent(self, event):
        if self.mousematch == True:
            if event.button() == Qt.LeftButton:
                self.m_drag = True
                self.m_DragPosition = event.globalPos() - self.pos()
                event.accept()
        else:
            pass

    def mouseMoveEvent(self, QMouseEvent):
        if self.mousematch == True:
            if Qt.LeftButton and self.m_drag:
                self.move(QMouseEvent.globalPos() - self.m_DragPosition)
                QMouseEvent.accept()
        else:
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        if self.mousematch == True:
            self.m_drag = False
        else:
            pass

    def timerEvent(self, event):
        for i in GlobalVar.downloadobjectlist:
            i.progressbar.setValue(i.suspendsize)


    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.iconlogo.setStyleSheet("border-image: url(:/images/MNSS.ico);")
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        dialog = login(self)
        dialog.show()
        dialog.password.setStyleSheet("lineedit-password-character:42")
        dialog.exec_()
        from PyQt5.QtCore import QBasicTimer
        self.timer = QBasicTimer()
        self.timer.start(100,self)
        GlobalVar.area = self.scrollAreaWidgetContents
        try:
            with open('download.txt','r') as f:
                initdownload = eval(f.read())
                for i in initdownload.keys():
                    GlobalVar.nowurllist.add(i)
                    newpath = os.path.join(GlobalVar.iospath, i.split('/')[-1])
                    newmisstion = wget(i, initdownload[i], newpath, GlobalVar.area)
                    GlobalVar.downloadobjectlist.append(newmisstion)
                    newgame = newthreading(newmisstion)
                    # newgame = multiprocessing.Process(target=newmisstion.download)
                    newgame.start()
        except Exception as e:
            pass

            req = requests.get(GlobalVar.headportrait)
            photo = QPixmap()
            photo.loadFromData(req.content)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(photo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.uilogin.setIcon(icon)

        if GlobalVar.name == '':
            pass
        else:
            self.uilogin.setText(GlobalVar.name)

        self.judge()
        MainWindow._instance = self
        self._settings = {}
        HTTPClient.setProgressCallback(Progress.instance(self))

        self.uiShowTopology.setChecked(True)
        self.uiShowServer.setChecked(True)
        self.uiAddLinkAction.setCheckable(True)
        self.uiAddNoteAction.setCheckable(True)
        self.uiDrawEllipseAction.setCheckable(True)
        self.uiDrawRectangleAction.setCheckable(True)
        self.uiShowPortNamesAction.setCheckable(True)
        self.uiStartAllAction.setCheckable(True)
        self.uiSuspendAllAction.setCheckable(True)
        self.uiStopAllAction.setCheckable(True)
        self.uiMaximumAction.setCheckable(True)

        self._project = None
        self._createTemporaryProject()
        self._first_file_load = True
        self._loadSettings()
        self._connections()
        self._ignore_unsaved_state = False
        self._max_recent_files = 5
        self._soft_exit = True
        self._project_dialog = None
        # self._recent_file_actions = []
        self._start_time = time.time()
        local_config = LocalConfig.instance()
        local_config.config_changed_signal.connect(self._localConfigChangedSlot)
        self._local_config_timer = QtCore.QTimer(self)
        self._local_config_timer.timeout.connect(local_config.checkConfigChanged)
        self._local_config_timer.start(1000)  # milliseconds
        self._analytics_client = AnalyticsClient()

        # restore the geometry and state of the main window.
        self.restoreGeometry(QtCore.QByteArray().fromBase64(self._settings["geometry"].encode()))
        self.restoreState(QtCore.QByteArray().fromBase64(self._settings["state"].encode()))

        # populate the view -> docks menu
        # self.uiDocksMenu.addAction(self.uiTopologySummaryDockWidget.toggleViewAction())
        # self.uiDocksMenu.addAction(self.uiServerSummaryDockWidget.toggleViewAction())
        # self.uiDocksMenu.addAction(self.uiConsoleDockWidget.toggleViewAction())
        # self.uiDocksMenu.addAction(self.uiNodesDockWidget.toggleViewAction())
        # Make sure the dock widget is not open
        self.uiNodesDockWidget.setVisible(False)

        # default directories for QFileDialog
        self._import_configs_from_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DocumentsLocation)
        self._export_configs_to_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DocumentsLocation)
        self._screenshots_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.PicturesLocation)
        self._pictures_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.PicturesLocation)

        # add recent file actions to the File menu
        # for i in range(0, self._max_recent_files):
        #     action = QtWidgets.QAction(self.uiFileMenu)
        #     action.setVisible(False)
        #     action.triggered.connect(self.openRecentFileSlot)
        #     self._recent_file_actions.append(action)
        # self.uiFileMenu.insertActions(self.uiQuitAction, self._recent_file_actions)
        # self._recent_file_actions_separator = self.uiFileMenu.insertSeparator(self.uiQuitAction)
        # self._recent_file_actions_separator.setVisible(False)
        # self._updateRecentFileActions()

        # set the window icon
        self.setWindowIcon(QtGui.QIcon(":/images/MNSS.ico"))

        # restore the style
        self._setStyle(self._settings.get("style"))

        if self._settings["hide_new_appliance_template_button"]:
            self.uiNewAppliancePushButton.hide()

        getpath = LocalConfig()
        GlobalVar.path = getpath._settings["Servers"]["local_server"]["images_path"]

        # self.setWindowTitle("[*] GNS3")

        # load initial stuff once the event loop isn't busy
        self.run_later(0, self.startupLoading)

    def judge(self):
        if GlobalVar.loginmark == True:
            pass
        else:
            sys.exit(0)

    def _loadSettings(self):
        """
        Loads the settings from the persistent settings file.
        """

        local_config = LocalConfig.instance()
        self._settings = local_config.loadSectionSettings(self.__class__.__name__, GENERAL_SETTINGS)

        # restore packet capture settings
        Port.loadPacketCaptureSettings()

    def settings(self):
        """
        Returns the general settings.

        :returns: settings dictionary
        """

        return self._settings

    def setSettings(self, new_settings):
        """
        Set new general settings.

        :param new_settings: settings dictionary
        """

        # change the GUI style
        style = new_settings.get("style")
        if style and new_settings["style"] != self._settings["style"]:
            if not self._setStyle(style):
                self._setLegacyStyle()

        self._settings.update(new_settings)
        # save the settings
        LocalConfig.instance().saveSectionSettings(self.__class__.__name__, self._settings)

    def setSoftExit(self, softExit):
        """If True warn user before exiting app if unsaved data"""
        self._soft_exit = softExit

    def _connections(self):
        """
        Connect widgets to slots
        """

        self.uiShowTopology.clicked.connect(lambda: self._showdockwidget(1))
        self.uiShowServer.clicked.connect(lambda: self._showdockwidget(2))

        # file menu connections
        self.uiNewProjectAction.clicked.connect(self._newProjectActionSlot)
        self.uiOpenProjectAction.clicked.connect(self.openProjectActionSlot)
        self.uiSaveProjectAsAction.clicked.connect(self._saveProjectAsActionSlot)
        self.uiImportProjectAction.clicked.connect(self._importProjectActionSlot)
        self.uiExportProjectAction.clicked.connect(self._exportProjectActionSlot)
        self.uiQuitAction.clicked.connect(self._close)

        # edit menu connections
        self.uigeneralPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(0))
        self.uiserverPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(1))
        self.uiwiresharkPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(2))
        self.uivpcsPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(3))
        self.uidynamipsPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(4))
        self.uiunixPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(6))
        self.uivmwarePreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(12))
        self.uirouterPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(5))
        self.uiiouPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(7))
        self.uihospitalPreferencesAction.clicked.connect(lambda:self._preferencesActionSlot(13))

        # work menu connections
        self.uiStartAllAction.clicked.connect(self._startAllActionSlot)
        self.uiSuspendAllAction.clicked.connect(self._suspendAllActionSlot)
        self.uiStopAllAction.clicked.connect(self._stopAllActionSlot)
        self.uiReloadAllAction.clicked.connect(self._reloadAllActionSlot)
        self.uiAddLinkAction.clicked.connect(self._addLinkActionSlot)
        self.uiShowPortNamesAction.clicked.connect(self._showPortNamesActionSlot)
        self.uiConfigAllAction.clicked.connect(self._consoleAllActionSlot)
        self.uiZoomInAction.clicked.connect(self._zoomInActionSlot)
        self.uiZoomOutAction.clicked.connect(self._zoomOutActionSlot)
        self.uiScreenshotAction.clicked.connect(self._screenshotActionSlot)
        self.uiShowLayersAction.clicked.connect(self._showLayersActionSlot)
        self.uiShowGridAction.clicked.connect(self._showGridActionSlot)
        self.uiInsertImageAction.clicked.connect(self._insertImageActionSlot)
        self.uiDrawRectangleAction.clicked.connect(self._drawRectangleActionSlot)
        self.uiDrawEllipseAction.clicked.connect(self._drawEllipseActionSlot)
        self.uiAddNoteAction.clicked.connect(self._addNoteActionSlot)

        # course menu connections
        self.uiWareAction.clicked.connect(lambda:self._onlineActionSlot("http://ware.imnss.net"))
        self.uiExamAction.clicked.connect(lambda:self._onlineActionSlot("http://exam.imnss.net"))
        self.uiStorageAction.clicked.connect(lambda:self._onlineActionSlot("http://storage.imnss.net"))
        self.uiPaperAction.clicked.connect(lambda:self._onlineActionSlot("http://paper.imnss.net"))
        self.uiToolsAction.clicked.connect(lambda:self._onlineActionSlot("http://tools.imnss.net"))
        self.uiiMNSSAction.clicked.connect(lambda:self._onlineActionSlot("http://www.imnss.net"))

        # help menu connections
        self.uiCheckForUpdateAction.clicked.connect(self._checkForUpdateActionSlot)
        self.uiOnlineHelpAction.clicked.connect(lambda:self._onlineActionSlot("http://mnss.imnss.net"))
        self.uiExportDebugInformationAction.clicked.connect(self._exportDebugInformationSlot)
        self.uiDoctorAction.clicked.connect(self._doctorSlot)
        self.uiAboutAction.clicked.connect(self._aboutActionSlot)
        self.uiGuideAction.clicked.connect(self._showdocuSlot)
        self.uiFeedbackAction.clicked.connect(lambda:self._onlineActionSlot("http://www.imnss.net/about.html"))
        # self.uiFeedbackAction.clicked.connect(self._pass)

        # browsers tool bar connections
        self.uiBrowseRoutersAction.clicked.connect(self._browseRoutersActionSlot)
        self.uiBrowseSwitchesAction.clicked.connect(self._browseSwitchesActionSlot)
        self.uiBrowseClientDevicesAction.clicked.connect(self._browseClientActionSlot)
        self.uiBrowseServerDevicesAction.clicked.connect(self._browseServerActionSlot)
        self.uiBrowseSecurityDevicesAction.clicked.connect(self._browseSecurityDevicesActionSlot)
        self.uiBrowseHISDevicesAction.clicked.connect(self._browseHISDevicesActionSlot)
        self.uiBrowseLISDevicesAction.clicked.connect(self._browseLISDevicesActionSlot)
        self.uiBrowsePACSDevicesAction.clicked.connect(self._browsePACSDevicesActionSlot)
        self.uiBrowseConnectDevicesAction.clicked.connect(self._browserConnectionActionSlot)

        # connect the signal to the view
        self.adding_link_signal.connect(self.uiGraphicsView.addingLinkSlot)
        self.uiminimumAction.clicked.connect(self.showMinimized)
        self.uiMaximumAction.clicked.connect(self._fullScreenActionSlot)
        self.uicloseAction.clicked.connect(self._close)
        # project
        self.project_new_signal.connect(self.project_created)

        self.ready_signal.connect(self._readySlot)

        #downloadflush
        self.showtab.tabBarClicked['int'].connect(self._flush)

        # New appliance button
        # self.uiNewAppliancePushButton.clicked.connect(self._newApplianceActionSlot)

    def _showdockwidget(self, n):
        if n == 1:
            if self.uiTopologySummaryDockWidget.isHidden():
                self.uiTopologySummaryDockWidget.show()
            else:
                self.uiTopologySummaryDockWidget.hide()
        else:
            if self.uiServerSummaryDockWidget.isHidden():
                self.uiServerSummaryDockWidget.show()
            else:
                self.uiServerSummaryDockWidget.hide()

    def _pass(self):
        # for i in GlobalVar.downloadobjectlist:
        #     i.mark = False
        print(GlobalVar.totalLocalConfig._settings)
        # from gns3.download import progressbar
        # progressbar()
        pass
        # LocalConfig().saveSectionSettings(GlobalVar.section,GlobalVar.settings)
        # local_config._settings['Dynamips']['routers'] = GlobalVar.settings

    def _close(self):
        for i in GlobalVar.downloadobjectlist:
            i.thread_stop = True
        GlobalVar().quitdownload()
        self.close()

    def reflush(self):
        print('ok')

    def project(self):
        """
        Return current project
        """

        return self._project

    def _showdocuSlot(self):
        """
        Show install document
        """

        dialog = docu(self)
        dialog.show()
        dialog.exec_()

    def setProject(self, project):
        """
        Set current project

        :param project: Project instance
        """

        self._project = project
        self._setCurrentFile(project.topologyFile())

    def setUnsavedState(self):
        """
        Sets the project in a unsaved state.
        """

        if not self._ignore_unsaved_state:
            self.setWindowModified(True)

    def ignoreUnsavedState(self, value):
        """
        Activates or deactivates the possibility to
        set the project in unsaved state.

        :param value: boolean
        """

        self._ignore_unsaved_state = value

    def _showGridActionSlot(self):
        """
        Called when we ask to display the grid
        """

        self.uiGraphicsView.viewport().update()

    def _createNewProject(self, new_project_settings):
        """
        Creates a new project.

        :param new_project_settings: project settings (dict)
        """

        self._project.close()
        self._project = Project()
        self.uiGraphicsView.reset()
        # create the destination directory for project files
        try:
            os.makedirs(new_project_settings["project_files_dir"], exist_ok=True)
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "New project", "Could not create project files directory {}: {}".format(new_project_settings["project_files_dir"], e))
            self._createTemporaryProject()

        # let all modules know about the new project files directory
        # self.uiGraphicsView.updateProjectFilesDir(new_project_settings["project_files_dir"])

        topology = Topology.instance()
        topology.project = self._project

        self._project.setName(new_project_settings["project_name"])
        self._project.setTopologyFile(new_project_settings["project_path"])
        self.saveProject(new_project_settings["project_path"])
        self.project_new_signal.emit(self._project.topologyFile())

    def _newProjectActionSlot(self):
        """
        Slot called to create a new project.
        """

        if self.checkForUnsavedChanges():
            self._project_dialog = NewProjectDialog(self)
            self._project_dialog.show()
            create_new_project = self._project_dialog.exec_()
            # Close the device dock so it repopulates.  Done in case switching
            # between cloud and local.
            self.uiNodesDockWidget.setVisible(False)
            self.uiNodesDockWidget.setWindowTitle("")

            if create_new_project:
                new_project_settings = self._project_dialog.getNewProjectSettings()
                self._createNewProject(new_project_settings)
            else:
                self._createTemporaryProject()
            self._project_dialog = None

    def _newApplianceActionSlot(self):
        """
        Called when user want to create a new appliance
        """
        dialog = NewApplianceDialog(self)
        dialog.show()

    def _IOUVMConverterActionSlot(self):
        command = shutil.which("gns3-iouvm-converter")
        if command is None:
            QtWidgets.QMessageBox.critical(self, "GNS3 IOU VM Converter", "gns3-iouvm-converter not found")
            return
        try:
            subprocess.Popen([command])
        except (OSError, subprocess.SubprocessError) as e:
            QtWidgets.QMessageBox.critical(self, "GNS3 IOU VM Converter", "Error when running gns3-iouvm-converter {}".format(e))

    def openApplianceActionSlot(self):
        """
        Slot called to open an appliance.
        """

        directory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DownloadLocation)
        if len(directory) == 0:
            directory = self.projectsDirPath()
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        "Open appliance",
                                                        directory,
                                                        "All files (*.*);;GNS3 Appliance (*.gns3appliance *.gns3a)",
                                                        "GNS3 Appliance (*.gns3appliance *.gns3a)")
        if path:
            self.loadPath(path)

    def openProjectActionSlot(self):
        """
        Slot called to open a project.
        """

        path, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        "Open project",
                                                        self.projectsDirPath(),
                                                        "All files (*.*);;GNS3 Project (*.gns3);;GNS3 Portable Project (*.gns3project *.gns3p);;NET files (*.net)",
                                                        "GNS3 Project (*.gns3)")
        if path:
            self.loadPath(path)

    def _flush(self,tab):
        if tab == 0:
            try:
                self.downloadarea.removeItem(self.spacerItem)
            except Exception as e:
                pass
        elif tab == 1:
            try:
                self.downloadarea.removeItem(self.spacerItem)
            except Exception as e:
                pass
            for i in GlobalVar.downloadobjectlist:
                try:
                    self.downloadarea.removeItem(i.layout)
                except Exception as e:
                    pass
            for i in GlobalVar.downloadobjectlist:
                self.downloadarea.addItem(i.layout)
            self.downloadarea.addItem(self.spacerItem)

    def openRecentFileSlot(self):
        """
        Slot called to open recent file from the File menu.
        """

        action = self.sender()
        if action:
            path = action.data()
            if not os.path.isfile(path):
                QtWidgets.QMessageBox.critical(self, "Recent file", "{}: no such file".format(path))
                return
            self.loadPath(path)

    def loadSnapshot(self, path):
        """Loads a snapshot"""

        self._open_project_path = path
        self._project.project_closed_signal.connect(self._projectClosedContinueLoadPath)
        self._project.close()

    def loadPath(self, path):
        """Open a file and close the previous project"""

        if path:
            if self._first_file_load is True:
                self._first_file_load = False
                time.sleep(0.5)  # give some time to the server to initialize

            if self._project_dialog:
                self._project_dialog.reject()
                self._project_dialog = None

            for image_format in self.SUPPORTED_IMAGE_FORMATS:
                if path.endswith("." + image_format):
                    self._importImage(path)
                    return

            if path.endswith(".gns3project") or path.endswith(".gns3p"):
                project_name = os.path.basename(path).split('.')[0]
                self._project_dialog = NewProjectDialog(self, default_project_name=project_name)
                self._project_dialog.show()
                if self._project_dialog.exec_():
                    new_project_settings = self._project_dialog.getNewProjectSettings()
                    import_worker = ImportProjectWorker(path, new_project_settings)
                    import_worker.imported.connect(self.loadPath)
                    progress_dialog = ProgressDialog(import_worker, "Importing project", "Importing portable project files...", "Cancel", parent=self)
                    progress_dialog.show()
                    progress_dialog.exec_()

                self._project_dialog = None

            elif path.endswith(".gns3appliance") or path.endswith(".gns3a"):
                try:
                    self._appliance_wizard = ApplianceWizard(self, path)
                except ApplianceError as e:
                    QtWidgets.QMessageBox.critical(self, "Appliance", "Error while importing appliance {}: {}".format(path, str(e)))
                    return
                self._appliance_wizard.show()
                self._appliance_wizard.exec_()
            elif self.checkForUnsavedChanges():
                self._open_project_path = path
                if self._project.closed():
                    self._projectClosedContinueLoadPath()
                else:
                    self._project.project_closed_signal.connect(self._projectClosedContinueLoadPath)
                    self._project.close()

    def _projectClosedContinueLoadPath(self):

        path = self._open_project_path
        if self._loadProject(path):
            self.project_new_signal.emit(path)

    def _saveProjectActionSlot(self):
        """
        Slot called to save a project.
        """

        if self._project.temporary():
            return self.saveProjectAs()
        else:
            if not self._project.filesDir():
                QtWidgets.QMessageBox.critical(self, "Project", "Sorry, no project has been created or initialized")
                return
            return self.saveProject(self._project.topologyFile())

    def _saveProjectAsActionSlot(self):
        """
        Slot called to save a project to another location/name.
        """

        self.saveProjectAs()

    def _importExportConfigsActionSlot(self):
        """
        Slot called when importing and exporting configs
        for the entire topology.
        """

        options = ["Export configs to a directory", "Import configs from a directory"]
        selection, ok = QtWidgets.QInputDialog.getItem(self, "Import/Export configs", "Please choose an option:", options, 0, False)
        if ok:
            if selection == options[0]:
                self._exportConfigs()
            else:
                self._importConfigs()

    def _exportConfigs(self):
        """
        Exports all configs to a directory.
        """

        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Export directory", self._export_configs_to_dir, QtWidgets.QFileDialog.ShowDirsOnly)
        if path:
            self._export_configs_to_dir = os.path.dirname(path)
            for module in MODULES:
                instance = module.instance()
                if hasattr(instance, "exportConfigs"):
                    instance.exportConfigs(path)

    def _importConfigs(self):
        """
        Imports all configs from a directory.
        """

        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Import directory", self._import_configs_from_dir, QtWidgets.QFileDialog.ShowDirsOnly)
        if path:
            self._import_configs_from_dir = os.path.dirname(path)
            for module in MODULES:
                instance = module.instance()
                if hasattr(instance, "importConfigs"):
                    instance.importConfigs(path)

    def _createScreenshot(self, path):
        """
        Create a screenshot of the scene.

        :returns: True if the image was successfully saved; otherwise returns False
        """

        scene = self.uiGraphicsView.scene()
        scene.clearSelection()
        source = scene.itemsBoundingRect().adjusted(-20.0, -20.0, 20.0, 20.0)
        image = QtGui.QImage(source.size().toSize(), QtGui.QImage.Format_RGB32)
        image.fill(QtCore.Qt.white)
        painter = QtGui.QPainter(image)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.TextAntialiasing, True)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        scene.render(painter, source=source)
        painter.end()
        # TODO: quality option
        return image.save(path)

    def _screenshotActionSlot(self):
        """
        Slot called to take a screenshot of the scene.
        """

        # supported image file formats
        file_formats = "PNG File (*.png);;JPG File (*.jpeg *.jpg);;BMP File (*.bmp);;XPM File (*.xpm *.xbm);;PPM File (*.ppm);;TIFF File (*.tiff)"
        path, selected_filter = QtWidgets.QFileDialog.getSaveFileName(self, "Screenshot", self._screenshots_dir, file_formats)
        if not path:
            return
        self._screenshots_dir = os.path.dirname(path)

        # add the extension if missing
        file_format = "." + selected_filter[:4].lower().strip()
        if not path.endswith(file_format):
            path += file_format

        if not self._createScreenshot(path):
            QtWidgets.QMessageBox.critical(self, "Screenshot", "Could not create screenshot file {}".format(path))

    def _snapshotActionSlot(self):
        """
        Slot called to open the snapshot dialog.
        """

        if self._project.temporary():
            QtWidgets.QMessageBox.critical(self, "Snapshots", "Sorry, snapshots are not supported with temporary projects")
            return

        # first check if any node doesn't run locally
        topology = Topology.instance()
        for node in topology.nodes():
            if node.server() != Servers.instance().localServer():
                QtWidgets.QMessageBox.critical(self, "Snapshots", "Sorry, snapshots can only be created if all the nodes run locally")
                return

        if self._nodeRunning():
            QtWidgets.QMessageBox.warning(self, "Snapshots", "Sorry, snapshots can only be created when all nodes are stopped")
            return

        dialog = SnapshotsDialog(self,
                                 self._project.topologyFile(),
                                 self._project.filesDir())
        dialog.show()
        dialog.exec_()

    def _selectAllActionSlot(self):
        """
        Slot called to select all the items on the scene.
        """

        scene = self.uiGraphicsView.scene()
        for item in scene.items():
            item.setSelected(True)

    def _selectNoneActionSlot(self):
        """
        Slot called to none of the items on the scene.
        """

        scene = self.uiGraphicsView.scene()
        for item in scene.items():
            item.setSelected(False)

    def _fullScreenActionSlot(self):
        """
        Slot to switch to full screen.
        """

        if not self.windowState() & QtCore.Qt.WindowFullScreen:
            # switch to full screen
            self.setWindowState(self.windowState() | QtCore.Qt.WindowFullScreen)
            self.mousematch = False
        else:
            # switch back to normal
            self.setWindowState(self.windowState() & ~QtCore.Qt.WindowFullScreen)
            self.mousematch = True

    def _zoomInActionSlot(self):
        """
        Slot called to scale in the view.
        """

        factor_in = pow(2.0, 120 / 240.0)
        self.uiGraphicsView.scaleView(factor_in)

    def _zoomOutActionSlot(self):
        """
        Slot called to scale out the view.
        """

        factor_out = pow(2.0, -120 / 240.0)
        self.uiGraphicsView.scaleView(factor_out)

    def _zoomResetActionSlot(self):
        """
        Slot called to reset the zoom.
        """

        self.uiGraphicsView.resetTransform()

    def _fitInViewActionSlot(self):
        """
        Slot called to fit the topology in the view.
        """

        view = self.uiGraphicsView
        bounding_rect = view.scene().itemsBoundingRect().adjusted(-20.0, -20.0, 20.0, 20.0)
        view.ensureVisible(bounding_rect)
        view.fitInView(bounding_rect, QtCore.Qt.KeepAspectRatio)

    def _showLayersActionSlot(self):
        """
        Slot called to show the layer positions on the scene.
        """

        NodeItem.show_layer = self.uiShowLayersAction.isChecked()
        ShapeItem.show_layer = self.uiShowLayersAction.isChecked()
        ImageItem.show_layer = self.uiShowLayersAction.isChecked()
        NoteItem.show_layer = self.uiShowLayersAction.isChecked()
        for item in self.uiGraphicsView.items():
            item.update()

    def _resetPortLabelsActionSlot(self):
        """
        Slot called to reset the port labels on the scene.
        """

        for item in self.uiGraphicsView.scene().items():
            if isinstance(item, LinkItem):
                item.resetPortLabels()
                item.adjust()

    def _showPortNamesActionSlot(self):
        """
        Slot called to show the port names on the scene.
        """

        LinkItem.showPortLabels(self.uiShowPortNamesAction.isChecked())
        for item in self.uiGraphicsView.scene().items():
            if isinstance(item, LinkItem):
                item.adjust()

    def _startAllActionSlot(self):
        """
        Slot called when starting all the nodes.
        """
        self.uiSuspendAllAction.setChecked(False)
        self.uiStopAllAction.setChecked(False)
        for item in self.uiGraphicsView.scene().items():
            if isinstance(item, NodeItem) and hasattr(item.node(), "start") and item.node().initialized():
                item.node().start()

    def _suspendAllActionSlot(self):
        """
        Slot called when suspending all the nodes.
        """
        self.uiStartAllAction.setChecked(False)
        self.uiStopAllAction.setChecked(False)
        for item in self.uiGraphicsView.scene().items():
            if isinstance(item, NodeItem) and hasattr(item.node(), "suspend") and item.node().initialized():
                item.node().suspend()

    def _stopAllActionSlot(self):
        """
        Slot called when stopping all the nodes.
        """
        self.uiStartAllAction.setChecked(False)
        self.uiSuspendAllAction.setChecked(False)
        for item in self.uiGraphicsView.scene().items():
            if isinstance(item, NodeItem) and hasattr(item.node(), "stop") and item.node().initialized():
                item.node().stop()

    def _reloadAllActionSlot(self):
        """
        Slot called when reloading all the nodes.
        """

        for item in self.uiGraphicsView.scene().items():
            if isinstance(item, NodeItem) and hasattr(item.node(), "reload") and item.node().initialized():
                item.node().reload()

    def _deviceMenuActionSlot(self):
        """
        Slot to contextually show the device menu.
        """

        self.uiDeviceMenu.clear()
        self.uiGraphicsView.populateDeviceContextualMenu(self.uiDeviceMenu)

    def _auxConsoleAllActionSlot(self):
        """
        Slot called when connecting to all the nodes using the AUX console.
        """

        self.uiGraphicsView.auxConsoleFromItems(self.uiGraphicsView.scene().items())

    def _consoleAllActionSlot(self):
        """
        Slot called when connecting to all the nodes using the console.
        """

        self.uiGraphicsView.consoleFromItems(self.uiGraphicsView.scene().items())

    def _vpcsActionSlot(self):
        """
        Slot called when VPCS multi-host is clicked in the Tools menu.
        """

        vpcs_module = VPCS.instance()

        if self._project.filesDir() is None:
            QtWidgets.QMessageBox.critical(self, "VPCS", "Sorry, the project hasn't been initialized yet")
            return

        try:
            working_dir = os.path.join(self._project.filesDir(), "project-files", "vpcs", "multi-host")
            os.makedirs(working_dir, exist_ok=True)
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "VPCS", "Could not create the VPCS working directory: {}".format(e))
            return

        try:
            vpcs_port = vpcs_module.startMultiHostVPCS(working_dir)
        except ModuleError as e:
            QtWidgets.QMessageBox.critical(self, "VPCS", "{}".format(e))
            return

        try:
            from .telnet_console import telnetConsole
            telnetConsole("VPCS multi-host", "127.0.0.1", vpcs_port)
        except (OSError, ValueError) as e:
            QtWidgets.QMessageBox.critical(self, "Console", "Cannot start console application: {}".format(e))

    def _addNoteActionSlot(self):
        """
        Slot called when adding a new note on the scene.
        """

        self.uiGraphicsView.addNote(self.uiAddNoteAction.isChecked())

    def _insertImageActionSlot(self):
        """
        Slot called when inserting an image on the scene.
        """

        # supported image file formats
        file_formats = "Image files (*." + " *.".join(self.SUPPORTED_IMAGE_FORMATS) + ");;All files (*.*)"

        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Image", self._pictures_dir, file_formats)
        if path:
            self._importImage(path)

    def _importImage(self, path):

        if not self._project:
            return

        self._pictures_dir = os.path.dirname(path)
        files_dir = self._project.filesDir()
        if files_dir is None:
            QtWidgets.QMessageBox.critical(self, "Image", "Project is not yet created")
            return
        os.makedirs(files_dir, exist_ok=True)
        image = QtGui.QPixmap(path)
        if image.isNull():
            QtWidgets.QMessageBox.critical(self, "Image", "Image file format not supported")
            return

        destination_dir = os.path.join(files_dir, "project-files", "images")
        try:
            os.makedirs(destination_dir, exist_ok=True)
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "Image", "Could not create the image directory: {}".format(e))
            return

        image_filename = os.path.basename(path)
        destination_image_path = os.path.join(destination_dir, image_filename)
        if not os.path.isfile(destination_image_path):
            # copy the image to the project files directory
            try:
                shutil.copyfile(path, destination_image_path)
            except OSError as e:
                QtWidgets.QMessageBox.critical(self, "Image", "Could not copy the image to the project image directory: {}".format(e))
                return

        renderer = QtSvg.QSvgRenderer(path)
        if renderer.isValid():
            # use a SVG image item if this is a valid SVG file
            image = renderer

        # path to the image is relative to the project-files dir
        self.uiGraphicsView.addImage(image, os.path.join("images", image_filename))

    def _drawRectangleActionSlot(self):
        """
        Slot called when adding a rectangle on the scene.
        """

        self.uiGraphicsView.addRectangle(self.uiDrawRectangleAction.isChecked())

    def _drawEllipseActionSlot(self):
        """
        Slot called when adding a ellipse on the scene.
        """

        self.uiGraphicsView.addEllipse(self.uiDrawEllipseAction.isChecked())

    def _onlineActionSlot(self,url):
        """
        Slot to launch a browser pointing to the documentation page.
        """

        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def _checkForUpdateActionSlot(self, silent=False):
        """
        Slot to check if a newer version is available.

        :param silent: do not display any message
        """

        self._update_manager = UpdateManager()
        self._update_manager.checkForUpdate(self, silent)

    def _setupWizardActionSlot(self):
        """
        Slot to open the setup wizard.
        """

        with Progress.instance().context(min_duration=0):
            setup_wizard = SetupWizard(self)
            setup_wizard.show()
            setup_wizard.exec_()

    def _labInstructionsActionSlot(self, silent=False):
        """
        Slot to open lab instructions.
        """

        if self._project.temporary():
            QtWidgets.QMessageBox.critical(self, "Lab instructions", "Sorry, lab instructions are not supported with temporary projects")
            return

        project_dir = glob.escape(os.path.dirname(self._project.topologyFile()))
        instructions_files = glob.glob(project_dir + os.sep + "instructions.*")
        instructions_files += glob.glob(os.path.join(project_dir, "instructions") + os.sep + "instructions*")
        if len(instructions_files):
            path = instructions_files[0]
            if QtGui.QDesktopServices.openUrl(QtCore.QUrl('file:///' + path, QtCore.QUrl.TolerantMode)) is False and silent is False:
                QtWidgets.QMessageBox.critical(self, "Lab instructions", "Could not open {}".format(path))
        elif silent is False:
            QtWidgets.QMessageBox.critical(self, "Lab instructions", "No instructions found")

    def _aboutQtActionSlot(self):
        """
        Slot to display the Qt About dialog.
        """

        QtWidgets.QMessageBox.aboutQt(self)

    def _aboutActionSlot(self):
        """
        Slot to display the GNS3 About dialog.
        """

        dialog = AboutDialog(self)
        dialog.show()
        dialog.exec_()

    def _exportDebugInformationSlot(self):
        """
        Slot to display a window for exporting debug information
        """

        dialog = ExportDebugDialog(self, self._project)
        dialog.show()
        dialog.exec_()

    def _doctorSlot(self):
        """
        Slot to display a window for exporting debug information
        """

        dialog = DoctorDialog(self)
        dialog.show()
        dialog.exec_()

    def _academyActionSlot(self):
        """
        Slot to launch a browser pointing to the courses page.
        """

        QtGui.QDesktopServices.openUrl(QtCore.QUrl("http://academy.gns3.com/"))

    def _showNodesDockWidget(self, title, category, marked):
        """
        Makes the NodesDockWidget appear with the appropriate title and the devices
        from the specified category listed.
        Makes the dock disappear if the same category is selected.

        :param title: NodesDockWidget title
        :param category: category of device to list
        """

        if self.uiNodesDockWidget.windowTitle() == title:
            self.uiNodesDockWidget.setVisible(False)
            self.uiNodesDockWidget.setWindowTitle("")
        else:
            self.uiNodesDockWidget.setWindowTitle(title)
            self.uiNodesDockWidget.setVisible(True)
            self.uiNodesView.clear()
            if marked == 'router':
                self.uiNodesView.ROUTERpopulateNodesView(category,marked)
            elif marked == 'switch':
                self.uiNodesView.SWITCHpopulateNodesView(category,marked)
            elif marked == 'security':
                self.uiNodesView.SECURITYpopulateNodesView(category,marked)
            elif marked == 'connection':
                self.uiNodesView.populateNodesView(category)
            else:
                self.uiNodesView.VMpopulateNodesView(category,marked)

    def _localConfigChangedSlot(self):
        """
        Called when the local config change
        """

        self.uiNodesView.refresh()

    def _browseRoutersActionSlot(self):
        """
        Slot to browse all the routers.
        """

        self._showNodesDockWidget("路由器", Node.routers,'router')

    def _browseSwitchesActionSlot(self):
        """
        Slot to browse all the switches.
        """

        self._showNodesDockWidget("交换机", Node.switches,'switch')

    def _browseSecurityDevicesActionSlot(self):
        """
        Slot to browse all the security devices.
        """

        self._showNodesDockWidget("防火墙", Node.security_devices,'security')

    def _browseHISDevicesActionSlot(self):
        """
        Slot to browse HIS devices.
        """
        self._showNodesDockWidget("HIS系统", None, 'his')

    def _browseLISDevicesActionSlot(self):
        """
        Slot to browse LIS devices.
        """
        self._showNodesDockWidget("LIS系统", None, 'lis')

    def _browsePACSDevicesActionSlot(self):
        """
        Slot to browse PACS devices.
        """
        self._showNodesDockWidget("PACS系统", None, 'pacs')

    def _browseClientActionSlot(self):
        """
        Slot to browse client devices.
        """

        self._showNodesDockWidget("客户端设备", Node.routers,'client')

    def _browseServerActionSlot(self):
        """
        Slot to browse server devices.
        """

        self._showNodesDockWidget("服务端设备", Node.routers,'server')

    def _browserConnectionActionSlot(self):
        """
        Slot to browse all the devices.
        """

        self._showNodesDockWidget("桥接设备", None,'connection')

    def _browseEndDevicesActionSlot(self,category):
        """
        Slot to browse all the end devices.
        """

        self._showNodesDockWidget(category, Node.end_devices,'end')

    def _addLinkActionSlot(self):
        """
        Slot to receive events from the add a link action.
        """

        if not self.uiAddLinkAction.isChecked():
            self.adding_link_signal.emit(False)
        else:
            self.adding_link_signal.emit(True)

    def _preferencesActionSlot(self,market):
        """
        Slot to show the preferences dialog.
        """

        with Progress.instance().context(min_duration=0):
            GlobalVar.globalmarket = market
            dialog = PreferencesDialog(self)
            dialog.restoreGeometry(QtCore.QByteArray().fromBase64(self._settings["preferences_dialog_geometry"].encode()))
            dialog.show()
            dialog.exec_()
            self._settings["preferences_dialog_geometry"] = bytes(dialog.saveGeometry().toBase64()).decode()
            self.setSettings(self._settings)

    def _editReadmeActionSlot(self):
        """
        Slot to edit the README file
        """

        if self._project.temporary():
            QtWidgets.QMessageBox.critical(self, "README", "Sorry, README file is not supported with temporary projects")
            return

        log.debug("Opened %s", self._project.readmePathFile())
        if not os.path.exists(self._project.readmePathFile()):
            try:
                with open(self._project.readmePathFile(), "w+") as f:
                    f.write("Title: My lab\nAuthor: Grace Hopper <grace@example.org>\n\nThis lab is about...")
            except OSError as e:
                QtWidgets.QMessageBox.critical(self, "README", "Could not create {}".format(self._project.readmePathFile()))
                return
        if QtGui.QDesktopServices.openUrl(QtCore.QUrl('file:///' + self._project.readmePathFile(), QtCore.QUrl.TolerantMode)) is False:
            QtWidgets.QMessageBox.critical(self, "README", "Could not open {}".format(self._project.readmePathFile()))

    def keyPressEvent(self, event):
        """
        Handles all key press events for the main window.

        :param event: QKeyEvent
        """

        key = event.key()
        # if the user is adding a link and press Escape, then cancel the link addition.
        if self.uiAddLinkAction.isChecked() and key == QtCore.Qt.Key_Escape:
            self.uiAddLinkAction.setChecked(False)
            self._addLinkActionSlot()
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event):
        """
        Handles the event when the main window is closed.

        :param event: QCloseEvent
        """

        progress = Progress.instance()
        progress.setAllowCancelQuery(True)
        progress.setCancelButtonText("Force quit")

        log.debug("Close the main Windows")

        self._analytics_client.sendScreenView("Main Window", session_start=False)

        servers = Servers.instance()
        if self._project.closed():
            log.debug("Project is closed killing server and closing main windows")
            self._finish_application_closing(close_windows=False)
            event.accept()
            self.uiConsoleTextEdit.closeIO()
        elif not self._soft_exit or self.checkForUnsavedChanges():
            log.debug("Project is not closed asking for project closing")
            self._project.project_closed_signal.connect(self._finish_application_closing)
            self._project.close(local_server_shutdown=True)
            event.ignore()
        else:
            event.ignore()

    def _finish_application_closing(self, close_windows=True):
        """
        Handles the event when the main window is closed.
        And project closed.

        :params closing: True the windows is currently closing do not try to reclose it
        """

        log.debug("_finish_application_closing")
        VPCS.instance().stopMultiHostVPCS()

        GNS3VM.instance().shutdown()
        self._settings["geometry"] = bytes(self.saveGeometry().toBase64()).decode()
        self._settings["state"] = bytes(self.saveState().toBase64()).decode()
        self.setSettings(self._settings)

        servers = Servers.instance()
        servers.stopLocalServer(wait=True)

        time_spent = "{:.0f}".format(time.time() - self._start_time)
        log.debug("Time spend in the software is {}".format(time_spent))

        if close_windows:
            self.close()

    def _nodeRunning(self):
        """
        Display a warning to user

        :returns: False is a device is still running
        """
        # check if any node is running
        topology = Topology.instance()
        topology.project = self._project
        running_node = False
        for node in topology.nodes():
            if hasattr(node, "start") and node.status() == Node.started:
                return True
        return False

    def checkForUnsavedChanges(self):
        """
        Checks if there are any unsaved changes.

        :returns: boolean
        """

        if self._nodeRunning():
            QtWidgets.QMessageBox.warning(self, "Closing project", "A device is still running, please stop it before closing your project")
            return False

        if self.testAttribute(QtCore.Qt.WA_WindowModified):
            if self._project.temporary():
                destination_file = "untitled.gns3"
            else:
                destination_file = os.path.basename(self._project.topologyFile())
            reply = QtWidgets.QMessageBox.warning(self, "未保存修改", '你有尚未保存的项目"{}"'.format(destination_file),
                                                  QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel)
            if reply == QtWidgets.QMessageBox.Save:
                if self._project.temporary():
                    return self.saveProjectAs()
                return self.saveProject(self._project.topologyFile())
            elif reply == QtWidgets.QMessageBox.Cancel:
                return False
        return True

    def startupLoading(self):
        """
        Called by QTimer.singleShot to load everything needed at startup.
        """

        if not LocalConfig.instance().isMainGui():
            reply = QtWidgets.QMessageBox.warning(self, "MNSS", "您已打开MNSS，是否继续？",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.No:
                self.close()
                return

        if not sys.platform.startswith("win") and os.geteuid() == 0:
            QtWidgets.QMessageBox.warning(self, "Root", "Running GNS3 as root is not recommended and could be dangerous")

        # restore debug level
        if self._settings["debug_level"]:
            root = logging.getLogger()
            root.addHandler(logging.StreamHandler(sys.stdout))

        # restore the style
        self._setStyle(self._settings.get("style"))

        servers = Servers.instance()
        # start the GNS3 VM
        gns3_vm = GNS3VM.instance()
        if not gns3_vm.isRunning():
            servers.initVMServer()
            if gns3_vm.isRemote():
                gns3_vm.setRunning(True)
            elif gns3_vm.autoStart():
                worker = WaitForVMWorker()
                progress_dialog = ProgressDialog(worker, "GNS3 VM", "Starting the GNS3 VM...", "Cancel", busy=True, parent=self, delay=5)
                progress_dialog.show()
                if progress_dialog.exec_():
                    gns3_vm.adjustLocalServerIP()

        # start and connect to the local server
        server = servers.localServer()
        if servers.shouldLocalServerAutoStart():
                if not servers.localServerAutoStart():
                    QtWidgets.QMessageBox.critical(self, "本地服服务器", "无法打开本地服务进程: {}".format(servers.localServerPath()))
                    return

                worker = WaitForConnectionWorker(server.host(), server.port())
                progress_dialog = ProgressDialog(worker,
                                                 "本地Server",
                                                 "正在连接服务器 {} : {}...".format(server.host(), server.port()),
                                                 "取消", busy=True, parent=self)
                progress_dialog.show()
                if not progress_dialog.exec_():
                    return

        # show the setup wizard
        if not self._settings["hide_setup_wizard"] and not gns3_vm.isRunning():
            with Progress.instance().context(min_duration=0):
                pass
                # setup_wizard = SetupWizard(self)
                # setup_wizard.show()
                # setup_wizard.exec_()

        self._analytics_client.sendScreenView("Main Window")
        self._createTemporaryProject()
        self.ready_signal.emit()

        if self._settings["check_for_update"]:
            # automatic check for update every week (604800 seconds)
            current_epoch = int(time.mktime(time.localtime()))
            if current_epoch - self._settings["last_check_for_update"] >= 604800:
                # let's check for an update
                self._checkForUpdateActionSlot(silent=True)
                self._settings["last_check_for_update"] = current_epoch
                self.setSettings(self._settings)

    def _readySlot(self):
        """
        Called when the application is ready to load a project
        """
        if self._settings["auto_launch_project_dialog"] and self._first_file_load:
            self._project_dialog = NewProjectDialog(self, showed_from_startup=True)
            self._project_dialog.accepted.connect(self._newProjectDialodAcceptedSlot)
            self._project_dialog.show()

    def _newProjectDialodAcceptedSlot(self):
        """
        Called when user accept the new project dialog
        """
        if self._project_dialog:
            new_project_settings = self._project_dialog.getNewProjectSettings()
            self._createNewProject(new_project_settings)
            self._project_dialog = None

    def _running_nodes(self):
        """
        :returns: Return the list of running nodes
        """
        topology = Topology.instance()
        running_nodes = []
        for node in topology.nodes():
            if hasattr(node, "start") and node.status() == Node.started:
                running_nodes.append(node.name())
        return running_nodes

    def _isTopologyOnRemoteServer(self):
        """
        :returns: Boolean True if topology run on a remote server
        """
        topology = Topology.instance()
        running_nodes = []
        for node in topology.nodes():
            if not node.server().isLocal():
                return True
        return False

    def saveProjectAs(self):
        """
        Saves a project to another location/name.

        :returns: GNS3 project file (.gns3)
        """

        if self._nodeRunning():
            QtWidgets.QMessageBox.warning(self, "Save As", "All devices must be stopped before saving to another location")
            return False

        if self._isTopologyOnRemoteServer() and not self._project.temporary():
            MessageBox(self, "Save project", "You can not use the save as function on a remote project for the moment.")
            return

        if self._project.temporary():
            default_project_name = "untitled"
        else:
            default_project_name = self._project.name()

        projects_dir_path = os.path.normpath(os.path.expanduser(self.projectsDirPath()))
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setWindowTitle("Save project")
        file_dialog.setNameFilters(["Directories"])
        file_dialog.setDirectory(projects_dir_path)
        file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        file_dialog.setLabelText(QtWidgets.QFileDialog.FileName, "Project name:")
        file_dialog.selectFile(default_project_name)
        file_dialog.setOptions(QtWidgets.QFileDialog.ShowDirsOnly)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        if file_dialog.exec_() == QtWidgets.QFileDialog.Rejected:
            return

        project_dir = file_dialog.selectedFiles()[0]
        project_name = os.path.basename(project_dir)
        topology_file_path = os.path.join(project_dir, project_name + ".gns3")
        old_topology_file_path = os.path.join(project_dir, default_project_name + ".gns3")

        # create the destination directory for project files
        try:
            os.makedirs(project_dir, exist_ok=True)
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "Save project", "Could not create project directory {}: {}".format(project_dir, e))
            return

        if self._project.temporary():
            # move files if saving from a temporary project
            log.info("Moving project files from {} to {}".format(self._project.filesDir(), project_dir))
            worker = ProcessFilesWorker(self._project.filesDir(), project_dir, move=True, skip_files=[".gns3_temporary"])
            progress_dialog = ProgressDialog(worker, "Project", "Moving project files...", "Cancel", parent=self)
        else:
            # else, just copy the files
            log.info("Copying project files from {} to {}".format(self._project.filesDir(), project_dir))
            worker = ProcessFilesWorker(self._project.filesDir(), project_dir)
            progress_dialog = ProgressDialog(worker, "Project", "Copying project files...", "Cancel", parent=self)
        progress_dialog.show()
        progress_dialog.exec_()

        errors = progress_dialog.errors()
        if errors:
            errors = "\n".join(errors)
            MessageBox(self, "Save project", "Errors detected while saving the project", errors, icon=QtWidgets.QMessageBox.Warning)

        self._project.setName(project_name)
        if self._project.temporary():
            self._project.moveFromTemporaryToPath(project_dir)
            return self.saveProject(topology_file_path)
        else:
            # We save the topology and use the standard restore process to reinitialize everything
            self._project.setTopologyFile(topology_file_path)
            self.saveProject(topology_file_path, random_id=True)

            if os.path.exists(old_topology_file_path):
                try:
                    os.remove(old_topology_file_path)
                except OSError as e:
                    MessageBox(self, "Save project", "Errors detected while saving the project", str(e), icon=QtWidgets.QMessageBox.Warning)
            return self.loadPath(topology_file_path)

    def saveProject(self, path, random_id=False):
        """
        Saves a project.

        :param path: path to project file
        :param random_id: Randomize project and vm id (use for save as)
        """

        topology = Topology.instance()
        topology.project = self._project
        try:
            self._project.commit()
            topo = topology.dump(random_id=random_id)
            log.info("Saving project: {}".format(path))
            content = json.dumps(topo, sort_keys=True, indent=4)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "Save", "Could not save project to {}: {}".format(path, e))
            return False

        if self._settings["auto_screenshot"]:
            self._createScreenshot(os.path.join(os.path.dirname(path), "screenshot.png"))
        self.uiStatusBar.showMessage("Project saved to {}".format(path), 2000)
        self._project.setTopologyFile(path)
        self._setCurrentFile(path)

        self._analytics_client.sendScreenView("Main Window")

        return True

    def _convertOldProject(self, path):
        """
        Converts old ini-style GNS3 topologies (<=0.8.7) to the newer version 1+ JSON format.

        :param path: path to the project file.
        """

        try:
            from gns3converter.main import do_conversion, get_snapshots, ConvertError
        except ImportError as e:
            log.error("GNS3 converter is missing: {}".format(str(e)))
            QtWidgets.QMessageBox.critical(self, "GNS3 converter", "Please install gns3-converter in order to open old ini-style GNS3 projects")
            self._createTemporaryProject()
            return

        try:
            project_name = os.path.basename(os.path.dirname(path))
            project_dir = os.path.join(self.projectsDirPath(), project_name)

            while os.path.isdir(project_dir):
                text, ok = QtWidgets.QInputDialog.getText(self,
                                                          "GNS3 converter",
                                                          "Project '{}' already exists. Please choose an alternative project name:".format(project_name),
                                                          text=project_name + "2")
                if ok:
                    project_name = text
                    project_dir = os.path.join(self.projectsDirPath(), project_name)
                else:
                    self._createTemporaryProject()
                    return

            for snapshot_def in get_snapshots(path):
                do_conversion(snapshot_def, project_name, project_dir, quiet=True)

            topology_def = {'file': path, 'snapshot': False}
            do_conversion(topology_def, project_name, project_dir, quiet=True)
        except ConvertError as e:
            QtWidgets.QMessageBox.critical(self, "GNS3 converter", "Could not convert {}: {}".format(path, e))
            self._createTemporaryProject()
            return
        except Exception:
            exc_type, exc_value, exc_tb = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_tb)
            tb = "".join(lines)
            MessageBox(self, "GNS3 converter", "Unexpected exception while converting {}".format(path), details=tb)
            self._createTemporaryProject()
            return

        QtWidgets.QMessageBox.information(self, "GNS3 converter", "Your project has been converted to a new format and can be found in: {}".format(project_dir))
        project_path = os.path.join(project_dir, project_name + ".gns3")
        self._loadProject(project_path)

    def _loadProject(self, path):
        """
        Loads a project into GNS3.

        :param path: path to project file
        """

        self._project = Project()
        self.uiGraphicsView.reset()
        topology = Topology.instance()
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

            extension = os.path.splitext(path)[1]
            if extension == ".net":
                self._convertOldProject(path)
                return
            topology.loadFile(path, self._project)
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "Load", "Could not load project {}: {}".format(os.path.basename(path), e))
            # log.error("exception {type}".format(type=type(e)), exc_info=1)
            self._createTemporaryProject()
            return False
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Load", "Invalid or corrupted file: {}".format(e))
            self._createTemporaryProject()
            return False
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

        self.uiStatusBar.showMessage("Project loaded {}".format(path), 2000)
        self._setCurrentFile(path)
        self._labInstructionsActionSlot(silent=True)

        return True

    def _createTemporaryProject(self):
        """
        Creates a temporary project.
        """

        if self._project:
            self._project.close()
        self._project = Project()
        self._project.setTemporary(True)
        self._project.setName("unsaved")
        self.uiGraphicsView.reset()
        self._setCurrentFile()

    def isTemporaryProject(self):
        """
        Returns either this is a temporary project or not.

        :returns: boolean
        """

        return self._project.temporary()

    def _setCurrentFile(self, path=None):
        """
        Sets the current project file path.

        :param path: path to project file
        """

        if not path:
            self.setWindowFilePath("Unsaved project")
            self.setWindowTitle("Unsaved project[*] - GNS3")
        else:
            path = os.path.normpath(path)
            self.setWindowFilePath(path)
            self.setWindowTitle("{path}[*] - GNS3".format(path=os.path.basename(path)))
            self._updateRecentFileSettings(path)
            # self._updateRecentFileActions()

        self.setWindowModified(False)

    def _updateRecentFileSettings(self, path):
        """
        Updates the recent file settings.

        :param path: path to the new file
        """

        recent_files = []
        for file_path in self._settings["recent_files"]:
            if file_path:
                file_path = os.path.normpath(file_path)
                if file_path not in recent_files and os.path.exists(file_path):
                    recent_files.append(file_path)

        # update the recent file list
        if path in recent_files:
            recent_files.remove(path)
        recent_files.insert(0, path)
        if len(recent_files) > self._max_recent_files:
            recent_files.pop()

        # write the recent file list
        self._settings["recent_files"] = recent_files
        self.setSettings(self._settings)

    def _updateRecentFileActions(self):
        """
        Updates recent file actions.
        """

        index = 0
        size = len(self._settings["recent_files"])
        for file_path in self._settings["recent_files"]:
            try:
                if file_path and os.path.exists(file_path):
                    action = self._recent_file_actions[index]
                    action.setText(" {}. {}".format(index + 1, os.path.basename(file_path)))
                    action.setData(file_path)
                    action.setVisible(True)
                    index += 1
            # We can have this error if user save a file with unicode char
            # and change his system locale.
            except UnicodeEncodeError:
                pass

        for index in range(size + 1, self._max_recent_files):
            self._recent_file_actions[index].setVisible(False)

        if size:
            self._recent_file_actions_separator.setVisible(True)

    @staticmethod
    def projectsDirPath():
        """
        Returns the projects directory path.

        :returns: path to the default projects directory
        """

        return Servers.instance().localServerSettings()["projects_path"]

    @staticmethod
    def instance():
        """
        Singleton to return only one instance of MainWindow.

        :returns: instance of MainWindow
        """

        if not hasattr(MainWindow, "_instance"):
            MainWindow._instance = MainWindow()
        return MainWindow._instance

    def project_created(self, project):
        """
        This slot is invoked when a project is created or opened

        :param project: path to gns3 project file currently opened
        """

        if self._project.temporary():
            # do nothing if project is temporary
            return

        try:
            with open(project, encoding="utf-8") as f:
                json_topology = json.load(f)
                if not isinstance(json_topology, dict):
                    raise ValueError("Not a GNS3 project")
        except (OSError, ValueError) as e:
            QtWidgets.QMessageBox.critical(self, "Project", "Could not read project: {}".format(e))

    def run_later(self, counter, callback):
        """
        Run a function after X milliseconds

        :params counter: Time to wait before fire the callback (in milliseconds)
        :params callback: Function to run
        """

        QtCore.QTimer.singleShot(counter, callback)

    def _exportProjectActionSlot(self):
        """
        Slot called to export a portable project
        """

        running_nodes = self._running_nodes()
        if running_nodes:
            nodes = "\n".join(running_nodes)
            MessageBox(self, "Export project", "Please stop the following nodes before exporting the project", nodes)
            return

        if self.testAttribute(QtCore.Qt.WA_WindowModified):
            QtWidgets.QMessageBox.critical(self, "Export project", "Please save the project before exporting it")
            return

        if self._project.temporary():
            QtWidgets.QMessageBox.critical(self, "Export project", "A temporary project cannot be exported")
            return

        topology = Topology.instance()
        for node in topology.nodes():
            if node.__class__.__name__ in ["VirtualBoxVM", "VMwareVM"]:
                QtWidgets.QMessageBox.critical(self, "Export portable project", "A project containing VMware or VirtualBox VMs cannot be exported because the VMs are managed by these software.")
                return
            if node.__class__.__name__ in ["Cloud"]:
                QtWidgets.QMessageBox.critical(self, "Export portable project", "A project containing cloud cannot be exported as a portable project because cloud depends of the machine.")
                return

        include_image_question = """Would you like to include any base image?

The project will not require additional images to run on another host, however the resulting file will be much bigger.

It is your responsability to check if you have the right to distribute the image(s) as part of the project.
        """

        reply = QtWidgets.QMessageBox.question(self, "Export project", include_image_question,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        include_images = int(reply == QtWidgets.QMessageBox.Yes)

        if not os.path.exists(self._project.readmePathFile()):
            text, ok = QtWidgets.QInputDialog.getMultiLineText(self, "Export project",
                                                               "Please provide a description for the project, especially if you want to share it. \nThe description will be saved in README.txt inside the project file",
                                                               "Project title\n\nAuthor: Grace Hopper <grace@example.org>\n\nThis project is about...")
            if not ok:
                return
            try:
                with open(self._project.readmePathFile(), 'wb+') as f:
                    f.write(text.encode("utf-8"))
            except OSError as e:
                QtWidgets.QMessageBox.critical(self, "Export project", "Could not create {}: {}".format(self._project.readmePathFile(), e))
                return

        for server in self._project.servers():
            if not server.isLocal() and not server.isGNS3VM():
                QtWidgets.QMessageBox.critical(self, "Export project", "Projects running on a remote server cannot be exported. Only projects running locally or in the GNS3 VM are supported.")
                return

        directory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DocumentsLocation)
        if len(directory) == 0:
            directory = self.projectsDirPath()

        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export portable project", directory,
                                                        "GNS3 Portable Project (*.gns3project *.gns3p)",
                                                        "GNS3 Portable Project (*.gns3project *.gns3p)")
        if path is None or len(path) == 0:
            return

        if not path.endswith(".gns3project") and not path.endswith(".gns3p"):
            path += ".gns3project"

        try:
            open(path, 'wb+').close()
        except OSError as e:
            QtWidgets.QMessageBox.critical(self, "Export project", "Could not write {}: {}".format(path, e))
            return

        export_worker = ExportProjectWorker(self._project, path, include_images)
        progress_dialog = ProgressDialog(export_worker, "Exporting project", "Exporting portable project files...", "Cancel", parent=self)
        progress_dialog.show()
        progress_dialog.exec_()

    def _importProjectActionSlot(self):
        """
        Slot called to import a portable project
        """

        directory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DownloadLocation)
        if len(directory) == 0:
            directory = self.projectsDirPath()
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        "Import project",
                                                        directory,
                                                        "All files (*.*);;GNS3 Portable Project (*.gns3project *.gns3p)",
                                                        "GNS3 Portable Project (*.gns3project *.gns3p)")
        if not path:
            return
        self.loadPath(path)

    def _setStyle(self, style):

        if style.startswith("Charcoal"):
            self._setCharcoalStyle()
            return True
        elif style == "Classic":
            self._setClassicStyle()
            return True

        return False

    def _getStyleIcon(self, normalon_file, normaloff_file = None):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(normalon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(normaloff_file), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def _setLegacyStyle(self):
        """
        Sets the legacy GUI style.
        """

        pass

    def _setClassicStyle(self):
        """
        Sets the classic GUI style.
        """

        self.setStyleSheet("")
        self.uiNewProjectAction.setIcon(self._getStyleIcon(":/images/new.png"))
        self.uiOpenProjectAction.setIcon(self._getStyleIcon(":/classic_icons/open.svg"))
        self.uiSaveProjectAsAction.setIcon(self._getStyleIcon(":/images/save.png"))
        self.uiImportProjectAction.setIcon(self._getStyleIcon(":/images/import.png"))
        self.uiExportProjectAction.setIcon(self._getStyleIcon(":/images/export.png"))
        self.uiQuitAction.setIcon(self._getStyleIcon(":/images/exit.png"))
        self.uigeneralPreferencesAction.setIcon(self._getStyleIcon(":/images/generalPreferences.png"))
        self.uiserverPreferencesAction.setIcon(self._getStyleIcon(":/images/serverPreferences.png"))
        self.uiwiresharkPreferencesAction.setIcon(self._getStyleIcon(":/images/wiresharkPreferences.png"))
        self.uivpcsPreferencesAction.setIcon(self._getStyleIcon(":/images/vpcsPreferences.png"))
        self.uidynamipsPreferencesAction.setIcon(self._getStyleIcon(":/images/dynamipsPreferences.png"))
        self.uiunixPreferencesAction.setIcon(self._getStyleIcon(":/images/unixPreferences.png"))
        self.uivmwarePreferencesAction.setIcon(self._getStyleIcon(":/images/vmwarePreferences.png"))
        self.uirouterPreferencesAction.setIcon(self._getStyleIcon(":/images/routerPreferences.png"))
        self.uiiouPreferencesAction.setIcon(self._getStyleIcon(":/images/iouPreferences.png"))
        self.uihospitalPreferencesAction.setIcon(self._getStyleIcon(":/images/hospitalPreferences.png"))
        self.uiStartAllAction.setIcon(self._getStyleIcon(":/charcoal_icons/start-hover.svg",":/charcoal_icons/start.svg"))
        self.uiSuspendAllAction.setIcon(self._getStyleIcon(":/classic_icons/pause-hover.svg",":/classic_icons/pause.svg"))
        self.uiStopAllAction.setIcon(self._getStyleIcon(":/classic_icons/stop-hover.svg",":/classic_icons/stop.svg"))
        self.uiReloadAllAction.setIcon(self._getStyleIcon(":/classic_icons/reload.svg"))
        self.uiAddLinkAction.setIcon(self._getStyleIcon(":/classic_icons/add-link-cancel.svg", ":/classic_icons/add-link.svg"))
        self.uiShowPortNamesAction.setIcon(self._getStyleIcon(":/classic_icons/show-interface-names-hover.svg",":/classic_icons/show-interface-names.svg"))
        self.uiZoomInAction.setIcon(self._getStyleIcon(":/classic_icons/zoom-in.svg"))
        self.uiZoomOutAction.setIcon(self._getStyleIcon(":/classic_icons/zoom-out.svg"))
        self.uiScreenshotAction.setIcon(self._getStyleIcon(":/classic_icons/camera-photo.svg"))
        self.uiInsertImageAction.setIcon(self._getStyleIcon(":/classic_icons/image.svg"))
        self.uiAddNoteAction.setIcon(self._getStyleIcon(":/classic_icons/add-note.svg"))
        self.uiDrawEllipseAction.setIcon(self._getStyleIcon(":/classic_icons/ellipse.svg"))
        self.uiDrawRectangleAction.setIcon(self._getStyleIcon(":/classic_icons/rectangle.svg"))
        self.uiGuideAction.setIcon(self._getStyleIcon(":/images/guide.png"))
        self.uiCheckForUpdateAction.setIcon(self._getStyleIcon(":/images/update.png"))
        self.uiOnlineHelpAction.setIcon(self._getStyleIcon(":/images/online.png"))
        self.uiExportDebugInformationAction.setIcon(self._getStyleIcon(":/images/debugstepout.png"))
        self.uiDoctorAction.setIcon(self._getStyleIcon(":/images/doctor.png"))
        self.uiAboutAction.setIcon(self._getStyleIcon(":/images/about.png"))
        self.uiFeedbackAction.setIcon(self._getStyleIcon(":/images/feedback.png"))
        self.uiBrowseRoutersAction.setIcon(self._getStyleIcon(":/classic_icons/router.svg"))
        self.uiBrowseSwitchesAction.setIcon(self._getStyleIcon(":/classic_icons/switch-hover.svg"))
        self.uiBrowseSecurityDevicesAction.setIcon(self._getStyleIcon(":/classic_icons/firewall.svg"))
        self.uiBrowseClientDevicesAction.setIcon(self._getStyleIcon(":/classic_icons/pc.svg"))
        self.uiBrowseServerDevicesAction.setIcon(self._getStyleIcon(":/classic_icons/pc.svg"))
        self.uiBrowseHISDevicesAction.setIcon(self._getStyleIcon(":/images/His.png"))
        self.uiBrowseLISDevicesAction.setIcon(self._getStyleIcon(":/images/Lis.png"))
        self.uiBrowsePACSDevicesAction.setIcon(self._getStyleIcon(":/images/Pacs.png"))
        self.uiBrowseClientDevicesAction.setIcon(self._getStyleIcon(":/images/Client.png"))
        self.uiBrowseServerDevicesAction.setIcon(self._getStyleIcon(":/images/Server.png"))
        self.uiBrowseConnectDevicesAction.setIcon(self._getStyleIcon(":/images/connection.png"))
        self.uiminimumAction.setIcon(self._getStyleIcon(":/images/minimum.png"))
        self.uiMaximumAction.setIcon(self._getStyleIcon(":/images/RestoreDown.png",":/images/maximization.png"))
        self.uicloseAction.setIcon(self._getStyleIcon(":/images/close.png"))
        self.uiShowTopology.setIcon(self._getStyleIcon(":/images/topology.png"))
        self.uiShowServer.setIcon(self._getStyleIcon(":/images/sever.png"))
        self.uiConfigAllAction.setIcon(self._getStyleIcon(":/classic_icons/console.svg", ":/classic_icons/console-hover.svg"))
        self.uiWareAction.setIcon(self._getStyleIcon(":/images/ware.png"))
        self.uiExamAction.setIcon(self._getStyleIcon(":/images/exam.png"))
        self.uiStorageAction.setIcon(self._getStyleIcon(":/images/storage.png"))
        self.uiPaperAction.setIcon(self._getStyleIcon(":/images/paper.png"))
        self.uiToolsAction.setIcon(self._getStyleIcon(":/images/tools.png"))
        self.uiiMNSSAction.setIcon(self._getStyleIcon(":/images/iMNSS.png"))

    def _setCharcoalStyle(self):
        """
        Sets the charcoal GUI style.
        """

        pass
