import os
import traceback
from datetime import datetime
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2
import numpy as np


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
    img=None
    imgRect=None
    imgUri=None

    stopped=True

    def run(self):
        if self.imgUri is None:
            print('[ERROR] Image URI is NONE')

        self.img=cv2.imread(self.imgUri)
        if self.img is None:
            print('[ERROR] Image not found')

        self.stopped=False

        while self.stopped is False:
            if self.isPause or self.isBreak:
                continue
            try:
                img, imgBin, imgBinEnhanced, contours = self.process()
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

    def changeMode(self, value):
        self.verboseMode = not self.verboseMode

    def pause(self):
        self.isPause = True

    def resume(self):
        self.isPause = False

    def startBreak(self):
        self.isBreak = True

    def endBreak(self):
        self.isBreak = False

    def stop(self):
        self.isActive = False
        self.quit()

    def screenshoot(self):
        self.saveFrame()

    def saveFrame(self):
        try:
            if self.currentFrame is None:
                return
            self.pause()
            now = datetime.now()
            filename=now.strftime("%d-%m-%y %H'%M'%S.jpg")
            print(os.path.join(self.screenshootDir, filename))
            cv2.imwrite(os.path.join(self.screenshootDir, filename), cv2.cvtColor(self.currentFrame, cv2.COLOR_RGB2BGR))
            self.resume()
        except Exception as e:
            print(traceback.format_exc())

    def detect(self, frame):
        roi=frame[
            int(self.cameraResHeight/4):int(self.cameraResHeight/4 + self.cameraResHeight/2), 
            int(self.cameraResWidth/4):int(self.cameraResWidth/4 + self.cameraResWidth/2), 
        ]
        hsvFrame=cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        masks=None
        for param in self.detectionParams:
            mask = cv2.inRange(hsvFrame, param[0], param[1])
            mask = cv2.medianBlur(mask, param[2])
            masks=(masks+mask) if masks is not None else mask
        # cv2.imshow('DETECTOR', filteredDetection)

        contours, _ = cv2.findContours(masks, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        selectedContour=None
        selectedContourArea=0
        for contour in contours:
            area = cv2.contourArea(contour)
            # print(area)
            if area > 5000:
                selectedContour=contour
                selectedContourArea=area
        filtered = cv2.bitwise_and(roi, roi, mask=masks)

        return roi, masks, filtered, selectedContour
    