# main.py MainWindow launch script
# Savital https://github.com/Savital

import sys
from PyQt5.QtWidgets import QApplication
from views import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()

