__author__ = 'Asi'
from nono.control import *
from PyQt4 import QtCore, QtGui
import sys

#START:
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())