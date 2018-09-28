# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

import os
import cv2

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_FaceAlignGui import Ui_Dialog
from app.face_align import face_align

class FaceAlignDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.imgPath = None
        self.resultPath = None
        
        self.algorithm = face_align()
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        打开图片
        """
        print(u'打开图片')
        self.imgPath = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.imgPath = unicode(self.imgPath)
        print(self.imgPath)
        father_path = os.path.abspath(os.path.dirname(self.imgPath)+os.path.sep+".")
        self.resultPath = os.path.join(father_path, 'result.jpg')
        if(self.imgPath != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.imgPath)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        人脸特征点对齐
        """
        print(u'人脸特征点对齐')
        self.algorithm.load_image(self.imgPath)
        res_img = self.algorithm.run()
        cv2.imwrite(self.resultPath, res_img)
         
        scene = QtGui.QGraphicsScene(self)                # 创建场景
        pixmap = QtGui.QPixmap(self.resultPath)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
        self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
        self.graphicsView_2.show()                    # 显示
