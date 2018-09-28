# -*- coding: utf-8 -*-

"""
Module implementing ShapePredictorDialog.
"""
import os
import cv2

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_ShapeDetectorGui import Ui_ShapePredictorDialog
from app.shape_predictor import shape_predictor
from gui.TrainShapePredictorParametersGui import TrainShapePredictorParametersDialog

class ShapePredictorDialog(QDialog, Ui_ShapePredictorDialog):
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
        self.train_images_path = os.path.join(self.images_path, 'test_shape_predictor', 'faces')# 这个文件夹中存放了我制作好的数据集
        self.default_path = os.path.join(self.train_images_path, 'training_with_face_landmarks.xml')# 保存训练数据集信息的xml文件路径，可以通过dlib自带的工具imglab制作
        self.train_xml_path = self.default_path# 默认的xml文件路径
        self.lineEdit.setText(self.train_xml_path)
        
        # 默认导入我制作好的模型
        if os.path.exists(os.path.join(self.train_images_path, 'predictor.dat')):
            self.test_dat_path = os.path.join(self.train_images_path, 'predictor.dat')
            self.lineEdit_2.setText(self.test_dat_path)
        self.test_image_path = None
        self.test_result_path = None
        
        self.algorithm = shape_predictor(self.train_xml_path)# 算法实现类（训练目标检测器）的实例
    
    @pyqtSignature("QString")
    def on_lineEdit_2_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        print(u'模型路径')
        text = unicode(p0)
        if os.path.exists(text):
            self.test_dat_path = text
            print(text)
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'导入模型文件')
        dat_path = QtGui.QFileDialog.getOpenFileName(self, u'导入模型', '/', u'(*.dat)')
        if os.path.exists(dat_path):
            self.test_dat_path = dat_path
            self.lineEdit_2.setText(self.test_dat_path)
    
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
    
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'检测目标')
        
        if self.test_dat_path == None:
            print(u'请先导入模型文件！')
        if self.test_image_path == None:
            print(u'请选择待识别的图片！')
            
        res_img = self.algorithm.predict(model_path=str(self.test_dat_path), img_path=str(self.test_image_path))
        cv2.imwrite(self.test_result_path, res_img)
        
        scene = QtGui.QGraphicsScene(self)                # 创建场景
        pixmap = QtGui.QPixmap(self.test_result_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
        self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
        self.graphicsView_2.show()                    # 显示
    
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
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'训练参数设置')
        dialog = TrainShapePredictorParametersDialog(self.algorithm.options)
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print(u'训练模型')
        self.algorithm.set_log(self.textBrowser)
        self.algorithm.set_train_xml_path(self.train_xml_path)
        self.algorithm.print_options()
        self.algorithm.train()
        
