# models.py Logbase wrapper
# Savital https://github.com/Savital

import sqlite3

# KeypadMonitoringDB is model, wraps the sqlite3 DB
class KeypadMonitoringDB():
    createTableUsersSQL = "CREATE TABLE IF NOT EXISTS users(username CHAR)"
    dropTableUsersSQL = "DROP TABLE IF EXISTS users"
    selectUsersSQL = "SELECT * FROM users"
    selectUsersByNameSQL = "SELECT * FROM users WHERE username='{0}'"
    insertUserSQL = "INSERT INTO users VALUES ('{0}')"
    deleteUserSQL = "DELETE FROM users WHERE username = '{0}'"

    createTableLogSQL = "CREATE TABLE IF NOT EXISTS log(username CHAR, scancode INT, downtime INT, searchtime INT, keyname CHAR)"
    dropTableLogSQL = "DROP TABLE IF EXISTS log"
    selectLogSQL = "SELECT * FROM log"
    selectLogByNameSQL = "SELECT * FROM log WHERE username='{0}'"
    insertLogByNameSQL = "INSERT INTO log VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
    deleteLogByNameSQL = "DELETE FROM log WHERE username = '{0}'"

    def __init__(self):
        super(KeypadMonitoringDB, self).__init__()
        self.construct()

    def construct(self):
        pass

    # Table Users
    def createTableUsers(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.createTableUsersSQL)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def dropTableUsers(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.dropTableUsersSQL)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def selectUsers(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.selectUsersSQL)
        results = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return results

    def selectUsersByName(self, name):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.selectUsersByNameSQL.format(name))
        results = self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        return results

    def insertUser(self, name):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.insertUserSQL.format(name))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def deleteUser(self, name):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.deleteUserSQL.format(name))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    # Table Log
    def createTableLog(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.createTableLogSQL)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def dropTableLog(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.dropTableLogSQL)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def selectLog(self):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.selectLogSQL)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def selectLogByName(self, name):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.selectLogByNameSQL.format(name))
        results = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return results

    def insertLogByName(self, name, list):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        if len(list) == 0:
            pass
        elif len(list[0]) == 1:
            self.cursor.execute(self.insertLogByNameSQL.format(name, list[0], list[1], list[2], list[3]))
        else:
            for item in list:
                self.cursor.execute(self.insertLogByNameSQL.format(name, item[0], item[1], item[2], item[3]))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def deleteLogByName(self, name):
        self.conn = sqlite3.connect("keypadMonitoringDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.deleteLogByNameSQL.format(name))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def hello(self):
        return True