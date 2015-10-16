# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\shihui\ericproject\bookstore\mainfram.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainfram(object):
    def setupUi(self, mainfram):
        mainfram.setObjectName(_fromUtf8("mainfram"))
        mainfram.resize(800, 600)
        self.centralWidget = QtGui.QWidget(mainfram)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.search = QtGui.QPushButton(self.centralWidget)
        self.search.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.search.setObjectName(_fromUtf8("search"))
        mainfram.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainfram)
        QtCore.QMetaObject.connectSlotsByName(mainfram)

    def retranslateUi(self, mainfram):
        mainfram.setWindowTitle(_translate("mainfram", "MainWindow", None))
        self.search.setText(_translate("mainfram", "查询", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainfram = QtGui.QMainWindow()
    ui = Ui_mainfram()
    ui.setupUi(mainfram)
    mainfram.show()
    sys.exit(app.exec_())

