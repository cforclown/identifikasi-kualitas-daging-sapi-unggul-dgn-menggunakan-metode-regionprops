import os
import traceback
from enum import Enum
from datetime import datetime
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2
import numpy as np

from Utils.CameraSettings import CAMERA_SETTINGS, getCameraCapture
from Utils.SettingsManager import Settings



class MEATQUALITY(Enum):
    GOOD=1
    MEDIUM=0
    BAD=-1

class QualityThreadWorker(QThread):
    processing=False;
    result=0, 0;

    def __init__(self, parent=None):
        super().__init__(parent)

    def init(self, contour, filteredFrame):
        self.contour=contour
        self.filteredFrame=filteredFrame

    def run(self):
        self.processing=True
        self.result=self.checkQuality(self.contour, self.filteredFrame);
        self.processing=False

    def checkQuality(self, contour, filteredFrame):
        x, y, w, h = cv2.boundingRect(contour)
        hsvFrame=cv2.cvtColor(filteredFrame, cv2.COLOR_BGR2HSV)
        roi=hsvFrame[y:h, x:w]
        
        sTotal=0
        vTotal=0
        pixelCount=0
        for y in range(0, roi.shape[1]):
            for x in range(0, roi.shape[0]):
                pixel=roi[x, y]
                pixelS=pixel[1]
                pixelV=pixel[0]
                if pixel is not None and pixelS!=0 and pixelV!=0:
                    # print(pixel)
                    pixelCount=pixelCount+1
                    sTotal=sTotal+pixelS
                    vTotal=vTotal+pixelV
        if pixelCount is not 0:
            return sTotal/pixelCount/255*100, vTotal/pixelCount/255*100
        else:
            return None

    def getResult(self):
      if self.result is None:
        return None
      value = self.result
      self.result=None
      return value
