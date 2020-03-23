#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv, exit
from gui import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow, Ui_MainWindow):
    title = 'FW-beam interation simulator'

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.simulateButton.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("clicked")


if __name__ == '__main__':
    app = QApplication(argv)

    window = MainWindow()
    window.setWindowTitle('FW-beam interation simulator')

    window.show()
    window.resize(500, 400)

    exit(app.exec_())
