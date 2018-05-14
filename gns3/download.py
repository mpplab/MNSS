import requests, os, re
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from gns3.globalvar import GlobalVar
import time

class wget(QtWidgets.QWidget):

    c7200templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "mac_addr": "",
        "midplane": "vxr",
        "mmap": True,
        "name": "",
        "npe": "npe-400",
        "nvram": 512,
        "platform": "c7200",
        "private_config": "",
        "ram": 512,
        "server": "local",
        "slot0": "C7200-IO-FE",
        "slot1": "",
        "slot2": "",
        "slot3": "",
        "slot4": "",
        "slot5": "",
        "slot6": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY",
    }
    c3660templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "3660",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "iomem": 5,
        "mac_addr": "",
        "mmap": True,
        "name": "",
        "nvram": 256,
        "platform": "c3600",
        "private_config": "",
        "ram": 192,
        "server": "local",
        "slot0": "Leopard-2FE",
        "slot1": "",
        "slot2": "",
        "slot3": "",
        "slot4": "",
        "slot5": "",
        "slot6": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY"
    }
    c3640templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "3640",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "iomem": 5,
        "mac_addr": "",
        "mmap": True,
        "name": "",
        "nvram": 256,
        "platform": "c3600",
        "private_config": "",
        "ram": 192,
        "server": "local",
        "slot0": "",
        "slot1": "",
        "slot2": "",
        "slot3": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY"
    }
    c3620templet = {
        "auto_delete_disks": True,
        "category": 0,
        "chassis": "3620",
        "default_name_format": "R{0}",
        "disk0": 0,
        "disk1": 0,
        "exec_area": 64,
        "idlemax": 500,
        "idlepc": "",
        "idlesleep": 30,
        "image": "",
        "iomem": 5,
        "mac_addr": "",
        "mmap": True,
        "name": "",
        "nvram": 256,
        "platform": "c3600",
        "private_config": "",
        "ram": 192,
        "server": "local",
        "slot0": "",
        "slot1": "",
        "sparsemem": True,
        "startup_config": '',
        "symbol": ":/symbols/router.svg",
        "system_id": "FTX0945W0MY"
    }

    def __init__(self, url, total, path, area):
        QtWidgets.QWidget.__init__(self)
        self.url = url
        self.total = total
        self.area = area
        self.size = 0
        self.suspendsize = 0
        self.filename = url.split('/')[-1]
        self.local_filename = path
        self.tmp_filename = self.local_filename + '.downtmp'

        self.textlabel = self._newtextlable()
        self.progressbar = self._newprogressbar()
        self.status = self._newstatus()
        self.layout = self._newlayout()
        self.thread_stop = False
        self.status.clicked['bool'].connect(self._changestatus)

    def _newlayout(self):
        new  = QtWidgets.QHBoxLayout(self.area)
        new.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        new.setSpacing(0)
        new.addWidget(self.textlabel)
        new.addWidget(self.progressbar)
        new.addWidget(self.status)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        new.addItem(spacerItem)
        return new

    def _newtextlable(self):
        new  = QtWidgets.QLabel(self.area)
        new.setText(self.url.split('/')[-1] + ':')
        length = len(new.text())
        new.setMinimumSize(QtCore.QSize(length*8, 20))
        new.setMaximumSize(QtCore.QSize(length*8, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        new.setFont(font)
        return new

    def _newprogressbar(self):
        new = QtWidgets.QProgressBar(self.area)
        new.setMinimumSize(QSize(500, 20))
        new.setMaximumSize(QSize(500, 20))
        new.setStyleSheet("QProgressBar::chunk {\n"
                                       "    background-color: #808080;\n"
                                       "    width: 20px;\n"
                                       "}\n"
                                       " \n"
                                       "QProgressBar {\n"
                                       "    border: 2px solid grey;\n"
                                       "    border-radius: 5px;\n"
                                       "    text-align: center;\n"
                                       "    font: 75 12pt \"宋体\"; \n"
                                       "}")
        new.setMaximum(self.total)
        return new

    def _newstatus(self):
        new = QtWidgets.QPushButton(self.area)
        new.setMinimumSize(QtCore.QSize(25, 25))
        new.setMaximumSize(QtCore.QSize(25, 25))
        new.setCheckable(True)
        new.setStyleSheet("QPushButton{\n"
                                "    border:solid 1px black opacity 0.4;\n"
                                "    }\n"
                                "QPushButton:hover {\n"
                                "    border-width: 1px;\n"
                                "    background-color:  rgb(240,240,240);\n"
                                "    border-color: rgb(171,168,165);\n"
                                "    border-style: outset;\n"
                                "    }\n"
                                "QPushButton:pressed {\n"
                                "    background-color: white;\n"
                                "    border-style: inset;\n"
                                "    }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/images/suspend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        new.setIcon(icon)
        return new

    def touch(self, filename):
        with open(filename, 'w') as fin:
            pass

    def remove_nonchars(self, name):
        (name, _) = re.subn(r'[\\\/\:\*\?\"\<\>\|]', '', name)
        return name

    def suspend(self):
        self.saveload()

    def finish(self):
        time.sleep(0.5)
        self.thread_stop = True
        self.status.setVisible(False)
        self.progressbar.setValue(self.total)
        os.remove(self.tmp_filename)
        temp = self.getRouterTemplet(self.filename)
        GlobalVar.totalLocalConfig.saveSectionSettings('Dynamips', temp)
        from gns3.main_window import MainWindow
        main_window = MainWindow.instance()
        main_window.uiNodesDockWidget.setVisible(False)
        main_window.uiNodesDockWidget.setWindowTitle("")
        GlobalVar.downloadobjectlist.remove(self)
        GlobalVar.downloadurllist.remove(self.url)

    def saveload(self):
        with open(self.tmp_filename, 'w') as ftmp:
            ftmp.write(str(self.suspendsize))

    def _changestatus(self,status):
        if status == True:
            self.thread_stop = True
        elif status == False:
            self.thread_stop = False
            newthreading(self).start()

    def getRouterTemplet(self,imagename):
        temp = {}
        if 'c7200' in imagename:
            temp = self.c7200templet
        elif 'c3660' in imagename:
            temp = self.c3660templet
        elif 'c3640' in imagename:
            temp = self.c3640templet
        elif 'c3620' in imagename:
            temp = self.c3620templet
        else:
            pass
        temp['startup_config'] = 'ios_base_startup-config.txt'
        temp["image"] = imagename
        temp["name"] = imagename[:-4]
        import copy
        settings = copy.deepcopy(GlobalVar.totalLocalConfig._settings['Dynamips'])
        if 'routers' not in settings.keys():
            settings['routers'] = []
        settings['routers'].append(temp)
        return settings

class newthreading(threading.Thread):
    def __init__(self,wget):
        threading.Thread.__init__(self)
        self.wget = wget

    def run(self):
        headers = {}
        size = 0
        try:
            with open(self.wget.tmp_filename, 'rb') as fin:
                self.wget.size = int(fin.read())
                size = self.wget.size + 1
        except:
            self.wget.touch(self.wget.tmp_filename)
        finally:
            headers['Range'] = "bytes=%d-" % (self.wget.size,)
        r = requests.get(self.wget.url, stream=True, verify=False, headers=headers)
        with open(self.wget.local_filename, 'ab+') as f:
            f.seek(self.wget.size)
            f.truncate()
            try:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        size += len(chunk)
                        self.wget.suspendsize = size
                        f.flush()
                    if self.wget.thread_stop == True:
                        self.wget.suspend()
                        break
                if self.wget.thread_stop == False:
                    self.wget.finish()
            except:
                pass

