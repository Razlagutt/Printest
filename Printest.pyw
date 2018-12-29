# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
from ctypes import *
import Printest_uis
import sqlite3
import win32print
import win32api
import os
import sys
import re

class printTest(QMainWindow, Printest_uis.Ui_Printest):
    def __init__(self):
        super(printTest, self).__init__()
        self.setupUi(self)
        self.btn_getPrinters.clicked.connect(self.getPrinterList)
        self.btn_saveList.clicked.connect(self.savePrinterList)
        self.btn_UndoList.clicked.connect(self.getDefaultPrintList)
        self.listPrinters.doubleClicked.connect(self.printPage)


    def getRootDir(self, *args):
        if getattr(sys, 'Printest.exe', False):
            application_path = toLongName(os.path.abspath(os.path.dirname(sys.executable)))
        else:
            application_path = os.path.dirname(__file__)
        if args:
            application_path = os.path.join(application_path, os.path.join(*args))
        application_path = application_path.replace('\\','/')
        return application_path


    def toLongName(self, path):
        ''' from dos 8.3 format '''
        buf = create_unicode_buffer(500)
        windll.kernel32.GetLongPathNameW(unicode(path), buf, 500)
        return buf.value


    def getPrinterList(self):
        self.listPrinters.clear()
        self.listPrinters.addItems([p.printerName() for p in QPrinterInfo.availablePrinters()])


    def getDefaultPrintList(self):

        try:
            dbOpen = sqlite3.connect(os.path.join(self.getRootDir(), r"db\PrinterBase.db"))
        #if dbOpen:
            self.listPrinters.clear()
            self.statusBar.showMessage("Соединение с базой установлено.")
            cur = dbOpen.cursor()
            cur.execute("SELECT * FROM Printers")
            PrintList = cur.fetchall()
            if PrintList:
                [self.listPrinters.addItem(p[0]) for p in PrintList]
            else:
                self.getPrinterList()
            dbOpen.commit()
            cur.close()
            dbOpen.close()
        except:
            self.statusBar.showMessage("Нет соединения с базой.")



    def savePrinterList(self):
        dbOpen = sqlite3.connect(os.path.join(self.getRootDir(), r"db\PrinterBase.db"))
        if dbOpen:
            self.statusBar.showMessage("Список сохранен.")
            cur = dbOpen.cursor()
            cur.execute("DELETE FROM Printers")
            dbOpen.commit()

            sql = "INSERT INTO Printers (Printer) VALUES (?)"
            cur.executemany(sql, [(self.listPrinters.item(p).text(),) for p in range(self.listPrinters.count())])
            dbOpen.commit()
            cur.close()
        else:
            self.statusBar.showMessage("Нет соединения с базой.")
        dbOpen.close()


    def delPrinter(self):
        [self.listPrinters.takeItem(self.listPrinters.indexFromItem(s).row()) for s in self.listPrinters.selectedItems()]


    def printPage(self):
        '''for p in QPrinterInfo.availablePrinters():
            if self.listPrinters.currentItem().text() == p.printerName():
                f = open(".\textpage.html")
                pageList = f.readlines()
                page = ''
                for pl in pageList:
                    pl = pl.replace('\n', '')
                    page += pl
                textHTML = QTextDocument()
                textHTML.setHtml(page)
                printer = QPrinter(p)
                textHTML.print_(printer)
                f.close()'''
        win32print.SetDefaultPrinter(self.listPrinters.currentItem().text())
        mess = 'Текущий принтер: {0}'.format(self.listPrinters.currentItem().text())
        self.statusBar.showMessage(mess)
        if not self.checkBox.isChecked():
            f = open(os.path.join(self.getRootDir(), "textpage.html"))
            pageList = f.readlines()
            page = ''
            for p in pageList:
                p = p.replace('\n', '')
                page += p
            textHTML = QTextDocument()
            textHTML.setHtml(page)
            printer = QPrinter()
            printer.setPageMargins(1, 1, 1, 1, printer.Point)
            textHTML.print_(printer)
            f.close()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.delPrinter()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.printPage()


if __name__ == '__main__':
    app = QApplication([])
    w = printTest()
    w.move(app.desktop().width()-380, app.desktop().height()-410)
    w.getDefaultPrintList()
    w.show()
    app.exec_()