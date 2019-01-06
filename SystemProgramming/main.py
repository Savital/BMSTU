# main.py launch script
# Savital https://github.com/Savital

from manager import Manager

def main():
    controller = Manager()
    controller.runApp()
    Manager.runApp(Manager)

main()
