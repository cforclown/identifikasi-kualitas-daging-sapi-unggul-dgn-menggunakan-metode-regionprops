from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QCloseEvent
from PySide2.QtCore import Qt
from Utils.CameraSettings import getAllCameraPorts
from Utils.SettingsManager import CameraResolutions, Settings
from Views.SettingsView import Ui_SettingsView
from Views.TrainerViewController import View as TrainerView


class View(QMainWindow):
  lastWindowEvent=None

  def __init__(self, onCloseCallback=None):
    super().__init__()
    self.ui = Ui_SettingsView()
    self.ui.setupUi(self)
    self.onCloseCallback=onCloseCallback
    self.setAcceptDrops(True)

    if onCloseCallback is not None:
      self.setWindowModality(Qt.WindowModal)
    
    self.settings=Settings().getJSON()
    self.initialize()

    self.show()

  def initialize(self):
    self.ui.saveBtn.clicked.connect(self.onSaveSettingsClick)
    self.ui.closeBtn.clicked.connect(self.onCloseClick)

    _, workingPorts, _=getAllCameraPorts()
    for port in workingPorts:
      self.ui.cameraPortCb.addItems(str(port))
    self.ui.cameraPortCb.currentTextChanged.connect(self.onCameraPortChange)
    self.ui.cameraPortCb.setCurrentText(str(self.settings[Settings.CAMERA_PORT_KEY]))

    for resName, resValue in CameraResolutions.VALUES.items():
      self.ui.cameraResCb.addItem(resName)
      if resValue==self.settings[Settings.CAMERA_RES_KEY]:
        self.ui.cameraResCb.setCurrentText(resName)
    self.ui.cameraResCb.currentTextChanged.connect(self.onCameraResChange)

    self.ui.medianBlurParamValueText.setText(str(self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.MEDIAN_BLUR_SCALE_KEY]))
    self.ui.lowRedValueText.setText(
      'LOW RED [{0}, {1}, {2}] [{3}, {4}, {5}]'.format(
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.LOW_HSV_KEY][0],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.LOW_HSV_KEY][1],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.LOW_HSV_KEY][2],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.HIGH_HSV_KEY][0],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.HIGH_HSV_KEY][1],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.LOW_RED_KEY][Settings.HIGH_HSV_KEY][2]
      )
    )
    self.ui.highRedValueText.setText(
      'HIGH RED [{0}, {1}, {2}] [{3}, {4}, {5}]'.format(
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.HIGH_RED_KEY][Settings.LOW_HSV_KEY][0],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.HIGH_RED_KEY][Settings.LOW_HSV_KEY][1],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.HIGH_RED_KEY][Settings.LOW_HSV_KEY][2],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.HIGH_RED_KEY][Settings.HIGH_HSV_KEY][0],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.HIGH_RED_KEY][Settings.HIGH_HSV_KEY][1],
        self.settings[Settings.DETECTION_PARAMS_KEY][Settings.HIGH_RED_KEY][Settings.HIGH_HSV_KEY][2]
      )
    )

    self.ui.changeDetectionParamsBtn.clicked.connect(self.onChangeDetectionParamsClick)

  def closeEvent(self, event: QCloseEvent) -> None:
    if self.onCloseCallback is not None:
      self.onCloseCallback()

  def onCloseClick(self):
    self.close()

  def onSaveSettingsClick(self):
    self.settings=Settings().save(self.settings).toJSON()

  def onCameraPortChange(self, value):
    self.settings[Settings.CAMERA_PORT_KEY]=int(value)
  
  def onCameraResChange(self, value):
    self.settings[Settings.CAMERA_RES_KEY]=CameraResolutions.VALUES[value]
  
  def onBlurTypeChange(self):
    print('coming soon')

  def onChangeDetectionParamsClick(self):
    self.trainerView=TrainerView(self.onTrainerClosed)
    self.ui.centralwidget.setEnabled(False)

  def onTrainerClosed(self):
    self.trainerView.close()
    self.trainerView.destroy()
    self.trainerView=None
    self.settings=Settings().getJSON()
    self.initialize()
    self.ui.centralwidget.setEnabled(True)
