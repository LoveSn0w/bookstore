# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dell/github/bookstore/reject.ui'
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

class Ui_refuse(object):
    def setupUi(self, refuse):
        refuse.setObjectName(_fromUtf8("refuse"))
        refuse.resize(400, 300)
        refuse.setSizeGripEnabled(True)
        self.label = QtGui.QLabel(refuse)
        self.label.setGeometry(QtCore.QRect(110, 60, 201, 81))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(refuse)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(refuse)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), refuse.close)
        QtCore.QMetaObject.connectSlotsByName(refuse)

    def retranslateUi(self, refuse):
        refuse.setWindowTitle(_translate("refuse", "Dialog", None))
        self.label.setText(_translate("refuse", "密码错误！！！请重新输入", None))
        self.pushButton.setText(_translate("refuse", "确定", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    refuse = QtGui.QDialog()
    ui = Ui_refuse()
    ui.setupUi(refuse)
    refuse.show()
    sys.exit(app.exec_())

