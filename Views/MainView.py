# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainViewqceycz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainView(object):
    def setupUi(self, MainView):
        if not MainView.objectName():
            MainView.setObjectName(u"MainView")
        MainView.setEnabled(True)
        MainView.resize(800, 600)
        MainView.setMinimumSize(QSize(800, 600))
        MainView.setMaximumSize(QSize(800, 600))
        MainView.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.controllerGroup = QGroupBox(self.centralwidget)
        self.controllerGroup.setObjectName(u"controllerGroup")
        self.controllerGroup.setGeometry(QRect(10, 540, 781, 51))
        self.horizontalLayoutWidget = QWidget(self.controllerGroup)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 781, 41))
        self.controllerLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.controllerLayout.setSpacing(8)
        self.controllerLayout.setObjectName(u"controllerLayout")
        self.controllerLayout.setContentsMargins(8, 8, 8, 8)
        self.startVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.startVideoBtn.setObjectName(u"startVideoBtn")
        self.startVideoBtn.setEnabled(True)
        icon = QIcon()
        icon.addFile(u"./Resources/camera-lens.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startVideoBtn.setIcon(icon)
        self.startVideoBtn.setIconSize(QSize(16, 16))

        self.controllerLayout.addWidget(self.startVideoBtn)

        self.pauseVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.pauseVideoBtn.setObjectName(u"pauseVideoBtn")
        icon1 = QIcon()
        icon1.addFile(u"./Resources/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseVideoBtn.setIcon(icon1)
        self.pauseVideoBtn.setIconSize(QSize(16, 16))

        self.controllerLayout.addWidget(self.pauseVideoBtn)

        self.screenshootBtn = QPushButton(self.horizontalLayoutWidget)
        self.screenshootBtn.setObjectName(u"screenshootBtn")
        icon2 = QIcon()
        icon2.addFile(u"./Resources/crop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.screenshootBtn.setIcon(icon2)

        self.controllerLayout.addWidget(self.screenshootBtn)

        self.displayInfoBtn = QPushButton(self.horizontalLayoutWidget)
        self.displayInfoBtn.setObjectName(u"displayInfoBtn")
        self.displayInfoBtn.setMinimumSize(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u"./Resources/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.displayInfoBtn.setIcon(icon3)

        self.controllerLayout.addWidget(self.displayInfoBtn)

        self.videoModeCb = QComboBox(self.horizontalLayoutWidget)
        self.videoModeCb.addItem("")
        self.videoModeCb.addItem("")
        self.videoModeCb.setObjectName(u"videoModeCb")
        self.videoModeCb.setEnabled(True)
        self.videoModeCb.setEditable(False)

        self.controllerLayout.addWidget(self.videoModeCb)

        self.meatQualityText = QLabel(self.centralwidget)
        self.meatQualityText.setObjectName(u"meatQualityText")
        self.meatQualityText.setGeometry(QRect(700, 10, 91, 31))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.meatQualityText.setFont(font)
        self.meatQualityText.setFrameShape(QFrame.NoFrame)
        self.meatQualityText.setTextFormat(Qt.AutoText)
        self.meatQualityText.setScaledContents(False)
        self.meatQualityText.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.verboseModeLayout = QFrame(self.centralwidget)
        self.verboseModeLayout.setObjectName(u"verboseModeLayout")
        self.verboseModeLayout.setEnabled(True)
        self.verboseModeLayout.setGeometry(QRect(0, 0, 801, 531))
        self.verboseModeLayout.setFrameShape(QFrame.StyledPanel)
        self.verboseModeLayout.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.verboseModeLayout)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 801, 531))
        self.verboseModeGrid = QGridLayout(self.layoutWidget)
        self.verboseModeGrid.setSpacing(4)
        self.verboseModeGrid.setObjectName(u"verboseModeGrid")
        self.verboseModeGrid.setContentsMargins(4, 4, 4, 4)
        self.roiFrame = QLabel(self.layoutWidget)
        self.roiFrame.setObjectName(u"roiFrame")
        self.roiFrame.setPixmap(QPixmap(u"./Resources/camera-lens.png"))
        self.roiFrame.setScaledContents(True)
        self.roiFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.roiFrame, 0, 1, 1, 1)

        self.videoFrame = QLabel(self.layoutWidget)
        self.videoFrame.setObjectName(u"videoFrame")
        self.videoFrame.setPixmap(QPixmap(u"./Resources/camera-lens.png"))
        self.videoFrame.setScaledContents(True)
        self.videoFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.videoFrame, 0, 0, 1, 1)

        self.roiMaskFrame = QLabel(self.layoutWidget)
        self.roiMaskFrame.setObjectName(u"roiMaskFrame")
        self.roiMaskFrame.setPixmap(QPixmap(u"./Resources/camera-lens.png"))
        self.roiMaskFrame.setScaledContents(True)
        self.roiMaskFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.roiMaskFrame, 1, 0, 1, 1)

        self.videoFilteredFrame = QLabel(self.layoutWidget)
        self.videoFilteredFrame.setObjectName(u"videoFilteredFrame")
        self.videoFilteredFrame.setPixmap(QPixmap(u"./Resources/camera-lens.png"))
        self.videoFilteredFrame.setScaledContents(True)
        self.videoFilteredFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.videoFilteredFrame, 1, 1, 1, 1)

        self.defaultModeLayout = QFrame(self.centralwidget)
        self.defaultModeLayout.setObjectName(u"defaultModeLayout")
        self.defaultModeLayout.setGeometry(QRect(0, 0, 801, 531))
        self.defaultModeLayout.setFrameShape(QFrame.StyledPanel)
        self.defaultModeLayout.setFrameShadow(QFrame.Raised)
        self.videoOutpuFrame = QLabel(self.defaultModeLayout)
        self.videoOutpuFrame.setObjectName(u"videoOutpuFrame")
        self.videoOutpuFrame.setGeometry(QRect(0, 0, 801, 540))
        self.videoOutpuFrame.setAutoFillBackground(False)
        self.videoOutpuFrame.setPixmap(QPixmap(u"camera.png"))
        self.videoOutpuFrame.setScaledContents(True)
        self.detectionIndikatorLayout = QFrame(self.centralwidget)
        self.detectionIndikatorLayout.setObjectName(u"detectionIndikatorLayout")
        self.detectionIndikatorLayout.setGeometry(QRect(12, 12, 70, 40))
        self.detectionIndikatorLayout.setFrameShape(QFrame.StyledPanel)
        self.detectionIndikatorLayout.setFrameShadow(QFrame.Raised)
        self.detectionIndicator = QLabel(self.detectionIndikatorLayout)
        self.detectionIndicator.setObjectName(u"detectionIndicator")
        self.detectionIndicator.setGeometry(QRect(0, 0, 48, 32))
        self.detectionIndicator.setTextFormat(Qt.AutoText)
        self.detectionIndicator.setPixmap(QPixmap(u"./Resources/indikator.png"))
        self.detectionIndicator.setScaledContents(True)
        self.detectionIndicator.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        MainView.setCentralWidget(self.centralwidget)
        self.meatQualityText.raise_()
        self.controllerGroup.raise_()
        self.videoFrame.raise_()
        self.roiFrame.raise_()
        self.roiMaskFrame.raise_()
        self.videoFilteredFrame.raise_()
        self.verboseModeLayout.raise_()
        self.defaultModeLayout.raise_()
        self.detectionIndikatorLayout.raise_()

        self.retranslateUi(MainView)

        QMetaObject.connectSlotsByName(MainView)
    # setupUi

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QCoreApplication.translate("MainView", u"Main Window", None))
        self.controllerGroup.setTitle(QCoreApplication.translate("MainView", u"Control", None))
        self.startVideoBtn.setText(QCoreApplication.translate("MainView", u"Start", None))
        self.pauseVideoBtn.setText(QCoreApplication.translate("MainView", u"Pause", None))
        self.screenshootBtn.setText(QCoreApplication.translate("MainView", u"Screenshoot", None))
        self.displayInfoBtn.setText(QCoreApplication.translate("MainView", u"Info", None))
        self.videoModeCb.setItemText(0, QCoreApplication.translate("MainView", u"Default", None))
        self.videoModeCb.setItemText(1, QCoreApplication.translate("MainView", u"Verbose", None))

        self.videoModeCb.setCurrentText(QCoreApplication.translate("MainView", u"Default", None))
        self.meatQualityText.setText(QCoreApplication.translate("MainView", u"<html><head/><body><p><span style=\" font-weight:600; color:#00e800;\">BAIK</span>/<span style=\" font-weight:600; color:#ff0000;\">BURUK</span></p></body></html>", None))
        self.videoOutpuFrame.setText("")
        self.detectionIndicator.setText("")
    # retranslateUi

