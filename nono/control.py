__author__ = 'Astrid Krickl'
#from nono.view import *
from nono.model import *
from nono.view2 import Ui_MainWindow
from PyQt4 import QtGui, QtCore

import sys

try:
     _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Spiel(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handlenew)
        self.ui.pushButton_2.clicked.connect(self.handlesolution)

        self.ui.tableWidget.cellClicked.connect(self.cell_was_clicked)

        self.ui.lineEdit.setText(_fromUtf8("new"))

        self.mo = Model()
        self.handlenew()

        self.geklickteFelder_list = []
        self.felderoffen

    def cell_was_clicked(self, row, column):
        if [row, column] in self.geklickteFelder_list:

            feld = self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(255, 255, 135))  # weiß
            self.geklickteFelder_list.remove([row, column])
            self.ui.tableWidget.item(row, column).setWhatsThis(_fromUtf8("0"))
        else:
            self.ui.tableWidget.setItem(row, column, QtGui.QTableWidgetItem())
            feld = self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(81, 171, 255))  # blau
            self.ui.tableWidget.item(row, column).setWhatsThis(_fromUtf8("1"))
            self.geklickteFelder_list.append([row, column])
        self.check(row, column)

    def check(self, row, column):
        lo = self.mo.getLosung()
        if str(lo[row][column]) == str(self.ui.tableWidget.item(row, column).whatsThis()):
            self.felderoffen -= 1
            self.ui.lineEdit.setText("%s" % self.felderoffen)

    def handlenew(self):
        self.mo.getpic(15)
        self.setSpalten(self.mo.getSpalten())
        self.setZeilen(self.mo.getZeilen())

        self.ui.lineEdit.setText("%s" % self.mo.getOffen(15))
        self.felderoffen = self.mo.getOffen(15)
        for y in range(15):
           for x in range(15):
               self.ui.tableWidget.setItem(y, x, QtGui.QTableWidgetItem())
               feld = self.ui.tableWidget.item(y, x).setBackground(QtGui.QColor(255, 255, 135))

        index = self.ui.comboBox.currentIndex()
        #print(index)

    def handlesolution(self):
        losung = self.mo.getLosung()

        for y in range(15):
           for x in range(15):
               self.ui.tableWidget.setItem(y, x, QtGui.QTableWidgetItem())
               feld = self.ui.tableWidget.item(y, x).setBackground(QtGui.QColor(255, 255, 135))

        for y in range(15):
            for x in range(15):
                if losung[y][x] == 0:
                    self.ui.tableWidget.setItem(y, x, QtGui.QTableWidgetItem())
                    self.ui.tableWidget.item(y, x).setBackground(QtGui.QColor(81,171,255)) #blau
                    self.geklickteFelder_list = []
                if losung[y][x] == 1:
                    self.ui.tableWidget.setItem(y, x, QtGui.QTableWidgetItem())
                    self.ui.tableWidget.item(y, x).setBackground(QtGui.QColor(255, 255, 135)) #gelb
                    self.geklickteFelder_list = []

    def setSpalten(self, ar):
        for y in range(8):
            #spaltenDaten[y].sort()
            for x in range(15):
                if ar[y][x] == 0:
                    item = QtGui.QTableWidgetItem(" ")
                else:
                    item = QtGui.QTableWidgetItem("%s" % ar[y][x])
                self.ui.tableWidget_3.setItem(y, x, item)
                if x == 14:
                    break

    def setZeilen(self, ar):
        for y in range(15):
            #zeilenDaten[y].sort()
            for x in range(8):
                if ar[y][x] == 0:
                    item = QtGui.QTableWidgetItem(" ")
                else:
                    item = QtGui.QTableWidgetItem("%s" % ar[y][x])
                self.ui.tableWidget_2.setItem(y, x, item)
                if x == 7:
                    break


#START:
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Spiel()
    ex.show()
    sys.exit(app.exec_())
