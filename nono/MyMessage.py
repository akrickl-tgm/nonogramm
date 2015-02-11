__author__ = 'Astrid Krickl'

from PyQt4 import QtGui


class Dialog(QtGui.QWidget):

    def __init__(self):
        """
        Konstruktor der das popup erzeugt
        """
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.edit = QtGui.QTextEdit()
        self.edit.setFontPointSize(20)
        self.edit.insertPlainText('You Won - bad motherlover')
        layout.addWidget(self.edit)
