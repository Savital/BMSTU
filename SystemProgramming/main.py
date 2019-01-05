# main.py launch script
# Savital https://github.com/Savital

from manager import Manager
from reader import DataReader

def main():
    #controller = Manager()
    #controller.runApp()
    #Manager.runApp(Manager)
    dataReader = DataReader("/proc/keymonitoring")
    dataReader.get()

main()
