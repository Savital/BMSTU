# manager.py Manager control
# Savital https://github.com/Savital

import sys
from PyQt5 import QtCore, QtSql
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import *
from views import MainWindow
from models import KeypadMonitoringDB
from threading import Timer, Thread, Event
from reader import DataReader
import pygame

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
    doneInitSignal = QtCore.pyqtSignal(list)
    doneChangeUserStateSignal = QtCore.pyqtSignal(list)

    doneMonitoringSignal = QtCore.pyqtSignal(list)
    doneAddUserSignal = QtCore.pyqtSignal(list)
    doneDeleteUserSignal = QtCore.pyqtSignal(list)
    doneClearLogSignal = QtCore.pyqtSignal()

    refreshDataSignal = QtCore.pyqtSignal(list)

    def __init__(self):
        super(Manager, self).__init__()
        self.construct()
        self.timer = RefreshEventGenerator(0.01, self.refreshData)
        self.timer.start()

    def __del__(self):
        pass

    def construct(self):
        self.db = KeypadMonitoringDB()
        self.db.createTableUsers()
        self.db.createTableLog()

        self.monitoringFlag = False

    def connects(self):
        self.window.initWindowSignal.connect(self.initWindow)
        self.doneInitSignal.connect(self.window.onInitWindowSignalReverted)

        self.window.changeUserStateSignal.connect(self.changeUserState)
        self.doneChangeUserStateSignal.connect(self.window.onChangeUserStateSignalReverted)
        self.window.comboUser.currentTextChanged.connect(self.window.onComboUserChanged)

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
        #Close when the thread terminated (TODO)

        self.refreshDataSignal.connect(self.window.onRefreshSignalReverted)


    def runApp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.connects()
        self.window.show()
        sys.exit(self.app.exec_())

    @QtCore.pyqtSlot()
    def initWindow(self):
        self.users = self.db.selectUsers()
        self.user = ""
        if len(self.users):
            self.user = self.users[0][0]

        self.doneInitSignal.emit([self.users])

    @QtCore.pyqtSlot(list)
    def changeUserState(self, list):
        self.user = list[0]

        self.log = self.db.selectLogByName(self.user)
        self.stats = self.formStats()
        self.doneChangeUserStateSignal.emit([self.stats, self.log])

    @QtCore.pyqtSlot()
    def monitoring(self):
        self.monitoringFlag = not self.monitoringFlag
        if self.monitoringFlag:
            dataReader = DataReader("/proc/keymonitoring")
            list = dataReader.get()
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
        self.db.deleteLogByName(self.user)
        self.doneClearLogSignal.emit()

    @QtCore.pyqtSlot()
    def close(self):
        self.timer.cancel()

    def averageDowntime(self, list):
        average = 0.0
        for item in self.log:
            average += item[2]
        average /= len(self.log)
        return average

    def averageSearchtime(self, list):
        average = 0.0
        for item in self.log:
            average += item[3]
        average /= len(self.log)
        return average

    def inputSpeed(self, list):
        sum = 0
        for item in self.log:
            sum += item[2] + item[3]
        return 1000 * len(self.log) / (sum)

    def formStats(self):
        list = []
        if len(self.log) == 0:
            list.append(0.0)
            list.append(0.0)
            list.append(0.0)
            list.append(0.0)
            list.append(0.0)
        elif len(self.log[0]) == 1:
            list.append(self.log[0][2])
            list.append(self.log[0][3])
            list.append(1 / (self.log[0][2] + self.log[0][3]))
            list.append(0.0)
            list.append(0.0)
        else:
            list.append(self.averageDowntime(self.log))
            list.append(self.averageSearchtime(self.log))
            list.append(self.inputSpeed(self.log))
            list.append(0.0)
            list.append(0.0)
        return list

    def refreshData(self):
        dataReader = DataReader("/proc/keymonitoring")
        list = dataReader.get()
        if list:
            self.db.insertLogByName(self.user, list)

        self.log = self.db.selectLogByName(self.user)
        self.stats = self.formStats()
        self.refreshDataSignal.emit([self.stats, self.log])