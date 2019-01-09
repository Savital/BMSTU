# Savital https://github.com/Savital
# Errors for keypad monitoring project

from PyQt5.QtWidgets import QMessageBox

# Base Class for Exceptions
class Error(Exception):
    pass

class ErrorMessage():
    def __init__(self, window, msg):
        self.msg = msg
        self.reply = QMessageBox.critical(window, 'Ошибка', msg, QMessageBox.Ok)

