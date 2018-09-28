# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\PyQt\Project\my_dlib_face_detection_application\FaceClusteringGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FaceClusteringDialog(object):
    def setupUi(self, FaceClusteringDialog):
        FaceClusteringDialog.setObjectName(_fromUtf8("FaceClusteringDialog"))
        FaceClusteringDialog.resize(1085, 661)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FaceClusteringDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(FaceClusteringDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(FaceClusteringDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(FaceClusteringDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(FaceClusteringDialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtGui.QTextBrowser(FaceClusteringDialog)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(FaceClusteringDialog)
        QtCore.QMetaObject.connectSlotsByName(FaceClusteringDialog)

    def retranslateUi(self, FaceClusteringDialog):
        FaceClusteringDialog.setWindowTitle(_translate("FaceClusteringDialog", "人脸聚类", None))
        self.label.setText(_translate("FaceClusteringDialog", "说明： \n"
"自行指定文件夹保存一些测试图片或是使用预载入的测试文件夹；\n"
"model文件夹保存模型文件，也可以自己训练；\n"
"output文件夹中会保存输出结果；", None))
        self.pushButton.setText(_translate("FaceClusteringDialog", "选择文件夹", None))
        self.pushButton_2.setText(_translate("FaceClusteringDialog", "人脸聚类", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FaceClusteringDialog = QtGui.QDialog()
    ui = Ui_FaceClusteringDialog()
    ui.setupUi(FaceClusteringDialog)
    FaceClusteringDialog.show()
    sys.exit(app.exec_())

