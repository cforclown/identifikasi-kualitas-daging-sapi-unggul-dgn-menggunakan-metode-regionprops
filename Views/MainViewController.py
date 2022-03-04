from time import sleep
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QPixmap, QCloseEvent, QShowEvent
from PySide2.QtCore import QEvent
from Utils.CameraThreadWorker import MEATQUALITY, CameraThreadWorker
from Views.MainView import Ui_MainView
from Views.SettingsViewController import View as SettingsView


class View(QMainWindow):
  DEFAULT_MODE='Default'
  VERBOSE_MODE='Verbose'

  def __init__(self):
    super().__init__()
    
    self.lastWindowEvent=None
    self.ui = Ui_MainView()
    self.ui.setupUi(self)
    self.installEventFilter(self)
    self.setAcceptDrops(True)

    self.currentMode=self.DEFAULT_MODE
    
    self.initialize()
    self.show()

  def initialize(self):
    self.ui.videoModeCb.clear()
    self.ui.videoModeCb.addItem(self.DEFAULT_MODE)
    self.ui.videoModeCb.addItem(self.VERBOSE_MODE)

    self.ui.videoOutpuFrame.setScaledContents(True)
    self.ui.videoFrame.setScaledContents(True)
    self.ui.roiFrame.setScaledContents(True)
    self.ui.roiMaskFrame.setScaledContents(True)
    self.ui.videoFilteredFrame.setScaledContents(True)

    self.ui.startVideoBtn.clicked.connect(self.onResumeCamera)
    self.ui.pauseVideoBtn.clicked.connect(self.onPauseCamera)
    self.ui.screenshootBtn.clicked.connect(self.onScreenshoot)
    self.ui.videoModeCb.currentTextChanged.connect(self.onModeChange)
    self.ui.settingsBtn.clicked.connect(self.onSettingsClick)

    self.initCameraThreadWorker()
  
  def initCameraThreadWorker(self):
    self.cameraThread = CameraThreadWorker()
    self.cameraThread.frameUpdate.connect(self.imageUpdateCallback)
    self.cameraThread.roiUpdate.connect(self.roiUpdateCallback)
    self.cameraThread.roiMaskUpdate.connect(self.roiMaskUpdateCallback)
    self.cameraThread.filteredUpdate.connect(self.videoFilteredUpdateCallback)
    self.cameraThread.meatDetected.connect(self.meatDetected)
    self.cameraThread.changeMode(self.currentMode)

  def startCameraThreadWorker(self):
    self.cameraThread.start()
  
  def stopCameraThreadWorker(self):
    self.cameraThread.breakWork()
    self.cameraThread.frameUpdate.disconnect()
    self.cameraThread.roiUpdate.disconnect()
    self.cameraThread.roiMaskUpdate.disconnect()
    self.cameraThread.filteredUpdate.disconnect()
    self.cameraThread.meatDetected.disconnect()
    self.cameraThread.quit()
    self.cameraThread.wait()
    while self.cameraThread.isRunning():
      sleep(0.1)
    self.cameraThread=None
    sleep(1)
    print('[TRAINER CAM THREAD] released')
  # ====================================================================== EVENT ======================================================================
  def showEvent(self, event: QShowEvent):
    self.onResumeCamera()
    self.meatDetected(False)
    self.startCameraThreadWorker()

  def closeEvent(self, event: QCloseEvent) -> None:
    self.removeEventFilter(self)
    self.stopCameraThreadWorker()

  def eventFilter(self, object, event):
    eventAction=False

    if event.type()==QEvent.Type.Move:
      self.cameraThread.startBreak()
      eventAction=True
    elif self.lastWindowEvent==QEvent.Type.Move and event.type()==QEvent.Type.NonClientAreaMouseButtonRelease and self.cameraThread.isBreak:
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
    self.currentMode=value
    if self.currentMode=='Verbose':
      self.ui.verboseModeFrame.show()
      self.ui.defaultModeFrame.hide()
    else:
      self.ui.verboseModeFrame.hide()
      self.ui.defaultModeFrame.show()
    self.cameraThread.changeMode(self.currentMode)

  def onSettingsClick(self):
    self.stopCameraThreadWorker()
    self.settingsWindow=SettingsView(self.onSettingsClosed)
    self.ui.controllerGroup.setEnabled(False)

  def onSettingsClosed(self):
    self.settingsWindow.close()
    self.settingsWindow.destroy()
    self.settingsWindow=None
    self.initCameraThreadWorker()
    self.startCameraThreadWorker()
    # self.ui.verboseModeFrame.hide()
    # self.ui.defaultModeFrame.show()
    # self.cameraThread.changeMode(False)
    self.ui.controllerGroup.setEnabled(True)
