# -*- coding: utf-8 -*-

"""
Module implementing chooseFaceDetectionModelDialog.
"""

import sys
sys.path.append("..")
from app.face_detect import face_detect
from FaceDetectGui import FaceDetectDialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_chooseFaceDetectionModel import Ui_chooseFaceDetectionModelDialog

class chooseFaceDetectionModelDialog(QDialog, Ui_chooseFaceDetectionModelDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        
        self.model_type = 0
    
    @pyqtSignature("")
    def on_radioButton_pressed(self):
        """
        默认模型
        """
        print(u'默认模型')
        self.model_type = 0
    
    @pyqtSignature("")
    def on_radioButton_2_pressed(self):
        """
        卷积神经网络（CNN）
        """
        print(u'卷积神经网络（CNN）')
        self.model_type = 1
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        确认
        """
        print(u'确认')
        ui = FaceDetectDialog(self.model_type)
        ui.exec_()
        
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = chooseFaceDetectionModelDialog()
    dialog.show()
    sys.exit(app.exec_())
