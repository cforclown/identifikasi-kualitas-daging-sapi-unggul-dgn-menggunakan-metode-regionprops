# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsViewlASJsq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingsView(object):
    def setupUi(self, SettingsView):
        if not SettingsView.objectName():
            SettingsView.setObjectName(u"SettingsView")
        SettingsView.resize(600, 400)
        SettingsView.setMinimumSize(QSize(600, 400))
        SettingsView.setMaximumSize(QSize(600, 400))
        self.centralwidget = QWidget(SettingsView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 400))
        self.centralwidget.setMaximumSize(QSize(600, 400))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 601, 351))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 601, 351))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(8, 8, 8, 12)
        self.separator = QLabel(self.layoutWidget)
        self.separator.setObjectName(u"separator")

        self.gridLayout.addWidget(self.separator, 5, 0, 1, 1)

        self.noiseReductionTypeText = QLabel(self.layoutWidget)
        self.noiseReductionTypeText.setObjectName(u"noiseReductionTypeText")

        self.gridLayout.addWidget(self.noiseReductionTypeText, 2, 0, 1, 1)

        self.cameraPortText = QLabel(self.layoutWidget)
        self.cameraPortText.setObjectName(u"cameraPortText")

        self.gridLayout.addWidget(self.cameraPortText, 0, 0, 1, 1)

        self.medianBlurParamText = QLabel(self.layoutWidget)
        self.medianBlurParamText.setObjectName(u"medianBlurParamText")
        self.medianBlurParamText.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.medianBlurParamText, 3, 0, 1, 1)

        self.cameraResText = QLabel(self.layoutWidget)
        self.cameraResText.setObjectName(u"cameraResText")

        self.gridLayout.addWidget(self.cameraResText, 1, 0, 1, 1)

        self.cameraPortCb = QComboBox(self.layoutWidget)
        self.cameraPortCb.setObjectName(u"cameraPortCb")

        self.gridLayout.addWidget(self.cameraPortCb, 0, 1, 1, 1)

        self.medianBlurParamValueText = QLabel(self.layoutWidget)
        self.medianBlurParamValueText.setObjectName(u"medianBlurParamValueText")
        self.medianBlurParamValueText.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.medianBlurParamValueText, 3, 1, 1, 1)

        self.cameraResCb = QComboBox(self.layoutWidget)
        self.cameraResCb.setObjectName(u"cameraResCb")

        self.gridLayout.addWidget(self.cameraResCb, 1, 1, 1, 1)

        self.noiseReductionTypeCb = QComboBox(self.layoutWidget)
        self.noiseReductionTypeCb.setObjectName(u"noiseReductionTypeCb")
        self.noiseReductionTypeCb.setEnabled(False)

        self.gridLayout.addWidget(self.noiseReductionTypeCb, 2, 1, 1, 1)

        self.detectionParamsText = QLabel(self.layoutWidget)
        self.detectionParamsText.setObjectName(u"detectionParamsText")
        self.detectionParamsText.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.detectionParamsText, 4, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.lowRedValueText = QLabel(self.layoutWidget)
        self.lowRedValueText.setObjectName(u"lowRedValueText")
        self.lowRedValueText.setMinimumSize(QSize(0, 32))
        self.lowRedValueText.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_4.addWidget(self.lowRedValueText)

        self.highRedValueText = QLabel(self.layoutWidget)
        self.highRedValueText.setObjectName(u"highRedValueText")
        self.highRedValueText.setMinimumSize(QSize(0, 32))
        self.highRedValueText.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_4.addWidget(self.highRedValueText)

        self.changeDetectionParamsBtn = QPushButton(self.layoutWidget)
        self.changeDetectionParamsBtn.setObjectName(u"changeDetectionParamsBtn")

        self.verticalLayout_4.addWidget(self.changeDetectionParamsBtn)


        self.gridLayout.addLayout(self.verticalLayout_4, 4, 1, 1, 1)

        self.gridLayout.setRowStretch(4, 1)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 360, 601, 41))
        self.controlLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.controlLayout.setSpacing(8)
        self.controlLayout.setObjectName(u"controlLayout")
        self.controlLayout.setContentsMargins(8, 0, 8, 0)
        self.saveBtn = QPushButton(self.horizontalLayoutWidget)
        self.saveBtn.setObjectName(u"saveBtn")
        icon = QIcon()
        icon.addFile(u"Resources/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon)

        self.controlLayout.addWidget(self.saveBtn)

        self.closeBtn = QPushButton(self.horizontalLayoutWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        icon1 = QIcon()
        icon1.addFile(u"Resources/delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)

        self.controlLayout.addWidget(self.closeBtn)

        SettingsView.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsView)

        QMetaObject.connectSlotsByName(SettingsView)
    # setupUi

    def retranslateUi(self, SettingsView):
        SettingsView.setWindowTitle(QCoreApplication.translate("SettingsView", u"MainWindow", None))
        self.separator.setText("")
        self.noiseReductionTypeText.setText(QCoreApplication.translate("SettingsView", u"Noise Reduction Type", None))
        self.cameraPortText.setText(QCoreApplication.translate("SettingsView", u"Camera Port", None))
        self.medianBlurParamText.setText(QCoreApplication.translate("SettingsView", u"Median Blur Param", None))
        self.cameraResText.setText(QCoreApplication.translate("SettingsView", u"Camera Resolution", None))
        self.medianBlurParamValueText.setText(QCoreApplication.translate("SettingsView", u"5", None))
        self.detectionParamsText.setText(QCoreApplication.translate("SettingsView", u"Detection Params", None))
        self.lowRedValueText.setText(QCoreApplication.translate("SettingsView", u"LOW RED [170, 0, 0] [180, 255, 255]", None))
        self.highRedValueText.setText(QCoreApplication.translate("SettingsView", u"HIGH RED [0, 0, 0] [30, 255, 255]", None))
        self.changeDetectionParamsBtn.setText(QCoreApplication.translate("SettingsView", u"Change Value", None))
        self.saveBtn.setText(QCoreApplication.translate("SettingsView", u" Save", None))
        self.closeBtn.setText(QCoreApplication.translate("SettingsView", u" Close", None))
    # retranslateUi

