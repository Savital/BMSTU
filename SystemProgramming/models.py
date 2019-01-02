# models.py database wrapper
# Savital https://github.com/Savital

import sqlite3

class KeypadMonitoringDB():
    createTableUsersSQL = """CREATE TABLE IF NOT EXISTS users(name TEXT)"""
    dropTableUsersSQL = """DROP TABLE IF EXISTS users"""
    insertUserSQL = "INSERT INTO users VALUES ('{0}')"
    deleteUserSQL = "DELETE FROM users WHERE name = '{0}'"
    selectUsersSQL = """SELECT * FROM users"""
    selectUsersByNameSQL = "SELECT * FROM users WHERE name='{0}'"
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

    def selectUsers(self):
        self.cursor.execute(self.selectUsersSQL)
        results = self.cursor.fetchall()
        return results

    def selectUsersByName(self, name):
        self.cursor.execute(self.selectUsersByNameSQL.format(name))
        results = self.cursor.fetchone()
        return results

    def insertUser(self, name):
        self.cursor.execute(self.insertUserSQL.format(name))
        self.conn.commit()

    def deleteUser(self, name):
        self.cursor.execute(self.deleteUserSQL.format(name))
        self.conn.commit()