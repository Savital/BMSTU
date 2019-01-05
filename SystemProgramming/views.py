# views.py MainWindow view
# Savital https://github.com/Savital

from PyQt5 import uic, QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
import string

# MainWindow is view
class MainWindow(QWidget):
    monitoringSignal = QtCore.pyqtSignal()
    addUserSignal = QtCore.pyqtSignal(list)
    deleteUserSignal = QtCore.pyqtSignal(list)
    clearLogSignal = QtCore.pyqtSignal()
    closeSignal = QtCore.pyqtSignal()
    changeUserStateSignal = QtCore.pyqtSignal(list)

    def __init__(self, users):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("MainForm.ui", self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        for item in users:
            for name in item:
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
            self.comboUser.setEnabled(False)
        else:
            self.buttonMonitoring.setStyleSheet("background-color: rgb(255, 85, 0)")
            self.buttonMonitoring.setText("Включить мониторинг действий")
            self.comboUser.setEnabled(True)

    @QtCore.pyqtSlot(list)
    def onAddUserSignalReverted(self, list):
        if (list[0]):
            self.comboUser.addItem(list[1])
        else:
            reply = QMessageBox.critical(self, 'Ошибка', "Данное имя уже существует", QMessageBox.Ok)

    @QtCore.pyqtSlot(list)
    def onDeleteUserSignalReverted(self, list):
        if (list[0]):
            self.comboUser.removeItem(self.comboUser.findText(list[1]))
        else:
            reply = QMessageBox.critical(self, 'Ошибка', "Данного имени нет", QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def onClearLogSignalReverted(self):
        pass #Revert signal ClearLog TODO

    @QtCore.pyqtSlot()
    def onComboUserChanged(self):
        self.changeUserStateSignal.emit([self.comboUser.currentText()])

    @QtCore.pyqtSlot(list)
    def onRefreshSignalReverted(self, list):
        self.keyDelay.setText(str(list[0]))
        self.keySearch.setText(str(list[1]))
        self.keyNumber.setText(str(list[2]))
        self.keyCombines.setText(str(list[3]))
        self.keyFunctionals.setText(str(list[4]))
        print(list)

    @QtCore.pyqtSlot(list)
    def onChangeUserStateSignalReverted(self, list):
        self.keyDelay.setText(str(list[0]))
        self.keySearch.setText(str(list[1]))
        self.keyNumber.setText(str(list[2]))
        self.keyCombines.setText(str(list[3]))
        self.keyFunctionals.setText(str(list[4]))
        print(list)

def onButtonMonitoringClick(window):
    window.monitoringSignal.emit()

def onButtonAddUserClick(window):
    name = window.editUserName.text().strip()
    if name != "":
        window.addUserSignal.emit([name])
    else:
        reply = QMessageBox.critical(window, 'Ошибка', "Неправильный формат имени", QMessageBox.Ok)

def onButtonDeleteUserClick(window):
    name = window.editUserName.text().strip()
    window.deleteUserSignal.emit([name])

def onButtonClearLogClick(window):
    window.clearLogSignal.emit()