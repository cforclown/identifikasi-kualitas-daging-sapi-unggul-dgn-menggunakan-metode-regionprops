from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QPixmap, QCloseEvent, QShowEvent
from PySide2.QtCore import QEvent, QCoreApplication
from Utils.TrainerThreadWorker import MEATQUALITY
from Utils.TrainerThreadWorker import TrainerThreadWorker
from Views.TrainerView import Ui_TrainerView


class View(QMainWindow):
  lastWindowEvent=None

  def __init__(self):
    super().__init__()
    self.ui = Ui_TrainerView()
    self.ui.setupUi(self)
    self.installEventFilter(self)
    self.setAcceptDrops(True)
    
    self.initialize()
    self.show()

  def initialize(self):
    self.ui.image.setScaledContents(True)
    self.ui.imageBinary.setScaledContents(True)
    self.ui.imageBinaryEnhanced.setScaledContents(True)

    self.imgProcessingThread = TrainerThreadWorker()
    self.imgProcessingThread.frameUpdate.connect(self.imageUpdateCallback)
    self.imgProcessingThread.roiUpdate.connect(self.roiUpdateCallback)
    self.imgProcessingThread.roiMaskUpdate.connect(self.roiMaskUpdateCallback)
    self.imgProcessingThread.filteredUpdate.connect(self.videoFilteredUpdateCallback)
    self.imgProcessingThread.meatDetected.connect(self.meatDetected)
  
  # ====================================================================== EVENT ======================================================================
  def showEvent(self, event: QShowEvent):
    print('ON SHOW')
    self.imgProcessingThread.start()
    self.onResumeCamera()
    self.meatDetected(False)

  def closeEvent(self, event: QCloseEvent) -> None:
    print('ON CLOSE')
    self.removeEventFilter(self)
    self.imgProcessingThread.stop()

  def eventFilter(self, object, event):
    eventAction=False

    if event.type()==QEvent.Type.Move:
      self.imgProcessingThread.startBreak()
      eventAction=True
      print('ON MOVE')
    elif self.lastWindowEvent==QEvent.Type.Move and event.type()==QEvent.Type.NonClientAreaMouseButtonRelease and self.imgProcessingThread.isBreak:
      print('ON MOVE STOP')
      self.imgProcessingThread.endBreak()
      eventAction=True
    self.lastWindowEvent=event.type()

    return eventAction
  # ===================================================================================================================================================

  # =============================================================== CAMERA WORKER EVENTs ==============================================================
  def imageUpdateCallback(self, frame):
    if not self.imgProcessingThread.verboseMode:
      self.ui.image.setPixmap(QPixmap.fromImage(frame))
    else:
      self.ui.videoFrame.setPixmap(QPixmap.fromImage(frame))
  def image(self, frame):
    self.ui.roiFrame.setPixmap(QPixmap.fromImage(frame))
  def roiMaskUpdateCallback(self, frame):
    self.ui.roiMaskFrame.setPixmap(QPixmap.fromImage(frame))
  def videoFilteredUpdateCallback(self, frame):
    self.ui.videoFilteredFrame.setPixmap(QPixmap.fromImage(frame))
  # ===================================================================================================================================================

  def onSaveParams(self):
    print('on save params')

  def onChangeImage(self):
    print('on change image')
  
  def onSaveToJSON(self):
    print('on save to JSON')

  def onRemoveParams(self, value):
    print('on remove params')
