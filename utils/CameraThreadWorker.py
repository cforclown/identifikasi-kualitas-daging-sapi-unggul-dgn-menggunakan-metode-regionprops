import os
import traceback
from datetime import datetime
from xml.dom.minidom import TypeInfo
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2
import numpy as np


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
    screenshootDir=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    
    verboseMode=False
    isActive=False
    isPause=True
    isBreak=False
    currentFrame=None
    detectionParams=[
        [
            np.array([18, 26, 147]),
            np.array([100, 120, 255]),
            35
        ],
        [
            np.array([50, 87, 170]),
            np.array([180, 255, 255]),
            35
        ]
    ]
    cameraResWidth=0
    cameraResHeight=0
    roi=None

    def run(self):
        self.isActive=True
        self.isPause=False
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if capture.isOpened(): 
            # get vcap property 
            self.cameraResWidth  = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.cameraResHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print(self.cameraResWidth, self.cameraResHeight)
            self.roi=ROI(int(self.cameraResWidth/4), int(self.cameraResHeight/4), int(self.cameraResWidth/2), int(self.cameraResHeight/2))
            print(self.roi.x, self.roi.y, self.roi.w, self.roi.h)
        else:
            print('[ERROR] FAILED TO ACCESS CAMERA!')
            return

        while self.isActive:
            if self.isPause or self.isBreak:
                continue
            try:
                ret, rawFrame = capture.read()
                if ret:
                    roi, mask, filtered, contour = self.detect(rawFrame)
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
                    if not self.verboseMode:
                        # filtered = np.asarray(filtered)
                        # rawFrame[ 
                        #     self.roi.y:self.roi.y+self.roi.h, 
                        #     self.roi.x:self.roi.x+self.roi.w
                        # ] = filtered
                        frame = cv2.flip(cv2.cvtColor(rawFrame, cv2.COLOR_BGR2RGB), 1)
                        self.currentFrame=frame
                        frameQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                        self.frameUpdate.emit(frameQtFormat.scaled(640, 480, Qt.KeepAspectRatio))
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


                        self.frameUpdate.emit(frameQtFormat.scaled(640, 480, Qt.KeepAspectRatio))
                        self.roiUpdate.emit(roiFrameQtFormat.scaled(640, 480, Qt.KeepAspectRatio))
                        self.roiMaskUpdate.emit(maskFrameQtFormat.scaled(640, 480, Qt.KeepAspectRatio))
                        self.filteredUpdate.emit(filteredFrameQtFormat.scaled(640, 480, Qt.KeepAspectRatio))
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
    