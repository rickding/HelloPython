# -*- coding: utf-8 -*-

from gui.mainWindow import MainWindow
from gui.chooseFaceDetectionModel import chooseFaceDetectionModelDialog
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
