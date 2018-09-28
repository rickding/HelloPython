# -*- coding: utf-8 -*-

"""
Module implementing FaceLandmarkDialog.
"""

import os
import sys
import cv2

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from gui.Ui_FaceLandmarkGui import Ui_FaceLandmarkDialog
from app.face_landmark import face_landmark

class FaceLandmarkDialog(QDialog, Ui_FaceLandmarkDialog):
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
        self.algoritm = face_landmark()
    
    @pyqtSignature("")
    def on_radioButton_pressed(self):
        """
        检测5个人脸特征点
        """
        print(u'检测5个人脸特征点')
        self.algoritm.load_method(0)
    
    @pyqtSignature("")
    def on_radioButton_2_pressed(self):
        """
        检测68个人脸特征点
        """
        print(u'检测68个人脸特征点')
        self.algoritm.load_method(1)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        人脸特征点检测
        """
        print(u'人脸特征点检测')
        self.algoritm.load_image(self.imgPath)
        result_img = self.algoritm.run()
        result_img = cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(self.resultPath, result_img)
        
        scene = QtGui.QGraphicsScene(self)                # 创建场景
        pixmap = QtGui.QPixmap(self.resultPath)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
        self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
        self.graphicsView_2.show()                    # 显示
    
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
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = FaceLandmarkDialog()
    ui.show()
    sys.exit(app.exec_())
