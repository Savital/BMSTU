# Savital https://github.com/Savital
# manager.py Manager control

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from models.db import Users, Log
from models.parsers import ProcReader
from models.calcs import Calc
from models.timers import RefreshEventGenerator

from views.forms import MainForm

# Controller, handles signals between view and model
class Manager(QtCore.QObject):
    PROC_PATH = "/proc/keymonitoring"

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
        self.timer = RefreshEventGenerator(0.01, self.onRefreshEvent)
        self.timer.start()

    def __del__(self): #TODO
        self.timer.cancel()

    def construct(self):
        self.mUsers = Users()
        self.mLog = Log()
        self.mProcReader = ProcReader()
        self.mCalc = Calc()

        self.mUsers.createTable()
        self.mLog.createTable()

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

        self.window.closeSignal.connect(self.close)
        #Close when the thread terminated (TODO)

        self.refreshDataSignal.connect(self.window.onRefreshSignalReverted)


    def runApp(self):
        self.app = QApplication(sys.argv)
        self.window = MainForm()
        self.connects()
        self.window.show()
        sys.exit(self.app.exec_())

    @QtCore.pyqtSlot()
    def initWindow(self):
        self.users = self.mUsers.select()
        self.user = ""
        if len(self.users):
            self.user = self.users[0][0]

        self.doneInitSignal.emit([self.users])

    def refreshData(self):
        self.log = self.mLog.selectByName(self.user)
        self.stats = self.mCalc.formStats(self.log)


    def onRefreshEvent(self):
        list = self.mProcReader.get(self.PROC_PATH)
        if list:
            self.mLog.insert(self.user, list)

        self.refreshData()

        self.refreshDataSignal.emit([self.stats, self.log])

    @QtCore.pyqtSlot(list)
    def changeUserState(self, list):
        self.user = list[0]

        self.refreshData()

        self.doneChangeUserStateSignal.emit([self.stats, self.log])

    @QtCore.pyqtSlot()
    def monitoring(self):
        self.monitoringFlag = not self.monitoringFlag
        if self.monitoringFlag:
            list = self.mProcReader.get(self.PROC_PATH)
            self.timer.runF()
        else:
            self.timer.stopF()

        self.doneMonitoringSignal.emit([self.monitoringFlag])

    @QtCore.pyqtSlot(list)
    def addUser(self, list):
        if list[0] == "":
            self.doneAddUserSignal.emit(["EMPTY_NAME"])
            return

        names = self.mUsers.selectByName(list[0])
        if names == None:
            self.mUsers.insert(list[0])
            self.doneAddUserSignal.emit(["OK", list[0]])
        else:
            self.doneAddUserSignal.emit(["ALREADY_EXIST", list[0]])

    @QtCore.pyqtSlot(list)
    def deleteUser(self, list):
        names = self.mUsers.selectByName(list[0])
        if names != None:
            self.doneDeleteUserSignal.emit(["OK", list[0]])
            self.mUsers.delete(list[0])
        else:
            self.doneDeleteUserSignal.emit(["DOESNT_EXIST", list[0]])

    @QtCore.pyqtSlot()
    def clearLog(self):
        self.mLog.delete(self.user)
        self.doneClearLogSignal.emit()

    @QtCore.pyqtSlot()
    def close(self):
        self.timer.cancel()