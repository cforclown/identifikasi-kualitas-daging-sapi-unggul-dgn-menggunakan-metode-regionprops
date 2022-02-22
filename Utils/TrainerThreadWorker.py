import os
import traceback
from datetime import datetime
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2
import numpy as np
from Utils.CameraSettings import getCameraCapture

from Utils.SettingsManager import Settings


class ImageRect:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

class TrainerThreadWorker(QThread):
    imgUpdate=Signal(QImage)
    imgBinUpdate=Signal(QImage)
    imgBinEnhancedUpdate=Signal(QImage)

    imgUri=None
    img=None
    imgRect=None

    stopped=True
    cameraPort=Settings().getCameraPort()
    cameraRes=Settings().getCameraResolution()
    detectionParams=Settings().getDetectionParams()
    capture=None

    def init(self, currentDectectionParams):
        self.currentDectectionParams=currentDectectionParams

    def run(self):
        self.stopped=False

        while self.stopped is False:
            try:
                ret, raw=self.getCurrentImg()
                if ret:
                    img, imgBin, imgBinEnhanced, contours = self.process(raw)
                    for contour in contours:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(
                            img, 
                            (x, y), 
                            (x+w, y+h), 
                            (75, 255, 75), 
                            2
                        )
                    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
                    imgQtFormat = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)

                    imgBin = np.asarray(imgBin)
                    imgBin = cv2.flip(cv2.cvtColor(imgBin, cv2.COLOR_BGR2RGB), 1)
                    imgBinQtFormat = QImage(imgBin.data, imgBin.shape[1], imgBin.shape[0], QImage.Format_RGB888)

                    imgBinEnhanced = np.asarray(imgBinEnhanced)
                    imgBinEnhanced = cv2.flip(cv2.cvtColor(imgBinEnhanced, cv2.COLOR_BGR2RGB), 1)
                    imgBinEnhancedQtFormat = QImage(imgBinEnhanced.data, imgBinEnhanced.shape[1], imgBinEnhanced.shape[0], QImage.Format_RGB888)

                    self.imgUpdate.emit(imgQtFormat.scaled(900, 600, Qt.KeepAspectRatio))
                    self.imgBinUpdate.emit(imgBinQtFormat.scaled(900, 600, Qt.KeepAspectRatio))
                    self.imgBinEnhancedUpdate.emit(imgBinEnhancedQtFormat.scaled(900, 600, Qt.KeepAspectRatio))
            except Exception as e:
                print(traceback.format_exc())
        self.capture.release()
        self.capture=None
        print('[THREAD] TRAINER worker ended')

    def breakWork(self):
        self.stopped = True
        if self.capture is not None:
            self.capture.release()

    def useCamera(self):
        self.img=None
    
    def useImg(self, imgUri):
        self.imgUri=imgUri
        self.img=cv2.imread(imgUri)

    def getCurrentImg(self):
        if self.img is not None:
            return True, self.img.copy()
        else:
            if self.capture is None:
                self.capture = getCameraCapture(self.cameraPort, self.cameraRes)
                if self.capture.isOpened(): 
                    print('CAM INITIALIZED', self.cameraPort)
                else:
                    print('[ERROR] FAILED TO ACCESS CAMERA!')
            return self.capture.read()

    def process(self, img):
        hsvFrame=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        imgBin=cv2.inRange(
            hsvFrame, 
            tuple(self.detectionParams[self.currentDectectionParams][Settings.LOW_HSV_KEY]), 
            tuple(self.detectionParams[self.currentDectectionParams][Settings.HIGH_HSV_KEY])
        )
        imgBin=cv2.medianBlur(
            imgBin, 
            self.detectionParams[self.currentDectectionParams][Settings.MEDIAN_BLUR_SCALE_KEY]
        )
        # cv2.imshow('DETECTOR', filteredDetection)

        contours, _ = cv2.findContours(imgBin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours=[]
        for contour in contours:
            area = cv2.contourArea(contour)
            # print(area)
            if area > 2500:
                contours.append(contour)
        imgBinEnhanced = cv2.bitwise_and(img, img, mask=imgBin)

        return img, imgBin, imgBinEnhanced, contours
    
    def onLowHChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.LOW_HSV_KEY][0]=value

    def onHighHChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.HIGH_HSV_KEY][0]=value
        
    def onLowSChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.LOW_HSV_KEY][1]=value
        
    def onHighSChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.HIGH_HSV_KEY][1]=value
        
    def onLowVChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.LOW_HSV_KEY][2]=value
        
    def onHighVChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.HIGH_HSV_KEY][2]=value

    def onMedianBlurScaleChange(self, value):
        self.detectionParams[self.currentDectectionParams][Settings.MEDIAN_BLUR_SCALE_KEY]=value
