__author__ = 'Berkan Seckin'
from control import *

class View():
    """
    buttons array etc
    """
    spielfeld = []
    tipszeilen = []  # nummern auf der seite zeilen
    tipsspalten = []  # nummern auf der seite spalten

    button.connect(Control.feldclicked())
