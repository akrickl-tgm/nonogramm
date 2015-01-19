__author__ = 'Astrid Krickl'
from random import *


class Control():
    losung = None
    spalten = []
    zeilen = []
    """

    """
    def getpic(self, breite):
        """
        man nimmt eine spaltenbreite (zeile = spalte)
        dann erstellt man ein array mit der größe breite²
        dies befüllt man mit random zahlen zwischen 0 und 1

        immer 'breitenanzahl' sind eine zeile
        und jedes 5te gehört zu der jeweiligen spalte
        dann zählt man die 1er und speichert sie in die jeweilige reihe bzw spalte
        und speichert die in ein 2d array (?)
        :param breite: breite des spielfelds
        :return:
        """
        #spielfeld generieren mit random zahlen in einem 2d array
        spielfeld = []
        for x in range(0, breite):
            spielfeld[x] = []
            for y in range(0, breite):
                spielfeld[x].append(round(random()))

        self.losung = spielfeld #losung speichern

        #spielfeld auszählen nur 1er
        #zeilen auslesen & ins attribut speichern
        self.zeilen = []
        zahler = 0
        for x in range(0, breite):
            for y in range(0, breite):
                if spielfeld[x][y] == 1:
                    ++zahler
                elif spielfeld[x][y] == 0:
                    if zahler > 0:
                        self.zeilen.append(zahler)
                        zahler = 0
        #spalten auslesen & ins attribut speichern
        self.spalten = []
        zahler = 0
        for x in range(0, breite):
            for y in range(0, breite):
                if spielfeld[y][x] == 1:
                    ++zahler
                elif spielfeld[y][x] == 0:
                    if zahler > 0:
                        self.spalten.append(zahler)
                        zahler = 0

    def getLosung(self):
        return self.losung

    def getSpalten(self):
        return self.spalten

    def getZeilen(self):
        return self.zeilen