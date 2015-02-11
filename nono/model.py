__author__ = 'Astrid Krickl'
from random import *


class Model():

    def __init__(self):
        """
        konstruktor zum setup der attribute
        """
        self.losung = None
        self.spalten = []
        self.zeilen = []

    def getpic(self, breite):
        """
        berechnet ein neues spielfeld mit zufallszahlen und zaehlt dieses spielfeld anschließend
        fuer die tipps aus

        :param breite:  breite des spielfelds

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
        # auszählen der felder funktioniert nicht richtig und es gehört noch sortiert und die 0er aussortiert

    def getOffen(self, breite):
        """
        zaehlt die offenen (blauen bzw 1) felder aus

        :param breite:  breite des spielfelds

        :return zaehler:    die anzahl der offenen felder
        """
        spielfeld = self.getLosung()
        zahler = 0
        for x in range(0, breite):
            for y in range(0, breite):
                if spielfeld[y][x] == 1:
                    zahler += 1
        return zahler


    def getLosung(self):
        """
        gibt die losung also das spielfeld zuruck

        :return losung: array des spielfelds
        """
        return self.losung

    def getSpalten(self):
        """
        Gibt die tips der spalten zuruck

        :return spalten:    tipps der spalten
        """
        return self.spalten

    def getZeilen(self):
        """
        gibt die tipps der zeilen zuruck

        :return zeilen: tipps der zeilen
        """
        return self.zeilen