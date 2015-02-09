__author__ = 'Astrid Krickl'
from nono.view import *
from nono.model import *


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
    def __init__(self):
        self.mo = Model()
        self.spielfeld = None
        self.hintzeile = None
        self.hintspalte = None
        self.ansicht = None

    def setView(self, view):
        self.ansicht = view
        print("geklappt")

    def feldclicked(self, row, col):
        """
        buttonfarbe ändern, textfeld felder offen ändern
        http://pyqt.sourceforge.net/Docs/PyQt4/qtablewidgetitem.html#isSelected
        :return:
        """
        # self.ansicht.changeFeld(self.ansicht, "20")
        pass

    def losen(self):
        print("Bitte lösen - Button wurde gedrückt")
        # self.ansicht.printTest()
        # print(self.ansicht)
        print(self.ansicht.getLevel())

    def neues(self):
        """
        print("TEST")
        View.spielfeld = Model.getPic(groesse)
        View.tipsspalten = Model.getSpalten()
        View.tipszeilen = Model.getZeilen()
        # View.repaint()
        """
        print(self.ansicht.getLevel())
        print("Neustart - Button wurde gedrückt")
"""
        Model.getpic(self.mo, groesse)
        self.spielfeld = Model.getLosung(self.mo)
        self.hintspalte = Model.getSpalten(self.mo)
        self.hintzeile = Model.getZeilen(self.mo)

        self.ansicht.setSpielfeld(self.spielfeld)
        self.ansicht.setHintSpalte(self.hintspalte)
        self.ansicht.setHintZeile(self.hintzeile)
"""



