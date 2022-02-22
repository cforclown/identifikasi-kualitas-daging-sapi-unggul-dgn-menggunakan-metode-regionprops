from time import sleep
import json
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtGui import QPixmap, QCloseEvent, QShowEvent
from PySide2.QtCore import Qt
from Utils.SettingsManager import Settings
from Utils.TrainerThreadWorker import TrainerThreadWorker
from Views.TrainerView import Ui_TrainerView


class View(QMainWindow):
  lastWindowEvent=None

  def __init__(self, onCloseCallback=None):
    super().__init__()
    self.ui = Ui_TrainerView()
    self.ui.setupUi(self)
    self.onCloseCallback=onCloseCallback
    self.setAcceptDrops(True)

    if onCloseCallback is not None:
      self.setWindowModality(Qt.WindowModal)
    
    self.settings=Settings().get()
    self.currentDetectionParams=Settings.LOW_RED_KEY
    self.imgUri=None
    self.imgProcessingThread=None
    self.initialize()
    
    self.show()

  def initialize(self):
    self.ui.image.setScaledContents(True)
    self.ui.imageBinary.setScaledContents(True)
    self.ui.imageBinaryEnhanced.setScaledContents(True)

    self.ui.saveParamsBtn.clicked.connect(self.onSaveParams)
    self.ui.resetParamsBtn.clicked.connect(self.onResetParams)
    self.ui.useImgBtn.clicked.connect(self.onUseImage)
    self.ui.useCameraBtn.clicked.connect(self.onUseCamera)
    self.ui.closeBtn.clicked.connect(self.onCloseClick)

    self.ui.lowRedValueTextBtn.clicked.connect(self.onLowRedValueTextBtn)
    self.ui.highRedValueTextBtn.clicked.connect(self.onHighRedValueTextBtn)

    self.ui.lowHSlider.valueChanged.connect(self.onLowHChange)
    self.ui.highHSlider.valueChanged.connect(self.onHighHChange)
    self.ui.lowSSlider.valueChanged.connect(self.onLowSChange)
    self.ui.highSSlider.valueChanged.connect(self.onHighSChange)
    self.ui.lowVSlider.valueChanged.connect(self.onLowVChange)
    self.ui.highVSlider.valueChanged.connect(self.onHighVChange)
    self.ui.noiseReductionParamSlider.valueChanged.connect(self.onMedianBlurScaleChange)

    self.initTrainerTreadWorker()
    self.initializeSliders()

  def initializeSliders(self):
    self.updateUICurrentDetectionParamsState()
    self.ui.lowHSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY][0])
    self.ui.highHSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY][0])
    self.ui.lowSSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY][1])
    self.ui.highSSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY][1])
    self.ui.lowVSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY][2])
    self.ui.highVSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY][2])
    self.ui.noiseReductionParamSlider.setValue(self.settings.detectionParams[self.currentDetectionParams][Settings.MEDIAN_BLUR_SCALE_KEY])
    self.onLowHChange()
    self.onHighHChange()
    self.onLowSChange()
    self.onHighSChange()
    self.onLowVChange()
    self.onHighVChange()
    self.onMedianBlurScaleChange()

  def initTrainerTreadWorker(self):
    self.imgProcessingThread = TrainerThreadWorker()
    self.imgProcessingThread.init(self.currentDetectionParams)
    self.imgProcessingThread.imgUpdate.connect(self.imgUpdateCallback)
    self.imgProcessingThread.imgBinUpdate.connect(self.imgBinUpdateCallback)
    self.imgProcessingThread.imgBinEnhancedUpdate.connect(self.imgBinEnhancedUpdateCallback)

  def startTrainerTreadWorker(self):
    if self.imgProcessingThread is None:
      print('THREAD is None')
      return
    self.imgProcessingThread.start()
  
  def stopTrainerThreadWorker(self):
    if self.imgProcessingThread is not None:
      self.imgProcessingThread.breakWork()
      self.imgProcessingThread.imgUpdate.disconnect()
      self.imgProcessingThread.imgBinUpdate.disconnect()
      self.imgProcessingThread.imgBinEnhancedUpdate.disconnect()
      self.imgProcessingThread.quit()
      self.imgProcessingThread.wait()
      while self.imgProcessingThread.isRunning():
        sleep(0.1)
    self.imgProcessingThread=None
    sleep(0.5)

  # ====================================================================== EVENT ======================================================================
  def showEvent(self, event: QShowEvent):
    self.imgProcessingThread.start()

  def closeEvent(self, event: QCloseEvent):
    self.stopTrainerThreadWorker()
    if self.onCloseCallback is not None:
      self.onCloseCallback()

  def onCloseClick(self):
    self.close()
  # ===================================================================================================================================================

  # =============================================================== CAMERA WORKER EVENTs ==============================================================
  def imgUpdateCallback(self, frame):
      self.ui.image.setPixmap(QPixmap.fromImage(frame))
  def imgBinUpdateCallback(self, frame):
    self.ui.imageBinary.setPixmap(QPixmap.fromImage(frame))
  def imgBinEnhancedUpdateCallback(self, frame):
    self.ui.imageBinaryEnhanced.setPixmap(QPixmap.fromImage(frame))
  # ===================================================================================================================================================

  def onSaveParams(self):
    self.settings = Settings().updateDetectionParams(
      json.loads(json.dumps(self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY])),
      json.loads(json.dumps(self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY])),
      self.settings.detectionParams[self.currentDetectionParams][Settings.BLUR_TYPE_KEY],
      self.settings.detectionParams[self.currentDetectionParams][Settings.MEDIAN_BLUR_SCALE_KEY],
      self.settings.detectionParams[self.currentDetectionParams][Settings.GAUSSIAN_BLUR_SCALE_KEY],
      (True if self.currentDetectionParams is Settings.LOW_RED_KEY else False)
    )

  def onResetParams(self):
    self.settings.detectionParams=Settings().get().detectionParams
    self.initializeSliders

  def onUseImage(self):
    print('COMING SOON')
    self.openImg()
    self.ui.useImgBtn.setEnabled(False)
    self.ui.useCameraBtn.setEnabled(True)
  
  def onUseCamera(self):
    self.imgUri=None
    self.imgProcessingThread.useCamera()
    self.ui.useImgBtn.setEnabled(True)
    self.ui.useCameraBtn.setEnabled(False)
  
  def onLowRedValueTextBtn(self):
    self.currentDetectionParams=Settings.LOW_RED_KEY
    self.initializeSliders()
    
  def onHighRedValueTextBtn(self):
    self.currentDetectionParams=Settings.HIGH_RED_KEY
    self.initializeSliders()
  
  def updateUICurrentDetectionParamsState(self):
    if self.currentDetectionParams==Settings.LOW_RED_KEY:
      self.ui.lowRedValueTextBtn.setEnabled(False)
      self.ui.lowRedValueTextBtn.setStyleSheet('QPushButton {background-color: rgb(0, 170, 255); color: rgb(255, 255, 255);}')
      self.ui.highRedValueTextBtn.setEnabled(True)
      self.ui.highRedValueTextBtn.setStyleSheet('')
    else:
      self.ui.lowRedValueTextBtn.setEnabled(True)
      self.ui.lowRedValueTextBtn.setStyleSheet('')
      self.ui.highRedValueTextBtn.setEnabled(False)
      self.ui.highRedValueTextBtn.setStyleSheet('QPushButton {background-color: rgb(0, 170, 255); color: rgb(255, 255, 255);}')

  def onLowHChange(self):
    value=self.ui.lowHSlider.value()
    self.ui.lowHValueText.setText(str(value))
    self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY][0]=value
    self.imgProcessingThread.onLowHChange(value)

  def onHighHChange(self):
    value=self.ui.highHSlider.value()
    self.ui.highHValueText.setText(str(value))
    self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY][0]=value
    self.imgProcessingThread.onHighHChange(value)
    
  def onLowSChange(self):
    value=self.ui.lowSSlider.value()
    self.ui.lowSValueText.setText(str(value))
    self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY][1]=value
    self.imgProcessingThread.onLowSChange(value)
    
  def onHighSChange(self):
    value=self.ui.highSSlider.value()
    self.ui.highSValueText.setText(str(value))
    self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY][1]=value
    self.imgProcessingThread.onHighSChange(value)
    
  def onLowVChange(self):
    value=self.ui.lowVSlider.value()
    self.ui.lowVValueText.setText(str(value))
    self.settings.detectionParams[self.currentDetectionParams][Settings.LOW_HSV_KEY][2]=value
    self.imgProcessingThread.onLowVChange(value)
    
  def onHighVChange(self):
    value=self.ui.highVSlider.value()
    self.ui.highVValueText.setText(str(value))
    self.settings.detectionParams[self.currentDetectionParams][Settings.HIGH_HSV_KEY][2]=value
    self.imgProcessingThread.onHighVChange(value)

  def onMedianBlurScaleChange(self):
    value=self.ui.noiseReductionParamSlider.value()
    self.ui.noiseReductionParamValueText.setText(str(value))
    value=value if value%2>0 else value+1
    self.settings.detectionParams[self.currentDetectionParams][Settings.MEDIAN_BLUR_SCALE_KEY]=value
    self.imgProcessingThread.onMedianBlurScaleChange(value)
  
  def openImg(self):
    fileUri, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
    self.imgProcessingThread.useImg(fileUri)

  def onCloseClick(self):
    self.close()
