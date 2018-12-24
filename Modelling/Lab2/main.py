import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
import random
import math 
from itertools import islice

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("MainWIndow.ui", self)
        self.construct()

    def construct(self):
        self.entropyAlg1.setReadOnly(True)
        self.entropyAlg2.setReadOnly(True)
        self.entropyAlg3.setReadOnly(True)
        self.entropyTabular1.setReadOnly(True)
        self.entropyTabular2.setReadOnly(True)
        self.entropyTabular3.setReadOnly(True)
        self.entropyHandle.setReadOnly(True)

        self.fillAlgButton.clicked.connect(lambda: onfillAlgButtonClick(self))
        self.fillTabularButton.clicked.connect(lambda: onfillTabularButtonClick(self))
        self.inputHandle.returnPressed.connect(lambda: onInputHandleEnter(self))

        self.algTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabularTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.lineQuantity = 0

        for i in range(10):
            self.algTable.insertRow(i)

        for i in range(10):
            self.tabularTable.insertRow(i)

# Count entropy of numeric sequence by deviding the hist element on number of this element in dictionary
def CalculateEntropy(sequence):
    count = len(sequence) 
    if count <= 1:
        return 0

    hist = dict()
    for el in sequence:
        if el not in hist.keys():
            hist.update({el: 1})
        else:
            hist[el] += 1
    
    entropy = 0
    for el in hist.keys():
        p = hist[el] / count
        entropy -= p * math.log(p, count)
    
    return entropy

def onfillAlgButtonClick(window):
    table = window.algTable
    random.seed()
    oneDigit = [random.randint(0, 9) for i in range(1000)]
    twoDigits = [random.randint(10, 99) for i in range(1000)]
    threeDigits = [random.randint(100, 999) for i in range(1000)]
    for i in range(10):
        item = QTableWidgetItem(str(oneDigit[i]))
        table.setItem(i, 0, item)

    for i in range(10):
        item = QTableWidgetItem(str(twoDigits[i]))
        table.setItem(i, 1, item)

    for i in range(10):
        item = QTableWidgetItem(str(threeDigits[i]))
        table.setItem(i, 2, item)

    entropyOneDigit = CalculateEntropy(oneDigit)
    entropyTwoDigits = CalculateEntropy(twoDigits)
    entropyThreeDigits = CalculateEntropy(threeDigits)
    window.entropyAlg1.setText('{:.4%}'.format(entropyOneDigit))
    window.entropyAlg2.setText('{:.4%}'.format(entropyTwoDigits))
    window.entropyAlg3.setText('{:.4%}'.format(entropyThreeDigits))

def onfillTabularButtonClick(window):
    table = window.tabularTable
    numbers = set()
    with open('digits.txt') as file: 
        lines = islice(file, window.lineQuantity, None)
        for l in lines:
            numbers.update(set(l.split(" ")[1:-1]))
            window.lineQuantity += 1
            if len(numbers) >= 3001:
                break
        numbers.remove("") 
        numbers = list(numbers)[:3000]
    oneDigit = [int(i)%9 + 1 for i in numbers[:1000]]
    twoDigits = [int(i)%90 + 10 for i in numbers[1000:2000]]
    threeDigits = [int(i)%900 + 100 for i in numbers[2000:3000]]
    
    for i in range(10):
        item = QTableWidgetItem(str(oneDigit[i]))
        table.setItem(i, 0, item)

    for i in range(10):
        item = QTableWidgetItem(str(twoDigits[i]))
        table.setItem(i, 1, item)

    for i in range(10):
        item = QTableWidgetItem(str(threeDigits[i]))
        table.setItem(i, 2, item)

    entropyOneDigit = CalculateEntropy(oneDigit)
    entropyTwoDigits = CalculateEntropy(twoDigits)
    entropyThreeDigits = CalculateEntropy(threeDigits)
    window.entropyTabular1.setText(' {:.4%}'.format(entropyOneDigit))
    window.entropyTabular2.setText(' {:.4%}'.format(entropyTwoDigits))
    window.entropyTabular3.setText(' {:.4%}'.format(entropyThreeDigits))

def onInputHandleEnter(window):
    input = window.inputHandle
    entropy = window.entropyHandle
    sequence = input.text().split(" ")
    filteredSequence = []
    for i in sequence:
        try:
            int(i)
        except ValueError:
            continue
        else:
            filteredSequence.append(i)

    entropy = CalculateEntropy(list(map(lambda x: int(x), filteredSequence)))
    window.entropyHandle.setText(' {:.4%}'.format(entropy))

def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

run()