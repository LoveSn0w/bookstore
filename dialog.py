# -*- coding: utf-8 -*-

"""
Module implementing DialogControl.
"""
import sys
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4 import QtGui
from Ui_dialog import Ui_Dialog
from mainfram import mainframcontrol
from Ui_reject import Ui_refuse
class DialogControl(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_login_clicked(self):
        print '这是登陆'
        
        if (self.username.text()=='123' and self.password.text()=='123'):
        

            mainframui.show()
            ui.close()

        else:
            print '登录失败'


            refuse.setupUi(refuse1)
            refuse1.show()
            self.username.setText("")
            self.password.setText("")

        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet

        
    
    @pyqtSignature("")
    def on_reset_clicked(self):
        """
        Slot documentation goes here.
        """
        print '''这是重置'''
    
        self.username.setText("")
        self.password.setText("")
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    ui = DialogControl()
    ui.show()
    mainframui=mainframcontrol()
    refuse=Ui_refuse()
    refuse1 = QtGui.QDialog()
    sys.exit(app.exec_())
