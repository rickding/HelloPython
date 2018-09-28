# -*- coding: utf-8 -*-

"""
Module implementing TrainObjectDetectorParametersDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_TrainObjectDetectorParametersGui import Ui_TrainObjectDetectorParametersDialog

class TrainObjectDetectorParametersDialog(QDialog, Ui_TrainObjectDetectorParametersDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, options, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        # 从原来的窗口中导入SVM参数设置的实例对象，这里都是直接操作self.options来更改值
        self.options = options
#         self.sliding_window_width = 80
#         self.sliding_window_height = 80
#         self.sliding_window_size = self.sliding_window_width * self.sliding_window_height
        
        self.doubleSpinBox.setValue(self.options.C)
        self.doubleSpinBox_2.setValue(self.options.epsilon)
        self.spinBox.setValue(self.options.num_threads)
        self.spinBox_2.setValue(self.options.detection_window_size)
        if self.options.add_left_right_image_flips == True:
            self.radioButton.setDown(True)
        else:
            self.radioButton_2.setDown(True)
        if self.options.be_verbose == True:
            self.radioButton_3.setDown(True)
        else:
            self.radioButton_4.setDown(True)
    
    @pyqtSignature("double")
    def on_doubleSpinBox_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'c: {0}'.format(p0))
        self.options.C = p0
    
    @pyqtSignature("double")
    def on_doubleSpinBox_2_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'epsilon: {0}'.format(p0))
        self.options.epsilon = p0
    
    @pyqtSignature("int")
    def on_spinBox_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'threads: {0}'.format(p0))
        self.options.num_threads = p0
    
    @pyqtSignature("int")
    def on_spinBox_2_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'sliding window width: {0}'.format(p0))
        self.options.detection_window_size = p0
    
    @pyqtSignature("")
    def on_radioButton_pressed(self):
        """
        Slot documentation goes here.
        """
        print(u'add_left_right_image_flips: True')
        self.options.add_left_right_image_flips = True
    
    @pyqtSignature("")
    def on_radioButton_2_pressed(self):
        """
        Slot documentation goes here.
        """
        print(u'add_left_right_image_flips: False')
        self.options.add_left_right_image_flips = False
    
    @pyqtSignature("")
    def on_radioButton_3_pressed(self):
        """
        Slot documentation goes here.
        """
        print(u'be_verbose: True')
        self.options.be_verbose = True
    
    @pyqtSignature("")
    def on_radioButton_4_pressed(self):
        """
        Slot documentation goes here.
        """
        print(u'be_verbose: False')
        self.options.be_verbose = False
