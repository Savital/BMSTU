# models.py database wrapper
# Savital https://github.com/Savital

import sqlite3

class KeypadMonitoringDB():
    createTableUsersSQL = """CREATE TABLE IF NOT EXISTS users(name TEXT)"""
    dropTableUsersSQL = """DROP TABLE IF EXISTS users"""
    insertUserSQL = """INSERT INTO users VALUES ('testUser')"""
    deleteUserSQL = """DELETE FROM users WHERE name = 'testUser'"""
    def __init__(self):
        super(KeypadMonitoringDB, self).__init__()
        self.construct()

    def construct(self):
        pass

    def connect(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()

    # Table Users
    def createTableUsers(self):
        self.cursor.execute(self.createTableUsersSQL)
        self.conn.commit()

    def dropTableUsers(self):
        self.cursor.execute(self.dropTableUsersSQL)
        self.conn.commit()

    def insertUserTest(self):
        self.cursor.execute(self.insertUserSQL)
        self.conn.commit()

    def deleteUserTest(self):
        self.cursor.execute(self.deleteUserSQL)
        self.conn.commit()
