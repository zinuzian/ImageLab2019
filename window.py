# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from Algo import ContourFinder

form_class = uic.loadUiType("ui/basic.ui")[0]


mainWindowWidth = 1280
mainWindowHeight = 720
toolbarHeight = 21



class MainWindow(QtWidgets.QMainWindow, form_class):
    resized = QtCore.pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color = "red"
        self.finder = None

        self.resized.connect(self.resizeElem)
        self.colorBtn.setStyleSheet("background-color:"+self.color)
        self.filepath = ""
        self.value = -1
        self.thickness = 0
        self.lineColor = ""

    def resizeElem(self):
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))



    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)

    def connect_all(self):
        # self.openFileBtn.clicked.connect(self.on_openFileBtn_clicked)
        # self.choosePointBtn.clicked.connect(self.on_choosePointBtn_clicked)
        # self.findContourBtn.clicked.connect(self.on_findContourBtn_clicked)
        # self.deleteContourBtn.clicked.connect(self.on_deleteContourBtn_clicked)
        # self.saveContourBtn.clicked.connect(self.on_saveContourBtn_clicked)
        pass



    @QtCore.pyqtSlot()
    def on_openFileBtn_clicked(self):
        try:
            print("file open")
            fname = QtWidgets.QFileDialog.getOpenFileName(self)
            self.filepath = fname[0]
            pixmap = QtGui.QPixmap(fname[0])
            self.label.setPixmap(pixmap)

            self.label.resize(self.imageWidget.sizeHint())
            self.statusBar.showMessage(self.filepath)

            self.finder = ContourFinder(self.filepath)
        except:
            print("open error")


    @QtCore.pyqtSlot()
    def on_choosePointBtn_clicked(self):
        print("choose")
        if self.filepath == "":
            msg = QtWidgets.QMessageBox.information(self, "Warning", "Select an image first !!")
        else:

            msg = QtWidgets.QMessageBox.information(self, "Information", "Choose any point you want")


    def paintEvent(self, event):
        try:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawLines(qp, self.contours)
            qp.end()
        except Exception as e:
            # print(e)
            pass

    def drawLines(self,qp, contours):

        # color = QtGui.QColor(0, 0, 0)
        # color.setNamedColor(self.color)

        pen = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        for n, contour in enumerate(contours):
            for i in range(len(contour[:, 1])-1):
                qp.drawLine(contour[i, 1], contour[i, 0],contour[i+1, 1], contour[i+1, 0])




    @QtCore.pyqtSlot()
    def on_findContourBtn_clicked(self):
        try:
            self.finder.setColor(self.color)
            self.contours = self.finder.find(0.8)
            self.update()



            # for n, contour in enumerate(contours):
            #     for i in range(len(contour[:, 1])-1):
            #
            #         qp.drawLine(contour[i, 1], contour[i, 0],contour[i+1, 1], contour[i+1, 0])
            print("그리기 끝")

        except Exception as e:
            print(e)



    @QtCore.pyqtSlot()
    def on_deleteContourBtn_clicked(self):
        print("delete")

    @QtCore.pyqtSlot()
    def on_saveContourBtn_clicked(self):
        print("save")

    @QtCore.pyqtSlot()
    def on_colorBtn_clicked(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            self.color = color.name()
            self.colorBtn.setStyleSheet("background-color:" + self.color)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.connect_all()
    window.show()
    sys.exit(app.exec_())

