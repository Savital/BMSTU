import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

import matplotlib.pyplot as pit

from scipy.stats import uniform
from scipy.stats import expon

import numpy as np

class DistributionsGetVectors(QtCore.QObject):
    emitter = QtCore.pyqtSignal(list)

    def exec(self, param1, param2, isUniform=True):
        data0 = []
        data1 = []
        data2 = []

        if isUniform:
            delta = abs(param1 - param2)
            data0 = np.linspace(param1 - 0.1 * delta, param2 + 0.1 * delta, 1000)
            dist = uniform(loc=param1, scale=delta)
            data1 = dist.pdf(data0)
            data2 = dist.cdf(data0)
        else:
            data0 = np.linspace(expon.ppf(0.0001), expon.ppf(0.999999), 1000)
            dist = expon(scale = 1/param1)
            data1 = dist.pdf(data0)
            data2 = dist.cdf(data0)

        self.emitter.emit([data0, data1, data2])


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Построение графиков распределений СВ')
        self.construct()

        self.DistributionsGetVectors = DistributionsGetVectors()
        self.DistributionsGetVectors.emitter.connect(self.showGraphics)

    def construct(self):
        self.radioUniform = QtWidgets.QRadioButton(self)
        self.radioUniform.setText('Равномерное распределение')
        self.radioUniform.clicked.connect(self.on_radioUniform_clicked)
        self.radioExponential = QtWidgets.QRadioButton(self)
        self.radioExponential.setText('Экспоненциальное распределение')
        self.radioExponential.clicked.connect(self.on_radioExponential_clicked)
        self.radioUniform.setChecked(True)
        self.chooseDistributions = QtWidgets.QGroupBox(self)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.addWidget(self.radioUniform)
        self.hbox.addWidget(self.radioExponential)
        self.chooseDistributions.setLayout(self.hbox)

        self.param1Label = QtWidgets.QLabel(self)
        self.param1Label.setText('a = ')
        self.param1 = QtWidgets.QDoubleSpinBox(self)
        self.param1.setMinimum(-1000)
        self.param1.setMaximum(1000)
        self.param1Group = QtWidgets.QGroupBox(self)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.addWidget(self.param1Label)
        self.hbox.addWidget(self.param1, 2)
        self.param1Group.setLayout(self.hbox)

        self.param2Label = QtWidgets.QLabel(self)
        self.param2Label.setText('b = ')
        self.param2 = QtWidgets.QDoubleSpinBox(self)
        self.param2.setMinimum(-1000)
        self.param2.setMaximum(1000)
        self.param2Group = QtWidgets.QGroupBox(self)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.addWidget(self.param2Label)
        self.hbox.addWidget(self.param2, 2)
        self.param2Group.setLayout(self.hbox)

        self.pushButtonPlot = QtWidgets.QPushButton(self)
        self.pushButtonPlot.setText("Построить графики")
        self.pushButtonPlot.clicked.connect(self.on_pushButtonPlot_clicked)

        self.OptionsGroup = QtWidgets.QGroupBox(self)
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.addWidget(self.chooseDistributions)
        self.vbox.addWidget(self.param1Group)
        self.vbox.addWidget(self.param2Group)
        self.vbox.addWidget(self.pushButtonPlot)
        self.OptionsGroup.setLayout(self.vbox)

        self.layoutGrid = QtWidgets.QGridLayout(self)
        self.layoutGrid.addWidget(self.OptionsGroup, 0, 0)

        self.param1.setValue(0)
        self.param2.setValue(1)

    @QtCore.pyqtSlot(list)
    def showGraphics(self, data):
        figure = pit.figure(figsize=(5,5))
        pit.title('Плотность распределения СВ', color='green')
        axis = figure.add_subplot(111)
        axis.plot(data[0], data[1], color='green')
        axis.set_xlabel('x')
        axis.set_ylabel('f(x)')
        figure = pit.figure(figsize=(5,5))
        pit.title('Функция распределения СВ', color='red')
        axis = figure.add_subplot(111)
        axis.plot(data[0], data[2], color='red')
        axis.set_xlabel('x')
        axis.set_ylabel('F(x)')
        pit.show()

    @QtCore.pyqtSlot()
    def on_pushButtonPlot_clicked(self):
        if self.radioUniform.isChecked() and self.param1.value() >= self.param2.value():
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Параметр b должен быть больше, чем параметр a!')
            msg.show()
            return
        self.DistributionsGetVectors.exec(self.param1.value(), self.param2.value(),
                                        self.radioUniform.isChecked())

    @QtCore.pyqtSlot()
    def on_radioUniform_clicked(self):
        self.param2Group.show()
        self.param1Label.setText('a = ')
        self.param2Label.setText('b = ')
        self.param1.setMinimum(-1000)
        self.param2.setMinimum(-1000)
        self.param1.setMaximum(1000)
        self.param2.setMaximum(1000)
        self.param1.setValue(0)
        self.param2.setValue(1)
        self.param2.setDecimals(2)

    @QtCore.pyqtSlot()
    def on_radioExponential_clicked(self):
        self.param2Group.hide()
        self.param1Label.setText('λ = ')
        self.param2Label.setText('not defined')
        self.param1.setMinimum(0.01)
        self.param2.setMinimum(0)
        self.param2.setMaximum(0)
        self.param1.setValue(1)
        self.param2.setValue(0)
        self.param2.setDecimals(0)

def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Построение графиков распределений СВ')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

run()