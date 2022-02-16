from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QPixmap, QCloseEvent, QShowEvent
from PySide2.QtCore import QEvent, QCoreApplication
from Utils.CameraThreadWorker import MEATQUALITY, CameraThreadWorker
from Views.MainView import Ui_MainView


class View(QMainWindow):
  lastWindowEvent=None

  def __init__(self):
    super().__init__()
    self.ui = Ui_MainView()
    self.ui.setupUi(self)
    self.installEventFilter(self)
    self.setAcceptDrops(True)
    
    self.initialize()
    self.show()

  def initialize(self):
    self.ui.videoOutpuFrame.setScaledContents(True)
    self.ui.videoFrame.setScaledContents(True)
    self.ui.roiFrame.setScaledContents(True)
    self.ui.roiMaskFrame.setScaledContents(True)
    self.ui.videoFilteredFrame.setScaledContents(True)

    self.ui.startVideoBtn.clicked.connect(self.onResumeCamera)
    self.ui.pauseVideoBtn.clicked.connect(self.onPauseCamera)
    self.ui.screenshootBtn.clicked.connect(self.onScreenshoot)
    self.ui.videoModeCb.currentTextChanged.connect(self.onModeChange)

    self.cameraThread = CameraThreadWorker()
    self.cameraThread.frameUpdate.connect(self.imageUpdateCallback)
    self.cameraThread.roiUpdate.connect(self.roiUpdateCallback)
    self.cameraThread.roiMaskUpdate.connect(self.roiMaskUpdateCallback)
    self.cameraThread.filteredUpdate.connect(self.videoFilteredUpdateCallback)
    self.cameraThread.meatDetected.connect(self.meatDetected)
  
  # ====================================================================== EVENT ======================================================================
  def showEvent(self, event: QShowEvent):
    print('ON SHOW')
    self.cameraThread.start()
    self.onResumeCamera()
    self.meatDetected(False)

  def closeEvent(self, event: QCloseEvent) -> None:
    print('ON CLOSE')
    self.removeEventFilter(self)
    self.cameraThread.stop()

  def eventFilter(self, object, event):
    eventAction=False

    if event.type()==QEvent.Type.Move:
      self.cameraThread.startBreak()
      eventAction=True
      print('ON MOVE')
    elif self.lastWindowEvent==QEvent.Type.Move and event.type()==QEvent.Type.NonClientAreaMouseButtonRelease and self.cameraThread.isBreak:
      print('ON MOVE STOP')
      self.cameraThread.endBreak()
      eventAction=True
    self.lastWindowEvent=event.type()

    return eventAction
  # ===================================================================================================================================================

  # =============================================================== CAMERA WORKER EVENTs ==============================================================
  def imageUpdateCallback(self, frame):
    if not self.cameraThread.verboseMode:
      self.ui.videoOutpuFrame.setPixmap(QPixmap.fromImage(frame))
    else:
      self.ui.videoFrame.setPixmap(QPixmap.fromImage(frame))
  def roiUpdateCallback(self, frame):
    self.ui.roiFrame.setPixmap(QPixmap.fromImage(frame))
  def roiMaskUpdateCallback(self, frame):
    self.ui.roiMaskFrame.setPixmap(QPixmap.fromImage(frame))
  def videoFilteredUpdateCallback(self, frame):
    self.ui.videoFilteredFrame.setPixmap(QPixmap.fromImage(frame))
  
  def meatDetected(self, isDetected, quality=MEATQUALITY.GOOD):
    if isDetected:
      self.ui.detectionIndicatorFrame.show()
      if quality is MEATQUALITY.GOOD:
        self.ui.goodTextFrame.show()
        self.ui.mediumText.hide()
        self.ui.badTextFrame.hide()
      elif quality is MEATQUALITY.MEDIUM:
        self.ui.goodTextFrame.hide()
        self.ui.mediumText.show()
        self.ui.badTextFrame.hide()
      elif quality is MEATQUALITY.MEDIUM:
        self.ui.goodTextFrame.hide()
        self.ui.mediumText.hide()
        self.ui.badTextFrame.show()
      else:
        self.ui.goodTextFrame.hide()
        self.ui.mediumText.hide()
        self.ui.badTextFrame.hide()
    else:
      self.ui.detectionIndicatorFrame.hide()
      self.ui.goodTextFrame.hide()
      self.ui.mediumText.hide()
      self.ui.badTextFrame.hide()
  # ===================================================================================================================================================

  def onPauseCamera(self):
    self.cameraThread.pause()
    self.ui.startVideoBtn.setEnabled(True)
    self.ui.pauseVideoBtn.setEnabled(False)
    self.ui.screenshootBtn.setEnabled(False)
    self.ui.displayInfoBtn.setEnabled(False)

  def onResumeCamera(self):
    self.cameraThread.resume()
    self.cameraThread.endBreak()
    self.ui.startVideoBtn.setEnabled(False)
    self.ui.pauseVideoBtn.setEnabled(True)
    self.ui.screenshootBtn.setEnabled(True)
    self.ui.displayInfoBtn.setEnabled(True)
  
  def onScreenshoot(self):
    self.ui.startVideoBtn.setEnabled(False)
    self.ui.pauseVideoBtn.setEnabled(False)
    self.ui.screenshootBtn.setEnabled(False)
    self.ui.displayInfoBtn.setEnabled(False)
    self.cameraThread.screenshoot()
    self.ui.startVideoBtn.setEnabled(False)
    self.ui.pauseVideoBtn.setEnabled(True)
    self.ui.screenshootBtn.setEnabled(True)
    self.ui.displayInfoBtn.setEnabled(True)

  def onModeChange(self, value):
    if value=='Verbose':
      self.ui.verboseModeFrame.show()
      self.ui.defaultModeFrame.hide()
    else:
      self.ui.verboseModeFrame.hide()
      self.ui.defaultModeFrame.show()
    self.cameraThread.changeMode(value)
