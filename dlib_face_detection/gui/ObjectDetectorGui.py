# -*- coding: utf-8 -*-

"""
Module implementing ObjectDetectorDialog.
"""

import os
import cv2
import numpy as np

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_ObjectDetectorGui import Ui_TrainObjectDetectorDialog
from app.object_detector import object_detector
from gui.TrainObjectDetectorParametersGui import TrainObjectDetectorParametersDialog

class ObjectDetectorDialog(QDialog, Ui_TrainObjectDetectorDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        # 默认导入我制作好的数据集
        pwd = os.getcwd()
        self.images_path = os.path.join(pwd, 'images')
        self.train_images_path = os.path.join(self.images_path, 'test_object_detector', 'cats_train')# 这个文件夹中存放了我制作好的数据集
        self.default_path = os.path.join(self.train_images_path, 'cat.xml')# 保存训练数据集信息的xml文件路径，可以通过dlib自带的工具imglab制作
        self.train_xml_path = self.default_path# 默认的xml文件路径
        self.lineEdit.setText(self.train_xml_path)
        
        # 默认导入我制作好的模型
        if os.path.exists(os.path.join(self.train_images_path, 'detector.svm')):
            self.test_svm_path = os.path.join(self.train_images_path, 'detector.svm')
            self.lineEdit_2.setText(self.test_svm_path)
        self.test_image_path = None
        self.test_result_path = None
        
        self.algorithm = object_detector(self.train_xml_path)# 算法实现类（训练目标检测器）的实例
        
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'数据集路径')
        path = unicode(self.lineEdit.text())
        if os.path.exists(path):# 路径是否存在
#             print(dir)
            if path.strip().split('.')[-1] == 'xml':
                print(path)
                self.train_xml_path = path
    
    @pyqtSignature("QString")
    def on_lineEdit_2_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'模型路径')
#         print(p0)
        text = unicode(p0)
        if os.path.exists(text):
            self.test_svm_path = text
        
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'导入模型文件')
        svm_path = QtGui.QFileDialog.getOpenFileName(self, u'导入模型', '/', u'(*.svm)')
        if os.path.exists(svm_path):
            self.test_svm_path = svm_path
            self.lineEdit_2.setText(self.test_svm_path)
    
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'打开图片')
        self.test_image_path = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.test_image_path = unicode(self.test_image_path)
#         print(self.test_image_path)
        father_path = os.path.abspath(os.path.dirname(self.test_image_path)+os.path.sep+".")
        self.test_result_path = os.path.join(father_path, 'result.jpg')
        if(self.test_image_path != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.test_image_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView.show()                    # 显示
            
#             print(self.test_image_path)
#             print(self.test_result_path)
    
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'检测目标')
        if self.test_svm_path == None:
            print(u'请先导入模型文件！')
        if self.test_image_path == None:
            print(u'请选择待识别的图片！')
        res_img = self.algorithm.predict(model_path=self.test_svm_path, img_path=self.test_image_path)
        cv2.imwrite(self.test_result_path, res_img)
        
        scene = QtGui.QGraphicsScene(self)                # 创建场景
        pixmap = QtGui.QPixmap(self.test_result_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
        self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
        self.graphicsView_2.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'导入训练数据集(XML)')
        xml_path = QtGui.QFileDialog.getOpenFileName(self, u'导入数据集', '/', u'(*.xml)')
        if os.path.exists(xml_path):
            self.train_xml_path = xml_path
            self.lineEdit.setText(xml_path)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'训练模型')
        self.algorithm.set_train_xml_path(self.train_xml_path)
        self.algorithm.set_log(self.textBrowser)
        self.algorithm.print_options()
        # 注：训练时采用默认参数
        self.algorithm.train()
        
    @pyqtSignature("")
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'训练参数设置')
        dialog = TrainObjectDetectorParametersDialog(self.algorithm.options)
        dialog.exec_()
        
