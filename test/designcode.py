# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Mon Jan 12 12:45:31 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
import sys

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 381, 227))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setEnabled(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout.addWidget(self.textBrowser_7, 1, 2, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_4.setEnabled(False)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 0, 3, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 1, 0, 1, 1)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.gridLayout.addWidget(self.textBrowser_10, 2, 0, 1, 1)
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.gridLayout.addWidget(self.textBrowser_12, 2, 3, 1, 1)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_9.setEnabled(False)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.gridLayout.addWidget(self.textBrowser_9, 1, 4, 1, 1)
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.gridLayout.addWidget(self.textBrowser_11, 2, 2, 1, 1)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout.addWidget(self.textBrowser_8, 1, 3, 1, 1)
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_13.setEnabled(False)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.gridLayout.addWidget(self.textBrowser_13, 2, 4, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setEnabled(False)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 0, 1, 1, 1)
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_14.setEnabled(False)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.gridLayout.addWidget(self.textBrowser_14, 0, 2, 1, 1)
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.gridLayout.addWidget(self.textBrowser_15, 1, 1, 1, 1)
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.gridLayout.addWidget(self.textBrowser_16, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 360, 521, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Felder Offen"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">150</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Lösung"))
        self.pushButton.setText(_translate("MainWindow", "Neustart"))


#from qt.mvc import MyView, MyModel


class MyController(QtGui.QWidget):
    """ MVC pattern: Creates a controller - mvc pattern.
    """

    def __init__(self, parent=None):
        """ Create a new controller with a object MyView and a object MyModel
        using the mvc pattern.
        :param parent:
        """
        super().__init__(parent)
        self.myForm = Ui_MainWindow.Ui_Form()
        self.myForm.setupUi(self)
        #self.myModel = Ui_MainWindow.MyModel()
        # connect the buttons with the clicked signal
        self.connectButtons()
        # start a new game
        self.start()

if __name__ == "__main__":
    app = QtCore.QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())