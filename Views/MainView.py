# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainViewLaybEy.ui'
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
        icon.addFile(u"Resources/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startVideoBtn.setIcon(icon)
        self.startVideoBtn.setIconSize(QSize(16, 16))

        self.controllerLayout.addWidget(self.startVideoBtn)

        self.pauseVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.pauseVideoBtn.setObjectName(u"pauseVideoBtn")
        icon1 = QIcon()
        icon1.addFile(u"Resources/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseVideoBtn.setIcon(icon1)
        self.pauseVideoBtn.setIconSize(QSize(16, 16))

        self.controllerLayout.addWidget(self.pauseVideoBtn)

        self.screenshootBtn = QPushButton(self.horizontalLayoutWidget)
        self.screenshootBtn.setObjectName(u"screenshootBtn")
        icon2 = QIcon()
        icon2.addFile(u"Resources/crop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.screenshootBtn.setIcon(icon2)

        self.controllerLayout.addWidget(self.screenshootBtn)

        self.displayInfoBtn = QPushButton(self.horizontalLayoutWidget)
        self.displayInfoBtn.setObjectName(u"displayInfoBtn")
        self.displayInfoBtn.setEnabled(False)
        self.displayInfoBtn.setMinimumSize(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u"Resources/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.displayInfoBtn.setIcon(icon3)

        self.controllerLayout.addWidget(self.displayInfoBtn)

        self.videoModeCb = QComboBox(self.horizontalLayoutWidget)
        self.videoModeCb.addItem("")
        self.videoModeCb.addItem("")
        self.videoModeCb.setObjectName(u"videoModeCb")
        self.videoModeCb.setEnabled(True)
        self.videoModeCb.setEditable(False)

        self.controllerLayout.addWidget(self.videoModeCb)

        self.settingsBtn = QPushButton(self.horizontalLayoutWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setEnabled(True)
        icon4 = QIcon()
        icon4.addFile(u"Resources/cog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)

        self.controllerLayout.addWidget(self.settingsBtn)

        self.verboseModeFrame = QFrame(self.centralwidget)
        self.verboseModeFrame.setObjectName(u"verboseModeFrame")
        self.verboseModeFrame.setGeometry(QRect(0, 0, 801, 531))
        self.verboseModeFrame.setFrameShape(QFrame.StyledPanel)
        self.verboseModeFrame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.verboseModeFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 801, 531))
        self.verboseModeGrid = QGridLayout(self.layoutWidget)
        self.verboseModeGrid.setSpacing(2)
        self.verboseModeGrid.setObjectName(u"verboseModeGrid")
        self.verboseModeGrid.setContentsMargins(0, 0, 0, 0)
        self.roiFrame = QLabel(self.layoutWidget)
        self.roiFrame.setObjectName(u"roiFrame")
        self.roiFrame.setPixmap(QPixmap(u"Resources/camera-lens.png"))
        self.roiFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.roiFrame, 0, 1, 1, 1)

        self.videoFrame = QLabel(self.layoutWidget)
        self.videoFrame.setObjectName(u"videoFrame")
        self.videoFrame.setPixmap(QPixmap(u"Resources/camera-lens.png"))
        self.videoFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.videoFrame, 0, 0, 1, 1)

        self.videoFilteredFrame = QLabel(self.layoutWidget)
        self.videoFilteredFrame.setObjectName(u"videoFilteredFrame")
        self.videoFilteredFrame.setPixmap(QPixmap(u"Resources/camera-lens.png"))
        self.videoFilteredFrame.setScaledContents(False)
        self.videoFilteredFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.videoFilteredFrame, 1, 1, 1, 1)

        self.roiMaskFrame = QLabel(self.layoutWidget)
        self.roiMaskFrame.setObjectName(u"roiMaskFrame")
        self.roiMaskFrame.setPixmap(QPixmap(u"Resources/camera-lens.png"))
        self.roiMaskFrame.setAlignment(Qt.AlignCenter)

        self.verboseModeGrid.addWidget(self.roiMaskFrame, 1, 0, 1, 1)

        self.defaultModeFrame = QFrame(self.centralwidget)
        self.defaultModeFrame.setObjectName(u"defaultModeFrame")
        self.defaultModeFrame.setGeometry(QRect(0, 0, 801, 531))
        self.defaultModeFrame.setFrameShape(QFrame.StyledPanel)
        self.defaultModeFrame.setFrameShadow(QFrame.Raised)
        self.videoOutpuFrame = QLabel(self.defaultModeFrame)
        self.videoOutpuFrame.setObjectName(u"videoOutpuFrame")
        self.videoOutpuFrame.setGeometry(QRect(0, 0, 801, 531))
        self.videoOutpuFrame.setAutoFillBackground(False)
        self.videoOutpuFrame.setPixmap(QPixmap(u"Resources/camera.png"))
        self.videoOutpuFrame.setScaledContents(False)
        self.videoOutpuFrame.setAlignment(Qt.AlignCenter)
        self.detectionIndicatorFrame = QFrame(self.centralwidget)
        self.detectionIndicatorFrame.setObjectName(u"detectionIndicatorFrame")
        self.detectionIndicatorFrame.setGeometry(QRect(8, 8, 48, 32))
        self.detectionIndicatorFrame.setFrameShape(QFrame.StyledPanel)
        self.detectionIndicatorFrame.setFrameShadow(QFrame.Raised)
        self.detectionIndicator = QLabel(self.detectionIndicatorFrame)
        self.detectionIndicator.setObjectName(u"detectionIndicator")
        self.detectionIndicator.setGeometry(QRect(0, 0, 48, 32))
        self.detectionIndicator.setTextFormat(Qt.AutoText)
        self.detectionIndicator.setPixmap(QPixmap(u"Resources/indikator.png"))
        self.detectionIndicator.setScaledContents(True)
        self.detectionIndicator.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.meatQualityFrame = QFrame(self.centralwidget)
        self.meatQualityFrame.setObjectName(u"meatQualityFrame")
        self.meatQualityFrame.setGeometry(QRect(692, 8, 100, 25))
        self.meatQualityFrame.setFrameShape(QFrame.StyledPanel)
        self.meatQualityFrame.setFrameShadow(QFrame.Raised)
        self.badTextFrame = QFrame(self.meatQualityFrame)
        self.badTextFrame.setObjectName(u"badTextFrame")
        self.badTextFrame.setGeometry(QRect(0, 0, 100, 25))
        self.badTextFrame.setFrameShape(QFrame.StyledPanel)
        self.badTextFrame.setFrameShadow(QFrame.Raised)
        self.badText = QLabel(self.badTextFrame)
        self.badText.setObjectName(u"badText")
        self.badText.setGeometry(QRect(0, 0, 100, 25))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.badText.setFont(font)
        self.badText.setFrameShape(QFrame.NoFrame)
        self.badText.setTextFormat(Qt.AutoText)
        self.badText.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.goodTextFrame = QFrame(self.meatQualityFrame)
        self.goodTextFrame.setObjectName(u"goodTextFrame")
        self.goodTextFrame.setGeometry(QRect(0, 0, 100, 25))
        self.goodTextFrame.setFrameShape(QFrame.StyledPanel)
        self.goodTextFrame.setFrameShadow(QFrame.Raised)
        self.goodText = QLabel(self.goodTextFrame)
        self.goodText.setObjectName(u"goodText")
        self.goodText.setGeometry(QRect(0, 0, 100, 25))
        self.goodText.setFont(font)
        self.goodText.setFrameShape(QFrame.NoFrame)
        self.goodText.setTextFormat(Qt.AutoText)
        self.goodText.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.mediumTextFrame = QFrame(self.meatQualityFrame)
        self.mediumTextFrame.setObjectName(u"mediumTextFrame")
        self.mediumTextFrame.setGeometry(QRect(0, 0, 100, 25))
        self.mediumTextFrame.setFrameShape(QFrame.StyledPanel)
        self.mediumTextFrame.setFrameShadow(QFrame.Raised)
        self.mediumText = QLabel(self.mediumTextFrame)
        self.mediumText.setObjectName(u"mediumText")
        self.mediumText.setGeometry(QRect(0, 0, 100, 25))
        self.mediumText.setFont(font)
        self.mediumText.setFrameShape(QFrame.NoFrame)
        self.mediumText.setTextFormat(Qt.AutoText)
        self.mediumText.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        MainView.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainView)

        QMetaObject.connectSlotsByName(MainView)
    # setupUi

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QCoreApplication.translate("MainView", u"Main Window", None))
        self.controllerGroup.setTitle(QCoreApplication.translate("MainView", u"Control", None))
        self.startVideoBtn.setText(QCoreApplication.translate("MainView", u" Start", None))
        self.pauseVideoBtn.setText(QCoreApplication.translate("MainView", u" Pause", None))
        self.screenshootBtn.setText(QCoreApplication.translate("MainView", u" Screenshoot", None))
        self.displayInfoBtn.setText(QCoreApplication.translate("MainView", u" Info", None))
        self.videoModeCb.setItemText(0, QCoreApplication.translate("MainView", u"Default", None))
        self.videoModeCb.setItemText(1, QCoreApplication.translate("MainView", u"Verbose", None))

        self.videoModeCb.setCurrentText(QCoreApplication.translate("MainView", u"Default", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainView", u" Settings", None))
        self.videoOutpuFrame.setText("")
        self.detectionIndicator.setText("")
        self.badText.setText(QCoreApplication.translate("MainView", u"<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">BAD</span></p></body></html>", None))
        self.goodText.setText(QCoreApplication.translate("MainView", u"<html><head/><body><p><span style=\" font-weight:600; color:#00df00;\">GOOD</span></p></body></html>", None))
        self.mediumText.setText(QCoreApplication.translate("MainView", u"<html><head/><body><p><span style=\" font-weight:600; color:#00df00;\">MEDIUM</span></p></body></html>", None))
    # retranslateUi

