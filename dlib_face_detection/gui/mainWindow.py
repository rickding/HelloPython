# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from chooseFaceDetectionModel import chooseFaceDetectionModelDialog
from gui.FaceLandmarkGui import FaceLandmarkDialog
from gui.FaceCompareGui import FaceCompareDialog
from gui.FaceAlignGui import FaceAlignDialog
from gui.CorrelationTrackerGui import CorrelationTrackerDialog
from gui.FaceExchangeGui import FaceExchangeDialog
from gui.FaceClusteringGui import FaceClusteringDialog
from gui.ObjectDetectorGui import ObjectDetectorDialog
from gui.ShapeDetectorGui import ShapePredictorDialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
import webbrowser

from Ui_mainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        人脸检测
        """
        print(u'人脸检测')
        # add your code here
        dialog = chooseFaceDetectionModelDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        人脸关键点检测
        """
        print(u'人脸关键点检测')
        # add your code here
        dialog = FaceLandmarkDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        人脸比对
        """
        print(u'人脸比对')
        # add your code here
        dialog = FaceCompareDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        人脸特征点对齐
        """
        print(u'人脸特征点对齐')
        dialog = FaceAlignDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        """
        人脸聚类
        """
        print(u'人脸聚类')
        dialog = FaceClusteringDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_6_clicked(self):
        """
        换脸
        """
        print(u'换脸')
        
        dialog = FaceExchangeDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_8_clicked(self):
        """
        训练目标检测器
        """
        print(u'训练目标检测器')
        dialog = ObjectDetectorDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_9_clicked(self):
        """
        训练人脸特征点检测器
        """
        print(u'训练人脸特征点检测器')
        dialog = ShapePredictorDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_pushButton_10_clicked(self):
        """
        目标跟踪
        """
        print(u'目标跟踪')
        dialog = CorrelationTrackerDialog()
        dialog.exec_()
    
    @pyqtSignature("")
    def on_action_triggered(self):
        """
        关于作者
        """
        print(u'关于作者')
        author_information = u'作者：许鸿斌' + '\n'
        author_information += u'邮箱：2775751197@qq.com' + '\n'
        author_information += u'个人博客：http://blog.csdn.net/hongbin_xu' + '\n'
        button = QtGui.QMessageBox.question(self,  u'作者信息',  author_information,  u'打开博客',  u'退出')
        print(button)  # 0--打开博客 1--退出
        if button == 0:
            webbrowser.open('http://blog.csdn.net/hongbin_xu')
        else:
            pass
    
    @pyqtSignature("")
    def on_action_2_triggered(self):
        """
        操作说明
        """
        print(u'操作说明')
        ret = QtGui.QMessageBox.information(self,  u'操作说明',  u'暂无操作说明，待补充',  1)
        # print(ret)
    
    @pyqtSignature("")
    def on_action_PYQT_triggered(self):
        """
        关于PYQT
        """
        print(u'关于PYQT')
        QtGui.QMessageBox.aboutQt(self,  u'关于PYQT')
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
