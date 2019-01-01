# views.py MainWindow view
# Savital https://github.com/Savital

from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    monitoringSignal = QtCore.pyqtSignal()
    addUserSignal = QtCore.pyqtSignal()
    deleteUserSignal = QtCore.pyqtSignal()
    clearLogSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("MainForm.ui", self)
        self.construct()

    def construct(self):
        self.buttonMonitoring.clicked.connect(lambda: onButtonMonitoringClick(self))
        self.buttonAdd.clicked.connect(lambda: onButtonAddUserClick(self))
        self.buttonDelete.clicked.connect(lambda: onButtonDeleteUserClick(self))
        self.buttonClear.clicked.connect(lambda: onButtonClearLogClick(self))

        self.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")
        self.buttonMonitoringClamped = False

    @QtCore.pyqtSlot()
    def onMonitoringRevertSignal(self):
        print("Revert signal Monitoring")
        self.buttonMonitoringClamped = not self.buttonMonitoringClamped

        if (self.buttonMonitoringClamped):
            self.buttonMonitoring.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(0, 255, 0, 255), stop:0.840909 rgba(0, 136, 0, 255));\n")
            self.buttonMonitoring.setText("Выключить мониторинг действий")
        else:
            self.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")
            self.buttonMonitoring.setText("Включить мониторинг действий")

    @QtCore.pyqtSlot()
    def onAddUserRevertSignal(self):
        print("Revert signal AddUser")

    @QtCore.pyqtSlot()
    def onDeleteUserRevertSignal(self):
        print("Revert signal DeleteUser")

    @QtCore.pyqtSlot()
    def onClearLogRevertSignal(self):
        print("Revert signal ClearLog")

def onButtonMonitoringClick(window):
    window.monitoringSignal.emit()

def onButtonAddUserClick(window):
    window.addUserSignal.emit()

def onButtonDeleteUserClick(window):
    window.deleteUserSignal.emit()

def onButtonClearLogClick(window):
    window.clearLogSignal.emit()

