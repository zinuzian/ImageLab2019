from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from Algo import ContourFinder


class DrawableQLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(DrawableQLabel, self).__init__(parent=parent)
        self.contours = None

    def paintEvent(self, e):
        try:
            super().paintEvent(e)
            if self.contours is not None:
                self.drawLines()

        except Exception as e:
            print(e)

    def drawLines(self):
        qp = QtGui.QPainter(self)
        qp.begin(self)
        pen = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        for n, contour in enumerate(self.contours):
            for i in range(len(contour[:, 1]) - 1):
                qp.drawLine(contour[i, 1], contour[i, 0], contour[i + 1, 1], contour[i + 1, 0])
        # qp.drawPixmap(100,50, QtGui.QPixmap("images/web.png"))
        qp.end()



    def setContours(self, contours):
        self.contours = contours

    def setPenColor(self, color):
        self.penColor = color

    def take_screenshot(self):
        p = QtGui.QPixmap.grabWindow(self.winId())
        p.save("images/capture.jpg", 'jpg')