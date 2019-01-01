# manager.py Manager control
# Savital https://github.com/Savital

from views import MainWindow
from models import KeypadMonitoringDB as db

class Manager():
    def __init__(self):
        super(self).__init__()
        self.construct()

    def construct(self):
        print("manager.construct()")

    def testDB(self):
        db.connect(db)
        db.createTableUsers(db)
        db.insertUserTest(db)
        #db.deleteUserTest(db)
        db.disconnect(db)