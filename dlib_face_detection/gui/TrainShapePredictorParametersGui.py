# -*- coding: utf-8 -*-

"""
Module implementing TrainShapePredictorParametersDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_TrainShapePredictorParametersGui import Ui_TrainShapePredictorParametersDialog

class TrainShapePredictorParametersDialog(QDialog, Ui_TrainShapePredictorParametersDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, options, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.options = options
        
        if self.options.be_verbose == True:
            self.radioButton.setDown(True)
        else:
            self.radioButton_2.setDown(True)
        self.spinBox.setValue(self.options.cascade_depth)
        self.doubleSpinBox.setValue(self.options.feature_pool_region_padding)
        self.spinBox_2.setValue(self.options.feature_pool_size)
        self.doubleSpinBox_2.setValue(self.options.lambda_param)
        self.doubleSpinBox_3.setValue(self.options.nu)
        self.spinBox_3.setValue(self.options.num_test_splits)
        self.spinBox_4.setValue(self.options.num_trees_per_cascade_level)
        self.spinBox_5.setValue(self.options.oversampling_amount)
        self.spinBox_6.setValue(self.options.tree_depth)
    
    @pyqtSignature("")
    def on_radioButton_pressed(self):
        """
        Slot documentation goes here.
        """
        print(u'be_verbose: True')
        self.options.be_verbose = True
    
    @pyqtSignature("")
    def on_radioButton_2_pressed(self):
        """
        Slot documentation goes here.
        """
        print(u'be_verbose: False')
        self.options.be_verbose = False
    
    @pyqtSignature("int")
    def on_spinBox_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'cascade_depth:{}'.format(p0))
        self.options.cascade_depth = p0
    
    @pyqtSignature("double")
    def on_doubleSpinBox_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'feature_pool_region_padding:{}'.format(p0))
        self.options.feature_pool_region_padding = p0
    
    @pyqtSignature("int")
    def on_spinBox_2_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'feature_pool_size:{}'.format(p0))
        self.options.feature_pool_size = p0
    
    @pyqtSignature("double")
    def on_doubleSpinBox_2_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'lambda_param:{}'.format(p0))
        self.options.lambda_param = p0
    
    @pyqtSignature("double")
    def on_doubleSpinBox_3_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'nu:{}'.format(p0))
        self.options.nu = p0
    
    @pyqtSignature("int")
    def on_spinBox_3_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'num_test_splits:{}'.format(p0))
        self.options.num_test_splits = p0
    
    @pyqtSignature("int")
    def on_spinBox_4_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'num_trees_per_cascade_level:{}'.format(p0))
        self.options.num_trees_per_cascade_level = p0
    
    @pyqtSignature("int")
    def on_spinBox_5_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'oversampling_amount:{}'.format(p0))
        self.options.oversampling_amount = p0
    
    @pyqtSignature("int")
    def on_spinBox_6_valueChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'tree_depth:{}'.format(p0))
        self.options.tree_depth = p0
