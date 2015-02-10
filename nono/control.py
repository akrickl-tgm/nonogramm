__author__ = 'Astrid Krickl'
from nono.view import *
from nono.model import *
from PyQt4 import QtGui


"""
alle buttons haben 3 zustände
-1 unbestimmt (lila?)
0 weiss
1 schwarz

wenn man auf ein feld drauf klickt kommt man von lila zu weiss und dann zu schwarz und dann wieder zu lila ....
textfeld felder offen zeigt anzahl der lila felder an + falsch angekreuzte (wird nach jdm klick gechekt)
neustart alles löschen neues puzzle generieren
lösen alle felder fertig einfärben
"""


class Control():

    def __init__(self, view):
        self.mo = Model()
        self.spielfeld = None
        self.hintzeile = None
        self.hintspalte = None
        self.ansicht = view
        self.offen = 100

    def feldclicked(self, row, col, color, element):
        """
        buttonfarbe ändern, textfeld felder offen ändern
        http://pyqt.sourceforge.net/Docs/PyQt4/qtablewidgetitem.html#isSelected
        wird auf actionlistener aufgerufen muss man noch einsetllen
        :return:
        """
        # farbe vom feld umaender muss im controller noch ausprogrammiert werden
        if color == 'white':
            cl = 1
            element.changeColor ('black')
        elif color == 'black':
            cl = 0
            element.changeColor ('yellow')
        elif color == 'yellow':
            cl = -1
            element.changeColor ('white')

        if self.spielfeld[row][col] == cl and element != 'black':
            self.offen -= 1

    def losen(self):
        print("Bitte loesen - Button wurde gedrueckt")
        self.ansicht.setSpielfeld(self.spielfeld)

    def neues(self):
        """
        print("TEST")
        View.spielfeld = Model.getPic(groesse)
        View.tipsspalten = Model.getSpalten()
        View.tipszeilen = Model.getZeilen()
        # View.repaint()
        """
        # algorithmus vorbereiten
        self.mo.getpic(self.ansicht.getLevel())
        self.hintspalte = self.mo.getSpalten()
        self.hintzeile = self.mo.getZeilen()

        #Werte in die GUI einfügen und spielfeld saubern
        self.ansicht.clearFeld()
        self.ansicht.setHintSpalte(self.hintspalte)
        self.ansicht.setHintZeile(self.hintzeile)

        #print(self.ansicht.getLevel())
        print("Neustart - Button wurde gedrückt")

#START:
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
