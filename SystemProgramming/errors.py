# Savital https://github.com/Savital
# Errors for keypad monitoring project
"""
from PyQt5.QtWidgets import QMessageBox

# Base Class for Exceptions
class Error(Exception):
    pass

class ErrorMessage():
    def __init__(self, window, msg):
        self.msg = msg
        self.reply = QMessageBox.critical(window, 'Ошибка', msg, QMessageBox.Ok)
"""

class ErrorsHandler():
    OK = 0
    ALREADY_EXISTS = -1
    EMPTY_NAME = -2

    errors = {"OK" : "", "ALREADY_EXISTS" : "", "EMPTY_NAME ": ""}

    def __init__(self):
        pass

    def __del__(self):
        pass

