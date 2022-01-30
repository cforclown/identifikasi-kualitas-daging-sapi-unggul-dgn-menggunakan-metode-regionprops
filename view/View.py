from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QPixmap, QCloseEvent, QShowEvent, QMouseEvent
from PySide2.QtCore import QEvent
from Utils.CameraThreadWorker import CameraThreadWorker
from View.MainView import MainView

class View(QMainWindow):
  lastWindowEvent=None

  def __init__(self):
    super().__init__()
    self.ui = MainView()
    self.ui.setupUi(self)
    self.installEventFilter(self)
    self.setAcceptDrops(True)
    
    self.initialize()
    self.show()

  def initialize(self):
    self.cameraThread = CameraThreadWorker()
    self.cameraThread.imageUpdate.connect(self.imageUpdateCallback)

    self.ui.startVideoBtn.clicked.connect(self.onResumeCamera)
    self.ui.pauseVideoBtn.clicked.connect(self.onPauseCamera)
    self.ui.screenshootBtn.clicked.connect(self.onScreenshoot)
  
  def showEvent(self, event: QShowEvent):
    print('ON SHOW')
    self.cameraThread.start()
    self.onResumeCamera()

  def closeEvent(self, event: QCloseEvent) -> None:
    print('ON CLOSE')
    self.removeEventFilter(self)
    self.cameraThread.stop()

  def eventFilter(self, object, event):
    eventAction=False

    if event.type()==QEvent.Type.Move:
      print('ON MOVE')
      self.cameraThread.pause()
      eventAction=True
    elif self.lastWindowEvent==QEvent.Type.Move and event.type()==QEvent.Type.NonClientAreaMouseButtonRelease and self.cameraThread.isPause==True:
      print('ON MOVE STOP')
      self.cameraThread.resume()
      eventAction=True
    self.lastWindowEvent=event.type()

    return eventAction

  def imageUpdateCallback(self, Image):
    self.ui.videoOutpuFrame.setPixmap(QPixmap.fromImage(Image))
  
  def onPauseCamera(self):
    self.cameraThread.pause()
    self.ui.startVideoBtn.setEnabled(True)
    self.ui.pauseVideoBtn.setEnabled(False)
    self.ui.screenshootBtn.setEnabled(False)
    self.ui.displayInfoBtn.setEnabled(False)

  def onResumeCamera(self):
    self.cameraThread.resume()
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

