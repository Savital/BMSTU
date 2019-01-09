import sys
sys.path.append("../")
from models import KeypadMonitoringDB

import unittest
import sqlite3
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock


class ModelsTest(unittest.TestCase):
    def setUp(self):
        self.db = KeypadMonitoringDB()
        self.db.dropTableUsers()

    def tearDown(self):
        self.db.dropTableUsers()

    def testSelectUsers_IfEmpty(self):
        self.db.createTableUsers()

        results = self.db.selectUsers()

        self.assertEqual(results, [])

    def testSelectUsers_IfOne(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser")
        results = self.db.selectUsers()

        self.assertEqual(results, [('TestUser',)])

    def testSelectUsers_IfMany(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser1")
        self.db.insertUser("TestUser2")
        self.db.insertUser("TestUser3")
        results = self.db.selectUsers()

        self.assertEqual(results, [('TestUser1',), ('TestUser2',), ('TestUser3',)])

    def testSelectUsersByName_IfEmpty(self):
        self.db.createTableUsers()

        results = self.db.selectUsersByName("WrongUser")

        self.assertEqual(results, None)

    def testSelectUsersByName_IfExists(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser1")
        self.db.insertUser("TestUser2")
        self.db.insertUser("TestUser3")
        results = self.db.selectUsersByName("TestUser2")

        self.assertEqual(results, ('TestUser2',))

    def testSelectUsersByName_IfNotExists(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser1")
        self.db.insertUser("TestUser2")
        self.db.insertUser("TestUser3")
        results = self.db.selectUsersByName("WrongUser")

        self.assertEqual(results, None)

    def testInsertUser_IfOne(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser")
        results = self.db.selectUsers()

        self.assertEqual(results, [('TestUser',)])

    def testInsertUser_IfMany(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser1")
        self.db.insertUser("TestUser2")
        self.db.insertUser("TestUser3")
        results = self.db.selectUsers()

        self.assertEqual(results, [('TestUser1',), ('TestUser2',), ('TestUser3',)])

    def testDeleteUser_IfEmpty(self):
        self.db.createTableUsers()

        self.db.deleteUser("TestUser")
        results = self.db.selectUsers()

        self.assertEqual(results, [])

    def testDeleteUser_IfOne(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser")
        self.db.deleteUser("TestUser")
        results = self.db.selectUsers()

        self.assertEqual(results, [])

    def testDeleteUser_IfMany(self):
        self.db.createTableUsers()

        self.db.insertUser("TestUser1")
        self.db.insertUser("TestUser2")
        self.db.insertUser("TestUser3")
        self.db.deleteUser("TestUser2")
        results = self.db.selectUsers()

        self.assertEqual(results, [('TestUser1',), ('TestUser3',)])

    def testSelectLog(self):
        pass

    def testSelectLogByName(self):
        pass

    def testInsertLog(self):
        pass

    def testDeleteLog(self):
        pass

if __name__ == '__main__':
    unittest.main()