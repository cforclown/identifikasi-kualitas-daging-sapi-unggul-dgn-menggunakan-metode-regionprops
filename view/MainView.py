# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainViewQtbyIF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainView(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        MainWindow.setTabShape(QTabWidget.Rounded)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 600))
        self.centralwidget.setMaximumSize(QSize(900, 600))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 550, 601, 51))

        # CAMERA CONTROL ----------------------------------------------------------------------
        self.videoControlLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.videoControlLayout.setSpacing(8)
        self.videoControlLayout.setObjectName(u"videoControlLayout")
        self.videoControlLayout.setContentsMargins(8, 8, 8, 8)

        self.startVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.startVideoBtn.setObjectName(u"startVideoBtn")


        self.pauseVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.pauseVideoBtn.setObjectName(u"pauseVideoBtn")

        self.screenshootBtn = QPushButton(self.horizontalLayoutWidget)
        self.screenshootBtn.setObjectName(u"screenshootBtn")

        self.displayInfoBtn = QPushButton(self.horizontalLayoutWidget)
        self.displayInfoBtn.setObjectName(u"displayInfoBtn")
        self.displayInfoBtn.setMinimumSize(QSize(0, 0))

        self.videoFrameFormatCb = QComboBox(self.horizontalLayoutWidget)
        self.videoFrameFormatCb.setObjectName(u"videoFrameFormatCb")
        self.videoFrameFormatCb.setEnabled(False)

        self.videoControlLayout.addWidget(self.startVideoBtn)
        self.videoControlLayout.addWidget(self.pauseVideoBtn)
        self.videoControlLayout.addWidget(self.screenshootBtn)
        self.videoControlLayout.addWidget(self.displayInfoBtn)
        self.videoControlLayout.addWidget(self.videoFrameFormatCb)
        # -------------------------------------------------------------------------------------


        self.videoOutpuFrame = QLabel(self.centralwidget)
        self.videoOutpuFrame.setObjectName(u"videoOutpuFrame")
        self.videoOutpuFrame.setGeometry(QRect(0, 0, 600, 551))
        self.videoOutpuFrame.setAutoFillBackground(False)
        self.videoOutpuFrame.setPixmap(QPixmap(u"./resources/camera.png"))
        self.videoOutpuFrame.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main Window", None))
        self.startVideoBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pauseVideoBtn.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.screenshootBtn.setText(QCoreApplication.translate("MainWindow", u"Screenshoot", None))
        self.displayInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Display Info", None))
        self.videoOutpuFrame.setText("")
    # retranslateUi
