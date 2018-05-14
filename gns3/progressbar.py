from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QBasicTimer,QSize


class ProgressBar(QtWidgets.QWidget):
    def __init__(self, newobject, parent=None):
        # super().__init__(parent)
        self.newobject = newobject
        self.pbar = QProgressBar(self)
        self.pbar.setMinimumSize(QSize(280, 20))
        self.pbar.setMaximumSize(QSize(280, 20))

        self.timer = QBasicTimer()
        self.timer.isActive()

    def timerEvent(self, event):
        if self.step >= self.newobject.total:
            self.timer.stop()
            return
        self.pbar.setValue(self.newobject.size)
