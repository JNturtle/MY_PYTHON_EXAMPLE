# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JN\source\repos\部落格範例\部落格範例\matplotlib繪圖互動\mlt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 520)
        MainWindow.setMinimumSize(QtCore.QSize(750, 520))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.f1 = MW_SIN(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f1.sizePolicy().hasHeightForWidth())
        self.f1.setSizePolicy(sizePolicy)
        self.f1.setObjectName("f1")
        self.verticalLayout.addWidget(self.f1)
        self.hsb_f1 = QtWidgets.QScrollBar(self.centralwidget)
        self.hsb_f1.setMaximum(99)
        self.hsb_f1.setSingleStep(1)
        self.hsb_f1.setPageStep(1)
        self.hsb_f1.setOrientation(QtCore.Qt.Horizontal)
        self.hsb_f1.setObjectName("hsb_f1")
        self.verticalLayout.addWidget(self.hsb_f1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_5.setStyleSheet("QGroupBox { border: 0;  }")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 20, 171, 51))
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.followF1 = QtWidgets.QCheckBox(self.groupBox_3)
        self.followF1.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.followF1.setObjectName("followF1")
        self.btn_show = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_show.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.btn_show.setObjectName("btn_show")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 231, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_f1plus = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_f1plus.setGeometry(QtCore.QRect(70, 20, 71, 23))
        self.btn_f1plus.setObjectName("btn_f1plus")
        self.lal_f1Width = QtWidgets.QLabel(self.groupBox_2)
        self.lal_f1Width.setGeometry(QtCore.QRect(10, 20, 61, 23))
        self.lal_f1Width.setObjectName("lal_f1Width")
        self.btn_f1sub = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_f1sub.setGeometry(QtCore.QRect(150, 20, 71, 23))
        self.btn_f1sub.setObjectName("btn_f1sub")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox.setGeometry(QtCore.QRect(260, 20, 171, 51))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.btn_timerStart = QtWidgets.QPushButton(self.groupBox)
        self.btn_timerStart.setGeometry(QtCore.QRect(10, 20, 71, 23))
        self.btn_timerStart.setObjectName("btn_timerStart")
        self.btn_timerStop = QtWidgets.QPushButton(self.groupBox)
        self.btn_timerStop.setGeometry(QtCore.QRect(90, 20, 71, 23))
        self.btn_timerStop.setObjectName("btn_timerStop")
        self.verticalLayout.addWidget(self.groupBox_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("MainWindow", "功能區"))
        self.groupBox_3.setTitle(_translate("MainWindow", "其他功能"))
        self.followF1.setText(_translate("MainWindow", "追蹤最新"))
        self.btn_show.setText(_translate("MainWindow", "顯示輔助線"))
        self.groupBox_2.setTitle(_translate("MainWindow", "顯示資料寬度"))
        self.btn_f1plus.setText(_translate("MainWindow", "+"))
        self.lal_f1Width.setText(_translate("MainWindow", "Width: 3"))
        self.btn_f1sub.setText(_translate("MainWindow", "-"))
        self.groupBox.setTitle(_translate("MainWindow", "Timer Control"))
        self.btn_timerStart.setText(_translate("MainWindow", "START!"))
        self.btn_timerStop.setText(_translate("MainWindow", "STOP!"))

from MatplotlibWidget import MW_SIN
