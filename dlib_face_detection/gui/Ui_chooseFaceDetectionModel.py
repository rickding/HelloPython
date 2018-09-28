# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\PyQt\Project\my_dlib_face_detection_application\chooseFaceDetectionModel.ui'
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

class Ui_chooseFaceDetectionModelDialog(object):
    def setupUi(self, chooseFaceDetectionModelDialog):
        chooseFaceDetectionModelDialog.setObjectName(_fromUtf8("chooseFaceDetectionModelDialog"))
        chooseFaceDetectionModelDialog.resize(301, 118)
        self.verticalLayout_2 = QtGui.QVBoxLayout(chooseFaceDetectionModelDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(chooseFaceDetectionModelDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(chooseFaceDetectionModelDialog)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.line = QtGui.QFrame(chooseFaceDetectionModelDialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.radioButton_2 = QtGui.QRadioButton(chooseFaceDetectionModelDialog)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(chooseFaceDetectionModelDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(chooseFaceDetectionModelDialog)
        QtCore.QMetaObject.connectSlotsByName(chooseFaceDetectionModelDialog)

    def retranslateUi(self, chooseFaceDetectionModelDialog):
        chooseFaceDetectionModelDialog.setWindowTitle(_translate("chooseFaceDetectionModelDialog", "选择人脸识别模型", None))
        self.label.setText(_translate("chooseFaceDetectionModelDialog", "在下面两个中选择一个人脸识别模型：", None))
        self.radioButton.setText(_translate("chooseFaceDetectionModelDialog", "默认模型", None))
        self.radioButton_2.setText(_translate("chooseFaceDetectionModelDialog", "卷积神经网络（CNN）", None))
        self.pushButton.setText(_translate("chooseFaceDetectionModelDialog", "确认", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    chooseFaceDetectionModelDialog = QtGui.QDialog()
    ui = Ui_chooseFaceDetectionModelDialog()
    ui.setupUi(chooseFaceDetectionModelDialog)
    chooseFaceDetectionModelDialog.show()
    sys.exit(app.exec_())

