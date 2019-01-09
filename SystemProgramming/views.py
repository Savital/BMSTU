# Savital https://github.com/Savital
# views.py MainWindow view

from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *

from errors import *

import string

# MainWindow is view
class MainWindow(QWidget):
    initWindowSignal = QtCore.pyqtSignal()
    changeUserStateSignal = QtCore.pyqtSignal(list)

    monitoringSignal = QtCore.pyqtSignal()
    addUserSignal = QtCore.pyqtSignal(list)
    deleteUserSignal = QtCore.pyqtSignal(list)
    clearLogSignal = QtCore.pyqtSignal()

    closeSignal = QtCore.pyqtSignal()
    errorSignal = QtCore.pyqtSignal(list)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("MainForm.ui", self)
        self.setWindowIcon(QtGui.QIcon('static/icon.png'))

        self.construct()

    def __del__(self):
        pass

    def construct(self):
        self.buttonMonitoring.clicked.connect(lambda: onButtonMonitoringClick(self))
        self.buttonAdd.clicked.connect(lambda: onButtonAddUserClick(self))
        self.buttonDelete.clicked.connect(lambda: onButtonDeleteUserClick(self))
        self.buttonClear.clicked.connect(lambda: onButtonClearLogClick(self))

        self.buttonMonitoring.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(0, 255, 0, 255), stop:0.840909 rgba(0, 136, 0, 255));\n")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение', "Вы точно хотите выйти?", QMessageBox.Yes, QMessageBox.No) #TODO

        if reply == QMessageBox.Yes:
            event.accept()
            self.closeSignal.emit()
        else:
            event.ignore()

    def showEvent(self, QShowEvent):
        self.initWindowSignal.emit()

    @QtCore.pyqtSlot(list)
    def onInitWindowSignalReverted(self, list):
        for item in list[0]:
            for name in item:
                self.comboUser.addItem(name)

    @QtCore.pyqtSlot()
    def onComboUserChanged(self):
        self.changeUserStateSignal.emit([self.comboUser.currentText()])

    @QtCore.pyqtSlot(list)
    def onChangeUserStateSignalReverted(self, list):
        self.keyDelay.setText(str(list[0][0]))
        self.keySearch.setText(str(list[0][1]))
        self.keyNumber.setText(str(list[0][2]))
        self.keyCombines.setText(str(list[0][3]))
        self.keyFunctionals.setText(str(list[0][4]))

        if len(list[1]) == 0:
            self.textLogging.setText("Log is empty")
        elif len(list[1][0]) == 1:
            self.textLogging.setText(str(list[1]))
        else:
            text = ""
            for item in list[1]:
                text += str(item) + "\n"
            self.textLogging.setText(text)

    @QtCore.pyqtSlot(list)
    def onMonitoringSignalReverted(self, list):
        if (list[0]):
            self.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")
            self.buttonMonitoring.setText("Выключить мониторинг действий")
            self.comboUser.setEnabled(False)
        else:
            self.buttonMonitoring.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(0, 255, 0, 255), stop:0.840909 rgba(0, 136, 0, 255));\n")
            self.buttonMonitoring.setText("Включить мониторинг действий")
            self.comboUser.setEnabled(True)

    @QtCore.pyqtSlot(list)
    def onAddUserSignalReverted(self, list):
        if (list[0]):
            self.comboUser.addItem(list[1])
        else:
            ErrorMessage(self, "Данное имя уже существует") #TODO

    @QtCore.pyqtSlot(list)
    def onDeleteUserSignalReverted(self, list):
        if (list[0]):
            self.comboUser.removeItem(self.comboUser.findText(list[1]))
        else:
            ErrorMessage(self, "Данного имени нет") #TODO

    @QtCore.pyqtSlot()
    def onClearLogSignalReverted(self):
        self.textLogging.setText("Log is empty")

    @QtCore.pyqtSlot(list)
    def onRefreshSignalReverted(self, list):
        self.keyDelay.setText(str(list[0][0]))
        self.keySearch.setText(str(list[0][1]))
        self.keyNumber.setText(str(list[0][2]))
        self.keyCombines.setText(str(list[0][3]))
        self.keyFunctionals.setText(str(list[0][4]))

        if len(list[1]) == 0:
            self.textLogging.setText("Log is empty")
        elif len(list[1][0]) == 1:
            self.textLogging.setText(str(list[1]))
        else:
            text = ""
            for item in list[1]:
                text += str(item) + "\n"
            self.textLogging.setText(text)

def onButtonMonitoringClick(window):
    window.monitoringSignal.emit()

def onButtonAddUserClick(window):
    name = window.editUserName.text().strip()
    if name != "":
        window.addUserSignal.emit([name])
    else:
        ErrorMessage("Неправильный формат имени") #TODO

def onButtonDeleteUserClick(window):
    name = window.editUserName.text().strip()
    window.deleteUserSignal.emit([name])

def onButtonClearLogClick(window):
    window.clearLogSignal.emit()