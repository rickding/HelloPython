# -*- coding: utf-8 -*-

"""
Module implementing FaceExchangeDialog.
"""

import os
import cv2

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_FaceExchangeGui import Ui_FaceExchangeDialog
from app.face_exchange import FaceChanger

class FaceExchangeDialog(QDialog, Ui_FaceExchangeDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.img_1_path = None
        self.img_2_path = None
        self.result_path = None
        
        self.algorithm = FaceChanger()
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'选择图片1')
        
        self.img_1_path = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.img_1_path = unicode(self.img_1_path)
        print(self.img_1_path)
        father_path = os.path.abspath(os.path.dirname(self.img_1_path)+os.path.sep+".")
        self.result_path = os.path.join(father_path, 'result.jpg')
        if(self.img_1_path != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.img_1_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'选择图片2')
        
        self.img_2_path = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.img_2_path = unicode(self.img_2_path)
        print(self.img_2_path)
#         father_path = os.path.abspath(os.path.dirname(self.img_2_path)+os.path.sep+".")
#         self.resultPath = os.path.join(father_path, 'result.jpg')
        if(self.img_2_path != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.img_2_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView_2.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'换脸')
        self.algorithm.load_images(self.img_1_path, self.img_2_path)
        res = self.algorithm.run(showProcedure=False, saveResult=False)# 处理过程中的图片不显示，这里面保存的图片默认会在当前路径下保存，不使用类自带的保存方法
        cv2.imwrite(self.result_path, res)
        
        if(self.result_path != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.result_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView_3.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView_3.show()                    # 显示
