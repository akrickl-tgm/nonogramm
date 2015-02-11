__author__ = 'Astrid Krickl'
__author__ = "Berkan Seckin"

from nono.model import *
from nono.view2 import Ui_MainWindow
from nono.MyMessage import Dialog
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
        """
        konstruktor der das setup und das connecten der buttons macht
        """
        # GUI setup - view2 file wird nicht verandert
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # buttons mit den jeweiligen methoden verbinden
        self.ui.pushButton.clicked.connect(self.handlenew)
        self.ui.pushButton_2.clicked.connect(self.handlesolution)

        # zellen des spielfelds mit entsprechender methode verbinden
        self.ui.tableWidget.cellClicked.connect(self.cell_was_clicked)

        # setzen des texts default texts im textfeld
        self.ui.lineEdit.setText(_fromUtf8("new"))

        # Model anlegen
        self.mo = Model()

        # spielfeld herrichten
        self.handlenew()

        # textfeld auf nicht auswählbar setzen
        self.ui.lineEdit.setEnabled(False)

        # attribute
        self.geklickteFelder_list = []
        self.felderoffen
        self.dia = None

    def cell_was_clicked(self, row, column):
        """
        wenn eine Zelle des Spielfelds angeklickt wurde wird diese methode aufgerufen, die dann
        die zelle entsprechend einfaerbt

        :param row: reihe der zelle

        :param column:  spalte der zelle
        """
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
        """
        checkt ob der zug richtig war

        :param row: reihe des gewaehlten elements

        :param column:  spalte des gewaehlten elements

        """
        lo = self.mo.getLosung()
        if str(lo[row][column]) == str(self.ui.tableWidget.item(row, column).whatsThis()):
            if lo[row][column] == 1:
                self.felderoffen -= 1
        else:
            self.felderoffen += 1
        self.ui.lineEdit.setText("%s" % self.felderoffen)

        if self.felderoffen == 0:
            #you won
            self.dia = Dialog()
            self.dia.setGeometry(QtGui.QRect(100, 100, 400, 200))
            self.dia.show()
            self.ui.tableWidget.setEnabled(False)


    def handlenew(self):
        """
        handling fuer den neues spiel button
        leert das spielfeld und setzt alle werte auf ein neues spiel
        """
        self.ui.tableWidget.setEnabled(True)

        self.mo.getpic(15)
        self.setSpalten(self.mo.getSpalten())
        self.setZeilen(self.mo.getZeilen())

        self.ui.lineEdit.setText("%s" % self.mo.getOffen(15))
        self.felderoffen = self.mo.getOffen(15)
        for y in range(15):
           for x in range(15):
               self.ui.tableWidget.setItem(y, x, QtGui.QTableWidgetItem())
               self.ui.tableWidget.item(y, x).setBackground(QtGui.QColor(255, 255, 135))

        # um die groesse des gewünschten spielfelds zu ermitteln
        # 0 easy - 1 medium - 2 hard - 3 impossible
        index = self.ui.comboBox.currentIndex()
        # groessenveraenderung des spielfelds noch nicht vorhanden

    def handlesolution(self):
        """
        handling fuer den losungs button
        projeziert die losung auf die spielflaeche
        """
        losung = self.mo.getLosung()
        self.ui.tableWidget.setEnabled(False)
        for y in range(15):
           for x in range(15):
               self.ui.tableWidget.setItem(y, x, QtGui.QTableWidgetItem())
               self.ui.tableWidget.item(y, x).setBackground(QtGui.QColor(255, 255, 135))

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
        """
        setzt die nummern der spalten tipps auf die GUI

        :param ar:  array mit den zahlen in entsprechendem format
        """
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
        """
        setzt die nummern der zeilen tipps auf die GUI

        :param ar:  array mit den zahlen in entsprechendem format

        """
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
