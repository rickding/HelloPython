# -*- coding: utf-8 -*-

"""
Module implementing FaceDetectDialog.
"""

import sys
sys.path.append("..")
from app.face_detect import face_detect

import cv2
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_FaceDetectGui import Ui_FaceDetectDialog

class FaceDetectDialog(QDialog, Ui_FaceDetectDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, method = 0, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.method = method# 人脸检测采用的方法：0--默认模型，1--CNN
        if method == 0:
            self.label_4.setText(u'默认模型')
        elif method == 1:
            self.label_4.setText(u'CNN')
        else:
            pass
        # print(self.method)
        self.imgPath = None
        self.resultPath = None
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        打开图片
        """
        self.imgPath = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.imgPath = unicode(self.imgPath)
        print(self.imgPath)
#         print(os.path.dirname(self.imgPath))
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
        人脸检测
        """
        fc = face_detect(img_path=self.imgPath, method=self.method)
        
#         waitWindow = QtGui.QWidget()
#         waitWindow.setGeometry(100,100,300,200) 
#         waitWindow.setWindowTitle(u'提示')
#         label = QtGui.QLabel(waitWindow)
#         label.setText(u'程序正在运行中')
#         label.move(100, 100)
#         waitWindow.show()
        
        res_img = fc.run()
        
#         waitWindow.close()
        
        res_img = cv2.cvtColor(res_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(self.resultPath, res_img)
        
        scene = QtGui.QGraphicsScene(self)                # 创建场景
        pixmap = QtGui.QPixmap(self.resultPath)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
        self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
        self.graphicsView_2.show()                    # 显示
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = FaceDetectDialog()
    ui.exec_()
    sys.exit(app.exec_())
