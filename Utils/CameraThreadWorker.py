import os
from time import sleep
import traceback
from enum import Enum
from datetime import datetime
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2
import numpy as np

from Utils.CameraSettings import CAMERA_SETTINGS, getCameraCapture
from Utils.QualityThreadWorker import QualityThreadWorker
from Utils.SettingsManager import Settings



class MEATQUALITY(Enum):
    GOOD=1
    MEDIUM=0
    BAD=-1

class ROI:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

class CameraThreadWorker(QThread):
    frameUpdate=Signal(QImage)
    roiUpdate=Signal(QImage)
    roiMaskUpdate=Signal(QImage)
    filteredUpdate=Signal(QImage)
    meatDetected=Signal(bool)
    detectedQuality=Signal(tuple)
    qualityThread=QualityThreadWorker()

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.screenshootDir=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        
        self.verboseMode=False
        self.isActive=False
        self.isPause=True
        self.isBreak=False
        self.stopped=True

        self.currentFrame=None

        self.cameraPort=Settings().getCameraPort()
        self.cameraRes=Settings().getCameraResolution()
        self.detectionParams=Settings().getDetectionParams()
        print('=================== CAM THREAD ===================')
        print('cam-port        :', self.cameraPort)
        print('cam-resolution  :', self.cameraRes)
        print('detection-params:', self.detectionParams)
        print('==================================================')

        self.cameraResWidth=0
        self.cameraResHeight=0
        self.roi=None

    def run(self):
        print('[CAM THREAD] running')
        
        self.isActive=True
        self.isPause=False
        capture = getCameraCapture(self.cameraPort, self.cameraRes)
        if capture.isOpened(): 
            # get vcap property 
            self.cameraResWidth  = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.cameraResHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.roi=ROI(
                int(self.cameraResWidth/4), 
                int(self.cameraResHeight/4), 
                int(self.cameraResWidth/2), 
                int(self.cameraResHeight/2)
            )
        else:
            print('[ERROR] FAILED TO ACCESS CAMERA!')
            return

        while self.isActive:
            if self.isPause or self.isBreak:
                continue
            try:
                ret, rawFrame = capture.read()
                if ret:
                    roi, mask, filtered, contour, quality = self.detect(rawFrame)
                    cv2.rectangle(
                        rawFrame, 
                        (self.roi.x, self.roi.y), 
                        (self.roi.x+self.roi.w, self.roi.y+self.roi.h), 
                        (75, 75, 255), 
                        2
                    )
                    if contour is not None:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(
                            rawFrame, 
                            (self.roi.x+x, self.roi.y+y), 
                            (self.roi.x + x + w, self.roi.y + y + h), 
                            (75, 255, 75), 
                            2
                        )
                        self.meatDetected.emit(True)
                    else:
                        self.meatDetected.emit(False)

                    if self.qualityThread.result is not None:
                        self.detectedQuality.emit(self.qualityThread.getResult());

                    if not self.verboseMode:
                        frame = cv2.flip(cv2.cvtColor(rawFrame, cv2.COLOR_BGR2RGB), 1)
                        self.currentFrame=frame
                        frameQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                        self.frameUpdate.emit(frameQtFormat.scaled(self.cameraRes[0], self.cameraRes[1], Qt.KeepAspectRatio))
                    else:
                        frame = cv2.flip(cv2.cvtColor(rawFrame, cv2.COLOR_BGR2RGB), 1)
                        self.currentFrame=frame
                        frameQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

                        roi = np.asarray(roi)
                        roiFrame = cv2.flip(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB), 1)
                        roiFrameQtFormat = QImage(roiFrame.data, roiFrame.shape[1], roiFrame.shape[0], QImage.Format_RGB888)

                        mask = np.asarray(mask)
                        maskFrame = cv2.flip(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), 1)
                        maskFrameQtFormat = QImage(maskFrame.data, maskFrame.shape[1], maskFrame.shape[0], QImage.Format_RGB888)

                        rawFrame[
                            self.roi.y:self.roi.y+self.roi.h,
                            self.roi.x:self.roi.x+self.roi.w
                        ] = filtered
                        filtered = np.asarray(filtered)
                        filteredFrame = cv2.flip(cv2.cvtColor(rawFrame, cv2.COLOR_BGR2RGB), 1)
                        filteredFrameQtFormat = QImage(filteredFrame.data, filteredFrame.shape[1], filteredFrame.shape[0], QImage.Format_RGB888)


                        self.frameUpdate.emit(frameQtFormat.scaled(self.cameraRes[0], self.cameraRes[1], Qt.KeepAspectRatio))
                        self.roiUpdate.emit(roiFrameQtFormat.scaled(self.cameraRes[0], self.cameraRes[1], Qt.KeepAspectRatio))
                        self.roiMaskUpdate.emit(maskFrameQtFormat.scaled(self.cameraRes[0], self.cameraRes[1], Qt.KeepAspectRatio))
                        self.filteredUpdate.emit(filteredFrameQtFormat.scaled(self.cameraRes[0], self.cameraRes[1], Qt.KeepAspectRatio))
            except Exception as e:
                print(traceback.format_exc())
        capture.release()
        capture=None
        print('[CAM THREAD] stopped')

    def changeMode(self, value):
        self.verboseMode = True if value=='Verbose' else False

    def pause(self):
        self.isPause = True

    def resume(self):
        self.isPause = False

    def halt(self):
        self.isBreak = True

    def unhalt(self):
        self.isBreak = False

    def breakWork(self):
        self.isActive = False
        self.qualityThread.quit()
        self.qualityThread.wait()
        while self.qualityThread.isRunning():
          sleep(0.1)
        self.qualityThread=None

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
        for detectionParams in self.detectionParams:
            mask = cv2.inRange(hsvFrame, tuple(detectionParams[Settings.LOW_HSV_KEY]), tuple(detectionParams[Settings.HIGH_HSV_KEY]))
            if detectionParams[Settings.BLUR_TYPE_KEY]==Settings.BLUR_TYPE_MEDIAN_BLUR:
                mask = cv2.medianBlur(mask, detectionParams[Settings.MEDIAN_BLUR_SCALE_KEY])
            else:
                mask = cv2.GaussianBlur(mask, tuple([detectionParams[Settings.GAUSSIAN_BLUR_SCALE_KEY], detectionParams[Settings.GAUSSIAN_BLUR_SCALE_KEY]]))
            masks=masks+mask if masks is not None else mask

        contours, _ = cv2.findContours(masks, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        selectedContour=None
        for contour in contours:
            area = cv2.contourArea(contour)
            # print(area)
            if area > 5000:
                selectedContour=contour
        filtered = cv2.bitwise_and(roi, roi, mask=masks)
        
        freshness=0
        quality=0
        if selectedContour is not None and self.qualityThread.processing is False and self.qualityThread.result is None:
            self.qualityThread.init(selectedContour, filtered)
            self.qualityThread.start();

        return roi, masks, filtered, selectedContour, (freshness, quality)
