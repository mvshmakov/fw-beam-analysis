# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-src/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName('centralWidget')
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 114, 32))
        self.pushButton.setObjectName('pushButton')
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 261, 221))
        self.graphicsView.setObjectName('graphicsView')
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName('menuBar')
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName('statusBar')
        MainWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName('mainToolBar')
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setCheckable(True)
        self.actionAbout.setObjectName('actionAbout')
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setCheckable(True)
        self.actionAuthor.setObjectName('actionAuthor')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'))
        self.pushButton.setText(_translate('MainWindow', 'Simulate'))
        self.actionAbout.setText(_translate('MainWindow', 'About'))
        self.actionAuthor.setText(_translate('MainWindow', 'Author'))
