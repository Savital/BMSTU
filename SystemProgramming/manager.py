# manager.py Manager control
# Savital https://github.com/Savital

import sys
from PyQt5 import QtCore, QtSql
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import *
from views import MainWindow
from models import KeypadMonitoringDB
from threading import Timer, Thread, Event

# Runs function hFunction on clock, when state is not zero
class RefreshEventGenerator():
    def __init__(self, t, hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)
        self.state = 0

    def __del__(self):
        pass

    def handle_function(self):
        if self.state:
            self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

    def runF(self):
        self.state += 1

    def stopF(self):
        self.state -= 1

# Controller, handles signals between view and model
class Manager(QtCore.QObject):
    doneMonitoringSignal = QtCore.pyqtSignal(list)
    doneAddUserSignal = QtCore.pyqtSignal(list)
    doneDeleteUserSignal = QtCore.pyqtSignal(list)
    doneClearLogSignal = QtCore.pyqtSignal()
    refreshDataSignal = QtCore.pyqtSignal(list)
    doneChangeUserStateSignal = QtCore.pyqtSignal(list)

    def __init__(self):
        super(Manager, self).__init__()
        self.construct()
        self.timer = RefreshEventGenerator(0.01, self.refreshData)
        self.timer.start()

    def __del__(self):
        self.db.disconnect()

    def construct(self):
        self.db = KeypadMonitoringDB()
        self.db.connect()
        self.users = self.db.selectUsers()
        self.user = ""
        if len(self.users):
            self.user = self.users[0][0]
        self.monitoringFlag = False

    def connects(self):
        self.window.monitoringSignal.connect(self.monitoring)
        self.window.addUserSignal.connect(self.addUser)
        self.window.deleteUserSignal.connect(self.deleteUser)
        self.window.clearLogSignal.connect(self.clearLog)

        self.doneMonitoringSignal.connect(self.window.onMonitoringSignalReverted)
        self.doneAddUserSignal.connect(self.window.onAddUserSignalReverted)
        self.doneDeleteUserSignal.connect(self.window.onDeleteUserSignalReverted)
        self.doneClearLogSignal.connect(self.window.onClearLogSignalReverted)

        #Close when the thread finishes (normally)
        self.window.closeSignal.connect(self.close)
        self.window.comboUser.currentTextChanged.connect(self.window.onComboUserChanged)
        self.window.changeUserStateSignal.connect(self.changeUserState)
        #Close when the thread terminated (TODO)
        self.refreshDataSignal.connect(self.window.onRefreshSignalReverted)
        self.doneChangeUserStateSignal.connect(self.window.onChangeUserStateSignalReverted)

    def runApp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow(self.users)
        self.window.show()
        self.connects()
        sys.exit(self.app.exec_())

    @QtCore.pyqtSlot()
    def monitoring(self):
        self.monitoringFlag = not self.monitoringFlag
        if self.monitoringFlag:
            self.timer.runF()
        else:
            self.timer.stopF()

        self.doneMonitoringSignal.emit([self.monitoringFlag])

    @QtCore.pyqtSlot(list)
    def addUser(self, list):
        names = self.db.selectUsersByName(list[0])
        if names == None:
            self.db.insertUser(list[0])
            self.doneAddUserSignal.emit([True, list[0]])
        else:
            self.doneAddUserSignal.emit([False, list[0]])

    @QtCore.pyqtSlot(list)
    def deleteUser(self, list):
        names = self.db.selectUsersByName(list[0])
        if names != None:
            self.doneDeleteUserSignal.emit([True, list[0]])
            self.db.deleteUser(list[0])
        else:
            self.doneDeleteUserSignal.emit([False, list[0]])

    @QtCore.pyqtSlot()
    def clearLog(self):
        print("Manager.ClearLog()") #TODO
        self.doneClearLogSignal.emit()

    @QtCore.pyqtSlot()
    def close(self):
        self.timer.cancel()

    @QtCore.pyqtSlot(list)
    def changeUserState(self, list): #TODO
        self.user = list[0]
        self.stats = "xxx"
        self.doneChangeUserStateSignal.emit([1.0, 1.0, 1.0, 1.0, 1.0, self.stats])

    def refreshData(self): #TODO
        #results = self.db.selectData(self.user)
        self.stats = "xxx"
        self.refreshDataSignal.emit([1.0, 1.0, 1.0, 1.0, 1.0, self.stats])