# models.py database wrapper
# Savital https://github.com/Savital

import sqlite3

class KeypadMonitoringDB():
    def __init__(self):
        super(self).__init__()
        #self.construct()

    def connect(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()

    # Table Users
    def createTableUsers(self):
        sql = """CREATE TABLE IF NOT EXISTS users(name TEXT)"""
        self.cursor.execute(sql)
        self.conn.commit()

    def dropTableUsers(self):
        sql = "'DROP TABLE IF EXISTS users'"
        self.cursor.execute(sql)
        self.conn.commit()

    def insertUserTest(self):
        sql = """INSERT INTO users VALUES ('testUser')"""
        self.cursor.execute(sql)
        self.conn.commit()

    def deleteUserTest(self):
        sql = "DELETE FROM albums WHERE artist = 'John Doe'"
        self.cursor.execute(sql)
        self.conn.commit()
