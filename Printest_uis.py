# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python34\Printest.ui'
#
# Created: Sat Feb  7 00:26:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Printest(object):
    def setupUi(self, Printest):
        Printest.setObjectName("Printest")
        Printest.resize(350, 340)
        Printest.setMinimumSize(QtCore.QSize(350, 340))
        Printest.setMaximumSize(QtCore.QSize(350, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Printest.setWindowIcon(icon)
        self.widget = QtGui.QWidget(Printest)
        self.widget.setMinimumSize(QtCore.QSize(350, 320))
        self.widget.setMaximumSize(QtCore.QSize(350, 320))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.listPrinters = QtGui.QListWidget(self.widget)
        self.listPrinters.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listPrinters.setObjectName("listPrinters")
        self.verticalLayout.addWidget(self.listPrinters)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_getPrinters = QtGui.QPushButton(self.widget)
        self.btn_getPrinters.setText("")
        self.btn_getPrinters.setIcon(icon)
        self.btn_getPrinters.setObjectName("btn_getPrinters")
        self.horizontalLayout.addWidget(self.btn_getPrinters)
        self.btn_saveList = QtGui.QPushButton(self.widget)
        self.btn_saveList.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ico/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_saveList.setIcon(icon1)
        self.btn_saveList.setObjectName("btn_saveList")
        self.horizontalLayout.addWidget(self.btn_saveList)
        self.btn_UndoList = QtGui.QPushButton(self.widget)
        self.btn_UndoList.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ico/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_UndoList.setIcon(icon2)
        self.btn_UndoList.setObjectName("btn_UndoList")
        self.horizontalLayout.addWidget(self.btn_UndoList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        Printest.setCentralWidget(self.widget)
        self.statusBar = QtGui.QStatusBar(Printest)
        self.statusBar.setObjectName("statusBar")
        Printest.setStatusBar(self.statusBar)

        self.retranslateUi(Printest)
        QtCore.QMetaObject.connectSlotsByName(Printest)

    def retranslateUi(self, Printest):
        Printest.setWindowTitle(QtGui.QApplication.translate("Printest", "Printest", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Printest", "Запретить печать", None, QtGui.QApplication.UnicodeUTF8))

