# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pointAnnotator.ui'
#
# Created: Wed Jul 01 15:51:35 2015
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(20, 110, 771, 571))
        self.img.setText("")
        self.img.setObjectName("img")
        self.dirView = QtWidgets.QLabel(self.centralwidget)
        self.dirView.setGeometry(QtCore.QRect(150, 30, 1041, 33))
        self.dirView.setObjectName("dirView")
        self.dirSearch = QtWidgets.QPushButton(self.centralwidget)
        self.dirSearch.setGeometry(QtCore.QRect(20, 20, 101, 57))
        self.dirSearch.setObjectName("dirSearch")
        self.currentImg = QtWidgets.QLabel(self.centralwidget)
        self.currentImg.setGeometry(QtCore.QRect(700, 520, 351, 33))
        self.currentImg.setText("")
        self.currentImg.setObjectName("currentImg")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(830, 90, 350, 277))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.numPtsText = QtWidgets.QLabel(self.formLayoutWidget)
        self.numPtsText.setObjectName("numPtsText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numPtsText)
        self.ptsLeftText = QtWidgets.QLabel(self.formLayoutWidget)
        self.ptsLeftText.setObjectName("ptsLeftText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ptsLeftText)
        self.numPts = QtWidgets.QLabel(self.formLayoutWidget)
        self.numPts.setObjectName("numPts")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numPts)
        self.ptsLeft = QtWidgets.QLabel(self.formLayoutWidget)
        self.ptsLeft.setObjectName("ptsLeft")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ptsLeft)
        self.subText = QtWidgets.QLabel(self.formLayoutWidget)
        self.subText.setObjectName("subText")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.subText)
        self.stuText = QtWidgets.QLabel(self.formLayoutWidget)
        self.stuText.setObjectName("stuText")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stuText)
        self.imgText = QtWidgets.QLabel(self.formLayoutWidget)
        self.imgText.setObjectName("imgText")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.imgText)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.nxtImg = QtWidgets.QPushButton(self.centralwidget)
        self.nxtImg.setGeometry(QtCore.QRect(990, 370, 187, 57))
        self.nxtImg.setObjectName("nxtImg")
        self.skip = QtWidgets.QPushButton(self.centralwidget)
        self.skip.setGeometry(QtCore.QRect(990, 430, 187, 57))
        self.skip.setObjectName("skip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 47))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dirView.setText(_translate("MainWindow", "path"))
        self.dirSearch.setText(_translate("MainWindow", "Browse"))
        self.numPtsText.setText(_translate("MainWindow", "Num points:"))
        self.ptsLeftText.setText(_translate("MainWindow", "Points left:"))
        self.numPts.setText(_translate("MainWindow", "np"))
        self.ptsLeft.setText(_translate("MainWindow", "pl"))
        self.subText.setText(_translate("MainWindow", "subject"))
        self.stuText.setText(_translate("MainWindow", "study"))
        self.imgText.setText(_translate("MainWindow", "image"))
        self.label.setText(_translate("MainWindow", "Subject:"))
        self.label_2.setText(_translate("MainWindow", "Study: "))
        self.label_3.setText(_translate("MainWindow", "Image:"))
        self.nxtImg.setText(_translate("MainWindow", "Next Image"))
        self.skip.setText(_translate("MainWindow", "Skip"))
