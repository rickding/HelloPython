# -*- coding: utf-8 -*-

"""
Module implementing FaceCompareDialog.
"""

import pickle
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from app.face_compare import face_compare

from Ui_FaceCompareGui import Ui_FaceCompareDialog

class FaceCompareDialog(QDialog, Ui_FaceCompareDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        pwd = os.getcwd()
        self.templates_path = os.path.join(pwd, 'templates')
        self.save_file_path = os.path.join(self.templates_path, 'templates_info.pkl')
        self.img_path = None
        self.face_compare = face_compare()
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        添加人脸模板
        """
        print(u'添加人脸模板')
        img_path = QtGui.QFileDialog.getOpenFileNames(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
#         print(img_path)
        if img_path != '':
#             img_path = str(img_path)
#             self.listWidget.addItem(img_path)

            self.listWidget.addItems(img_path)

            # 打印选择的图片数目
#             print(img_path.count())
#             for i in range(img_path.count()):
#                 q_str = unicode(img_path.takeAt(i))
#                 print(q_str)
#                 self.listWidget.addItem(q_str)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        重新导入模板
        """
        print(u'重新导入模板')
        save_file = open(self.save_file_path, 'rb')
        data = pickle.load(save_file)
        print data
        self.refresh_list(data)
        self.textBrowser.append(u'重新导入模板')
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        删除人脸模板
        """
        print(u'删除人脸模板')
        index = self.listWidget.currentRow()
        print(index)
        # item = self.listWidget.item(index)
        self.listWidget.takeItem(index)
    
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        打开图片
        """
        print(u'打开图片')
        self.img_path = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.img_path = unicode(self.img_path)
        print(self.img_path)
        if(self.img_path != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.img_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        """
        比对人脸
        """
        print(u'比对人脸')
        self.textBrowser.append(u'-'*20)
        self.textBrowser.append(u'比对人脸：')
        res = self.face_compare.compareAgainstTemplate(self.img_path)
        print(res)
        self.textBrowser.append(u'预测结果：')
        for index in range(len(res)):
            self.textBrowser.append(u'%s---%s'%(self.face_compare.template_name[index], res[index]))
        for index in range(len(res)):
            if res[index] == True:
                print(u'The person is %s'%self.face_compare.template_name[index])
                self.textBrowser.append(u'The person is %s'%self.face_compare.template_name[index])
        self.textBrowser.append(u'-'*20) 
        
    @pyqtSignature("")
    def on_pushButton_6_clicked(self):
        """
        保存模板
        """
        print(u'保存模板')
        list_num = self.listWidget.count()
        list_info = []
        for i in range(list_num):
            item_info = self.listWidget.item(i)
            print unicode(item_info.text())
            list_info.append(unicode(item_info.text()))
        
#         print(self.templates_path)
        
        save_file = open(self.save_file_path, 'wb')
        pickle.dump(list_info, save_file)
        
        self.textBrowser.append(u'模板保存成功')
        
    @pyqtSignature("")
    def on_pushButton_7_clicked(self):
        """
        解析模板
        """
        print(u'解析模板')
#         self.textBrowser.append(u'开始解析模板')
        save_file = open(self.save_file_path, 'rb')
        template = pickle.load(save_file)
        print(template)
        self.face_compare.load_template(template)
        self.face_compare.create_template()
        self.textBrowser.append(u'解析模板完成')
        
    def refresh_list(self, list):
        # 清空全部的item
        while(self.listWidget.count()):
            self.listWidget.takeItem(0)
        for i in range(len(list)):
            print(list[i])
            self.listWidget.addItem(list[i])

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = FaceCompareDialog()
    ui.show()
    sys.exit(app.exec_())
    
    
