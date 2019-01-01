# manager.py Manager control
# Savital https://github.com/Savital

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from views import MainWindow
from models import KeypadMonitoringDB as db

class Manager(QtCore.QObject):
    doneMonitoringSignal = QtCore.pyqtSignal()
    doneAddUserSignal = QtCore.pyqtSignal()
    doneDeleteUserSignal = QtCore.pyqtSignal()
    doneClearLogSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Manager, self).__init__()
        self.construct()

    def construct(self):
        pass

    def connects(self):
        self.window.monitoringSignal.connect(self.monitoring)
        self.window.addUserSignal.connect(self.AddUser)
        self.window.deleteUserSignal.connect(self.DeleteUser)
        self.window.clearLogSignal.connect(self.ClearLog)

        self.doneMonitoringSignal.connect(self.window.onMonitoringRevertSignal)
        self.doneAddUserSignal.connect(self.window.onAddUserRevertSignal)
        self.doneDeleteUserSignal.connect(self.window.onDeleteUserRevertSignal)
        self.doneClearLogSignal.connect(self.window.onClearLogRevertSignal)

    def runApp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()
        self.connects()
        sys.exit(self.app.exec_())

    def testDB(self):
        db.connect(db)
        db.createTableUsers(db)
        db.insertUserTest(db)
        #db.deleteUserTest(db)
        db.disconnect(db)

    @QtCore.pyqtSlot()
    def monitoring(self):
        print("Manager.Monitoring()")
        self.doneMonitoringSignal.emit()

    @QtCore.pyqtSlot()
    def AddUser(self):
        print("Manager.AddUser()")
        self.doneAddUserSignal.emit()

    @QtCore.pyqtSlot()
    def DeleteUser(self):
        print("Manager.DeleteUser()")
        self.doneDeleteUserSignal.emit()

    @QtCore.pyqtSlot()
    def ClearLog(self):
        print("Manager.ClearLog()")
        self.doneClearLogSignal.emit()