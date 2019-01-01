# views.py MainWindow view
# Savital https://github.com/Savital

from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *

from manager import Manager

class MainWindow(QWidget):
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

def onButtonMonitoringClick(window):
    window.buttonMonitoringClamped = not window.buttonMonitoringClamped

    if (window.buttonMonitoringClamped):
        window.buttonMonitoring.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(0, 255, 0, 255), stop:0.840909 rgba(0, 136, 0, 255));\n")
        window.buttonMonitoring.setText("Выключить мониторинг действий")
    else:
        window.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")
        window.buttonMonitoring.setText("Включить мониторинг действий")

    print("onClick")

def onButtonAddUserClick(window):
    print("onButtonAddClick")

def onButtonDeleteUserClick(window):
    print("onButtonDeleteClick")

def onButtonClearLogClick(window):
    print("onButtonClearClick")