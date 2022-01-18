from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from utils import CameraThreadWorker


class MainView(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.setEnabled(True)
        QMainWindow.resize(900, 600)
        QMainWindow.setMinimumSize(QSize(900, 600))
        QMainWindow.setMaximumSize(QSize(900, 600))
        QMainWindow.setTabShape(QTabWidget.Rounded)

        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 600))
        self.centralwidget.setMaximumSize(QSize(900, 600))
        
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 550, 601, 51))
        self.videoControlLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.videoControlLayout.setSpacing(8)
        self.videoControlLayout.setObjectName(u"videoControlLayout")
        self.videoControlLayout.setContentsMargins(8, 8, 8, 8)

        # VIDEO CONTROL ---------------------------------------------------------------------
        self.startVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.startVideoBtn.setObjectName(u"startVideoBtn")
        self.videoControlLayout.addWidget(self.startVideoBtn)

        self.pauseVideoBtn = QPushButton(self.horizontalLayoutWidget)
        self.pauseVideoBtn.setObjectName(u"pauseVideoBtn")
        self.videoControlLayout.addWidget(self.pauseVideoBtn)

        self.screenShootBtn = QPushButton(self.horizontalLayoutWidget)
        self.screenShootBtn.setObjectName(u"screenShootBtn")
        self.videoControlLayout.addWidget(self.screenShootBtn)

        self.displayInfoBtn = QPushButton(self.horizontalLayoutWidget)
        self.displayInfoBtn.setObjectName(u"displayInfoBtn")
        self.displayInfoBtn.setMinimumSize(QSize(0, 0))
        self.videoControlLayout.addWidget(self.displayInfoBtn)

        self.videoFrameFormatCb = QComboBox(self.horizontalLayoutWidget)
        self.videoFrameFormatCb.setObjectName(u"videoFrameFormatCb")
        self.videoFrameFormatCb.setEnabled(False)
        self.videoControlLayout.addWidget(self.videoFrameFormatCb)
        # -----------------------------------------------------------------------------------

        self.videoOutpuFrame = QLabel(self.centralwidget)
        self.videoOutpuFrame.setObjectName(u"videoOutpuFrame")
        self.videoOutpuFrame.setGeometry(QRect(0, 0, 600, 551))
        self.videoOutpuFrame.setAutoFillBackground(False)
        self.videoOutpuFrame.setPixmap(QPixmap(u"../resources/camera.png"))
        self.videoOutpuFrame.setScaledContents(True)
        QMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)
        
        self.cameraThread = CameraThreadWorker()
        self.cameraThread.start()
        self.cameraThread.imageUpdate.connect(self.imageUpdateSlot)
    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"Main Window", None))
        self.startVideoBtn.setText(QCoreApplication.translate("QMainWindow", u"Start", None))
        self.pauseVideoBtn.setText(QCoreApplication.translate("QMainWindow", u"Pause", None))
        self.screenShootBtn.setText(QCoreApplication.translate("QMainWindow", u"Screenshoot", None))
        self.displayInfoBtn.setText(QCoreApplication.translate("QMainWindow", u"Display Info", None))
    # retranslateUi

    def imageUpdateSlot(self, Image):
        self.videoOutpuFrame.setPixmap(QPixmap.fromImage(Image))
    
    def startCamera(self):
        self.cameraThread.start()

        self.startVideoBtn.setEnabled(False)
        self.pauseVideoBtn.setEnabled(True)
        self.screenShootBtn.setEnabled(True)
        # TODO set True when video is started
        self.displayInfoBtn.setEnabled(False)
    
    def pauseCamera(self):
        self.cameraThread.start()
        
        self.startVideoBtn.setEnabled(True)
        self.pauseVideoBtn.setEnabled(False)
        self.screenShootBtn.setEnabled(False)
        # TODO set False when video is started
        self.displayInfoBtn.setEnabled(False)
