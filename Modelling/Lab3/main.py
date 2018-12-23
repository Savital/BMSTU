print("Lab3")

import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem, QTableWidgetItem

import numpy
from numpy.linalg.linalg import LinAlgError

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("MainWindow.ui", self)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()