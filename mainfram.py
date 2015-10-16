# -*- coding: utf-8 -*-

"""
Module implementing mainframcontrol.
"""
import sys
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtGui
from Ui_mainfram import Ui_mainfram


class mainframcontrol(QMainWindow, Ui_mainfram):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_search_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    ui = mainframcontrol()

    ui.show()
    sys.exit(app.exec_())
