# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


mainWindowWidth = 1280
mainWindowHeight = 720
toolbarHeight = 21


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1241, 701))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainLayout.setContentsMargins(50, 50, 50, 50)
        self.mainLayout.setObjectName("mainLayout")
        self.imageWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.imageWidget.setObjectName("imageWidget")
        self.imageLayout = QtWidgets.QVBoxLayout(self.imageWidget)
        self.imageLayout.setContentsMargins(20, 20, 20, 20)
        self.imageLayout.setObjectName("imageLayout")
        self.label = QtWidgets.QLabel(self.imageWidget)
        self.label.setObjectName("label")
        self.imageLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.mainLayout.addWidget(self.imageWidget)
        self.controlPanelWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.controlPanelWidget.setObjectName("controlPanelWidget")
        self.controlPanelLayout = QtWidgets.QVBoxLayout(self.controlPanelWidget)
        self.controlPanelLayout.setContentsMargins(20, 20, 20, 20)
        self.controlPanelLayout.setObjectName("controlPanelLayout")
        self.openFileBtn = QtWidgets.QPushButton(self.controlPanelWidget)
        self.openFileBtn.setObjectName("openFileBtn")
        self.controlPanelLayout.addWidget(self.openFileBtn)
        self.choosePointBtn = QtWidgets.QPushButton(self.controlPanelWidget)
        self.choosePointBtn.setObjectName("choosePointBtn")
        self.controlPanelLayout.addWidget(self.choosePointBtn)
        self.findContourBtn = QtWidgets.QPushButton(self.controlPanelWidget)
        self.findContourBtn.setObjectName("findContourBtn")
        self.controlPanelLayout.addWidget(self.findContourBtn)
        self.contourOptionWidget = QtWidgets.QWidget(self.controlPanelWidget)
        self.contourOptionWidget.setObjectName("contourOptionWidget")
        self.contourOptionLayout = QtWidgets.QFormLayout(self.contourOptionWidget)
        self.contourOptionLayout.setContentsMargins(5, 5, 5, 5)
        self.contourOptionLayout.setObjectName("contourOptionLayout")
        self.thicknessLabel = QtWidgets.QLabel(self.contourOptionWidget)
        self.thicknessLabel.setObjectName("thicknessLabel")
        self.contourOptionLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.thicknessLabel)
        self.thicknessComboBox = QtWidgets.QComboBox(self.contourOptionWidget)
        self.thicknessComboBox.setObjectName("thicknessComboBox")
        self.thicknessComboBox.addItem("")
        self.thicknessComboBox.addItem("")
        self.thicknessComboBox.addItem("")
        self.contourOptionLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thicknessComboBox)
        self.colorLabel = QtWidgets.QLabel(self.contourOptionWidget)
        self.colorLabel.setObjectName("colorLabel")
        self.contourOptionLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.colorLabel)
        self.colorBtn = QtWidgets.QPushButton(self.contourOptionWidget)
        self.colorBtn.setObjectName("colorBtn")
        self.contourOptionLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.colorBtn)
        self.controlPanelLayout.addWidget(self.contourOptionWidget)
        self.deleteContourBtn = QtWidgets.QPushButton(self.controlPanelWidget)
        self.deleteContourBtn.setObjectName("deleteContourBtn")
        self.controlPanelLayout.addWidget(self.deleteContourBtn)
        self.saveContourBtn = QtWidgets.QPushButton(self.controlPanelWidget)
        self.saveContourBtn.setObjectName("saveContourBtn")
        self.controlPanelLayout.addWidget(self.saveContourBtn)
        self.mainLayout.addWidget(self.controlPanelWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.connect_all()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image will shown here"))
        self.openFileBtn.setText(_translate("MainWindow", "Open New Image"))
        self.choosePointBtn.setText(_translate("MainWindow", "Choose a Point"))
        self.findContourBtn.setText(_translate("MainWindow", "Find Contour"))
        self.thicknessLabel.setText(_translate("MainWindow", "Thickness:"))
        self.thicknessComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.thicknessComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.thicknessComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.colorLabel.setText(_translate("MainWindow", "Color:"))
        self.colorBtn.setText(_translate("MainWindow", "Color"))
        self.deleteContourBtn.setText(_translate("MainWindow", "Delete Contour"))
        self.saveContourBtn.setText(_translate("MainWindow", "Save Contour"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "New"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))



    def connect_all(self):
        self.openFileBtn.clicked.connect(self.on_openFileBtn_clicked)
        self.choosePointBtn.clicked.connect(self.on_choosePointBtn_clicked)
        self.findContourBtn.clicked.connect(self.on_findContourBtn_clicked)
        self.deleteContourBtn.clicked.connect(self.on_deleteContourBtn_clicked)
        self.saveContourBtn.clicked.connect(self.on_saveContourBtn_clicked)




    @QtCore.pyqtSlot()
    def on_openFileBtn_clicked(self):
        print("file open")
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget)
        self.filepath = fname[0]
        pixmap = QtGui.QPixmap(fname[0])
        self.label.resize(self.imageLayout.sizeHint())
        self.label.setPixmap(pixmap)
        self.statusBar.showMessage(self.filepath)



    @QtCore.pyqtSlot()
    def on_choosePointBtn_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_findContourBtn_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_deleteContourBtn_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_saveContourBtn_clicked(self):
        pass






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

