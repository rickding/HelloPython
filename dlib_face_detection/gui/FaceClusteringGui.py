# -*- coding: utf-8 -*-

"""
Module implementing FaceClusteringDialog.
"""

import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_FaceClusteringGui import Ui_FaceClusteringDialog
from app.face_clustering import face_clustering

class FaceClusteringDialog(QDialog, Ui_FaceClusteringDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        pwd = os.getcwd()# 获取当前路径
        image_path = os.path.join(pwd, 'images')
        default_test_path = os.path.join(image_path, 'test_face_clustering')
        
        self.clustering_path = default_test_path    # 待聚类的文件夹路径，存放有若干张图片，每张图片中有若干张人脸
        self.lineEdit.setText(default_test_path)
        
        self.algorithm = face_clustering()# 算法类（人脸聚类）的实例
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'选择文件夹')
        dir = QtGui.QFileDialog.getExistingDirectory(self, u'选择文件夹')
        dir = unicode(dir)
#         print(dir)
        if(os.path.exists(dir)):
#             self.clustering_path = dir
            self.lineEdit.setText(dir)# 如果路径改变，自动触发on_lineEdit_textChanged槽函数；若不变，不触发，不改变
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'人脸聚类')
        self.algorithm.set_input_dir(self.clustering_path)
        self.algorithm.set_log(self.textBrowser)
        self.algorithm.run()
    
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'TextChanged')
        text = self.lineEdit.text()
#         print(os.path.exists(text))
        if(os.path.exists(text)):# 验证路径存在
            self.clustering_path = unicode(text)
            self.textBrowser.append(u'文件夹路径：{0}'.format(text))
