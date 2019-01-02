# views.py MainWindow view
# Savital https://github.com/Savital

from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
import string

class MainWindow(QWidget):
    monitoringSignal = QtCore.pyqtSignal()
    addUserSignal = QtCore.pyqtSignal()
    deleteUserSignal = QtCore.pyqtSignal()
    clearLogSignal = QtCore.pyqtSignal()
    closeSignal = QtCore.pyqtSignal()

    def __init__(self, users):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("MainForm.ui", self)

        for name in users: # select items TODO
            self.comboUser.addItem(name)

        self.construct()

    def __del__(self):
        pass #MainWindow.del TODO

    def construct(self):
        self.buttonMonitoring.clicked.connect(lambda: onButtonMonitoringClick(self))
        self.buttonAdd.clicked.connect(lambda: onButtonAddUserClick(self))
        self.buttonDelete.clicked.connect(lambda: onButtonDeleteUserClick(self))
        self.buttonClear.clicked.connect(lambda: onButtonClearLogClick(self))

        self.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение', "Вы точно хотите выйти?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.closeSignal.emit()
        else:
            event.ignore()

    @QtCore.pyqtSlot(list)
    def onMonitoringSignalReverted(self, list):
        if (list[0]):
            self.buttonMonitoring.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(0, 255, 0, 255), stop:0.840909 rgba(0, 136, 0, 255));\n")
            self.buttonMonitoring.setText("Выключить мониторинг действий")
        else:
            self.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")
            self.buttonMonitoring.setText("Включить мониторинг действий")

    @QtCore.pyqtSlot()
    def onAddUserSignalReverted(self):
        pass #Revert signal AddUser TODO

    @QtCore.pyqtSlot()
    def onDeleteUserSignalReverted(self):
        pass #Revert signal DeleteUser TODO

    @QtCore.pyqtSlot()
    def onClearLogSignalReverted(self):
        pass #Revert signal ClearLog TODO

def onButtonMonitoringClick(window):
    window.monitoringSignal.emit()

def onButtonAddUserClick(window):
    name = window.editUserName.text().strip()
    if name != "":
        window.comboUser.addItem(name)
        window.addUserSignal.emit() # TODO
    else:
        reply = QMessageBox.critical(window, 'Сообщение', "Ошибка формата имени", QMessageBox.Ok)

def onButtonDeleteUserClick(window):
    window.deleteUserSignal.emit()

def onButtonClearLogClick(window):
    window.clearLogSignal.emit()