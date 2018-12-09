import socket
from threading import Thread
import random
import string
import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem, QTableWidgetItem

LEN = 40
TIMEOUT = 60

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("server.ui", self)
        self.construct()

    def construct(self):
        self.btnStart.clicked.connect(lambda: onBtnStart(self))
        self.loggerText.setReadOnly(True)

def onBtnStart(window):
    window.loggerText.setText("Logout:")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

