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
    test = []
    def feldclicked(self):
        """
        buttonfarbe ändern, textfeld felder offen ändern
        :return:
        """
        pass

    def losen(self):
        print("Bitte lösen - Button wurde gedrückt")


    def neues(self):
        """
        print("TEST")
        View.spielfeld = Model.getPic(30)
        View.tipsspalten = Model.getSpalten()
        View.tipszeilen = Model.getZeilen()
        # View.repaint()
                """
        print ("Neustart - Button wurde gedrückt")