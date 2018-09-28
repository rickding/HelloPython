# -*- coding: utf-8 -*-

"""
Module implementing CorrelationTrackerDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_CorrelationTrackerGui import Ui_Dialog
from app.correlation_tracker import correlation_tracker

class CorrelationTrackerDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.algorithm = None
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'实时跟踪')
        self.algorithm = correlation_tracker(windowName='image', cameraNum=0)
        self.algorithm.run()
