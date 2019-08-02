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
        self.color = "#ff0000"
        self.finder = None
        self.contours = None
        self.image = QtGui.QImage()

        self.resized.connect(self.resizeElem)

        self.colorBtn.setStyleSheet("background-color:"+self.color)
        self.originFilePath = ""
        self.saveFilePath = ""
        self.value = 0.5
        self.thickness = 0
        self.lineColor = ""

    def resizeElem(self):
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))


    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)



    @QtCore.pyqtSlot()
    def on_openFileBtn_clicked(self):
        print("file open")
        try:
            fname = QtWidgets.QFileDialog.getOpenFileName(self)
            self.originFilePath = fname[0]
            self.img = QtGui.QImage(self.originFilePath)
            pixmap = QtGui.QPixmap(QtGui.QPixmap.fromImage(self.img))
            self.label.setPixmap(pixmap)

            self.label.resize(self.imageWidget.sizeHint())
            self.statusBar.showMessage(self.originFilePath)

            self.finder = ContourFinder(self.originFilePath)

            print("open complete")
        except Exception as e:
            print("open error")
            print(e)

    def getPos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        val = self.label

    @QtCore.pyqtSlot()
    def on_choosePointBtn_clicked(self):
        print("choose")
        try:

            if self.originFilePath is None or self.originFilePath == "":
                msg = QtWidgets.QMessageBox.information(self, "Warning", "Select an image first !!")
            else:

                msg = QtWidgets.QMessageBox.information(self, "Information", "Choose any point you want")



        except Exception as e:
            print("choose error")
            print(e)




    def paintEvent(self, event):
        try:
            qp = QtGui.QPainter()
            qp.begin(self.label)
            self.label.drawLines(qp, self.contours)
            qp.end()
        except Exception as e:
            # print(e)
            pass






    @QtCore.pyqtSlot()
    def on_findContourBtn_clicked(self):
        try:
            self.finder.setColor(self.color)
            self.value = float(self.valueLine.text())
            self.contours = self.finder.find(self.value)
            self.update()
            print("그리기 끝")

        except Exception as e:
            print("find error")
            print(e)

    def drawLines(self,qp, contours):


        pen = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        for n, contour in enumerate(contours):
            for i in range(len(contour[:, 1])-1):
                qp.drawLine(contour[i, 1], contour[i, 0],contour[i+1, 1], contour[i+1, 0])

    @QtCore.pyqtSlot()
    def on_deleteContourBtn_clicked(self):
        print("delete")

    @QtCore.pyqtSlot()
    def on_saveContourBtn_clicked(self):
        try:
            options = QtWidgets.QFileDialog.Options()
            # options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                "Save File",
                                                                "c:\\",
                                                                "Image files (*.jpg *.gif);;Text Files (*.txt)",
                                                                options=options)
            file = open(fileName, 'wb')
            file.close()

        except Exception as e:
            print("save error")
            print(e)


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
    window.show()
    sys.exit(app.exec_())

