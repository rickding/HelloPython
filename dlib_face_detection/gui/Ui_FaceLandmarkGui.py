# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\PyQt\Project\my_dlib_face_detection_application\FaceLandmark.ui'
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

class Ui_FaceLandmarkDialog(object):
    def setupUi(self, FaceLandmarkDialog):
        FaceLandmarkDialog.setObjectName(_fromUtf8("FaceLandmarkDialog"))
        FaceLandmarkDialog.resize(699, 633)
        self.verticalLayout_8 = QtGui.QVBoxLayout(FaceLandmarkDialog)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(FaceLandmarkDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.graphicsView = QtGui.QGraphicsView(FaceLandmarkDialog)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_5.addWidget(self.graphicsView)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(FaceLandmarkDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.graphicsView_2 = QtGui.QGraphicsView(FaceLandmarkDialog)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.verticalLayout_6.addWidget(self.graphicsView_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.groupBox = QtGui.QGroupBox(FaceLandmarkDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.groupBox)
        self.pushButton = QtGui.QPushButton(FaceLandmarkDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(FaceLandmarkDialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(FaceLandmarkDialog)
        QtCore.QMetaObject.connectSlotsByName(FaceLandmarkDialog)

    def retranslateUi(self, FaceLandmarkDialog):
        FaceLandmarkDialog.setWindowTitle(_translate("FaceLandmarkDialog", "人脸特征点检测", None))
        self.label.setText(_translate("FaceLandmarkDialog", "原图", None))
        self.label_2.setText(_translate("FaceLandmarkDialog", "结果", None))
        self.groupBox.setTitle(_translate("FaceLandmarkDialog", "选择模式：", None))
        self.radioButton.setText(_translate("FaceLandmarkDialog", "检测5个人脸特征点", None))
        self.radioButton_2.setText(_translate("FaceLandmarkDialog", "检测68个人脸特征点", None))
        self.pushButton_2.setText(_translate("FaceLandmarkDialog", "检测人脸特征点", None))
        self.pushButton.setText(_translate("FaceLandmarkDialog", "打开图片", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FaceLandmarkDialog = QtGui.QDialog()
    ui = Ui_FaceLandmarkDialog()
    ui.setupUi(FaceLandmarkDialog)
    FaceLandmarkDialog.show()
    sys.exit(app.exec_())

