__author__ = 'Astrid Krickl'
from random import *


class Model():
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
        spielfeld = [[0 for x in range(breite)] for x in range(breite)]
        for x in range(0, breite):
            for y in range(0, breite):
                spielfeld[x][y] = round(random())

        self.losung = spielfeld #losung speichern

        #spielfeld auszählen nur 1er
        #zeilen auslesen & ins attribut speichern
        self.zeilen = [[0 for x in range(breite)] for x in range(breite)]
        for x in range(0, breite):
            zahler = 0
            for y in range(0, breite):
                if spielfeld[x][y] == 1:
                    zahler += 1
                elif spielfeld[x][y] == 0:
                    self.zeilen[x][y] = zahler
                    zahler = 0

        #spalten auslesen & ins attribut speichern
        self.spalten = [[0 for x in range(breite)] for x in range(breite)]
        for x in range(0, breite):
            zahler = 0
            for y in range(0, breite):
                if spielfeld[y][x] == 1:
                    zahler += 1
                elif spielfeld[y][x] == 0:
                    self.spalten[x][y] = zahler
                    zahler = 0

    def getOffen(self, breite):
        spielfeld = self.getLosung()
        zahler = 0
        for x in range(0, breite):
            for y in range(0, breite):
                if spielfeld[y][x] == 1:
                    zahler += 1
        return zahler


    def getLosung(self):
        return self.losung

    def getSpalten(self):
        return self.spalten

    def getZeilen(self):
        return self.zeilen