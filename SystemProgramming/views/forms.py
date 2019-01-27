# Savital https://github.com/Savital
# views.py MainForm view

from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *

import string

class BaseForm(QWidget):
    messages = {"EXIT" : ["Сообщение", "Вы точно хотите выйти?"],
                "EMPTY_NAME" : ["Ошибка", "Остались незаполненные поля."],
                "ALREADY_EXIST" : ["Ошибка", "Данное имя уже присутствует в базе данных."],
                "DOESNT_EXIST" : ["Ошибка", "Данного имени нет в базе данных."],
                "WRONG_FORMAT" : ["Ошибка", "Неправильный формат имени."],
                "LKM_MISSING" : ["Ошибка", "Отсутсвует модуль сбора статистики."]}

    initWindowSignal = QtCore.pyqtSignal()
    changeUserStateSignal = QtCore.pyqtSignal(list)

    monitoringSignal = QtCore.pyqtSignal()
    addUserSignal = QtCore.pyqtSignal(list)
    deleteUserSignal = QtCore.pyqtSignal(list)
    clearLogSignal = QtCore.pyqtSignal()

    closeSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(BaseForm, self).__init__()
        pass

    def __del__(self):
        pass

    def construct(self):
        pass

    @QtCore.pyqtSlot(list)
    def onInitWindowSignalReverted(self, list):
        pass

    @QtCore.pyqtSlot()
    def onComboUserChanged(self):
        pass

    @QtCore.pyqtSlot(list)
    def onChangeUserStateSignalReverted(self, list):
        pass

    @QtCore.pyqtSlot(list)
    def onMonitoringSignalReverted(self, list):
        pass

    @QtCore.pyqtSlot(list)
    def onAddUserSignalReverted(self, list):
        pass

    @QtCore.pyqtSlot(list)
    def onDeleteUserSignalReverted(self, list):
        pass

    @QtCore.pyqtSlot()
    def onClearLogSignalReverted(self):
        pass

    @QtCore.pyqtSlot(list)
    def onRefreshSignalReverted(self, list):
        pass

    def onButtonMonitoringClick(window):
        pass

    def onButtonAddUserClick(window):
        pass

    def onButtonDeleteUserClick(window):
        pass

    def onButtonClearLogClick(window):
        pass

    def displayMessage(self, list):
        try:
            message = self.messages[list[0]]
        except:
            message = ["Ошибка", "Неизвестная ошибка."]
        return QMessageBox.critical(self, message[0], message[1], QMessageBox.Ok)

    def askMessage(self, list):
        return QMessageBox.question(self, list[0], list[1], QMessageBox.Yes, QMessageBox.No)

# MainForm is view
class MainForm(BaseForm):
    def __init__(self):
        super(MainForm, self).__init__()
        self.UI = uic.loadUi("static/MainForm.ui", self)
        self.setWindowIcon(QtGui.QIcon('static/icon.png'))

        self.construct()

    def __del__(self):
        pass

    def construct(self):
        self.buttonMonitoring.clicked.connect(lambda: self.onButtonMonitoringClick())
        self.buttonAdd.clicked.connect(lambda: self.onButtonAddUserClick())
        self.buttonDelete.clicked.connect(lambda: self.onButtonDeleteUserClick())
        self.buttonClear.clicked.connect(lambda: self.onButtonClearLogClick())

        self.buttonMonitoring.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(0, 255, 0, 255), stop:0.840909 rgba(0, 136, 0, 255));\n")

    def closeEvent(self, event):
        reply = self.askMessage(self.messages["EXIT"])

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
            self.textLogging.setText("Журнал пуст")
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
        self.comboUser.addItem(list[0])

    @QtCore.pyqtSlot(list)
    def onDeleteUserSignalReverted(self, list):
        self.comboUser.removeItem(self.comboUser.findText(list[0]))

    @QtCore.pyqtSlot()
    def onClearLogSignalReverted(self):
        self.textLogging.setText("Журнал пуст")

    @QtCore.pyqtSlot(list)
    def onRefreshSignalReverted(self, list):
        self.keyDelay.setText(str(list[0][0]))
        self.keySearch.setText(str(list[0][1]))
        self.keyNumber.setText(str(list[0][2]))
        self.keyCombines.setText(str(list[0][3]))
        self.keyFunctionals.setText(str(list[0][4]))

        if len(list[1]) == 0:
            self.textLogging.setText("Журнал пуст")
        elif len(list[1][0]) == 1:
            self.textLogging.setText(str(list[1]))
        else:
            text = ""
            for item in list[1]:
                text += str(item) + "\n"
            self.textLogging.setText(text)

    def onButtonMonitoringClick(self):
        self.monitoringSignal.emit()

    def onButtonAddUserClick(self):
        name = self.editUserName.text().strip()
        self.addUserSignal.emit([name])

    def onButtonDeleteUserClick(self):
        name = self.editUserName.text().strip()
        self.deleteUserSignal.emit([name])

    def onButtonClearLogClick(self):
        self.clearLogSignal.emit()