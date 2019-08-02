from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from Algo import ContourFinder


class DrawableQLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(DrawableQLabel, self).__init__(parent=parent)

    def paintEvent(self, e):
        try:
            super().paintEvent(e)
            qp = QtGui.QPainter(self)
            qp.drawPixmap(100, 100, QtGui.QPixmap())
        except:





    def take_screenshot(self):
        p = QtGui.QPixmap.grabWindow(self.winId())
        p.save("images/capture.jpg", 'jpg')