import os
import traceback
import time
from datetime import datetime
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2


class CameraThreadWorker(QThread):
    imageUpdate=Signal(QImage)
    screenshootDir=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    
    isActive=False
    isPause=True
    currentFrame=None

    def run(self):
        self.isActive=True
        self.isPause=False
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.isActive:
            if self.isPause:
                continue
            try:
                ret, frame = capture.read()
                if ret:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flippedImage = cv2.flip(image, 1)
                    self.currentFrame=image
                    convertToQtFormat = QImage(
                        flippedImage.data,
                        flippedImage.shape[1],
                        flippedImage.shape[0],
                        QImage.Format_RGB888,
                    )
                    pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.imageUpdate.emit(pic)
            except Exception as e:
                print(traceback.format_exc())

    def pause(self):
        self.isPause = True

    def resume(self):
        self.isPause = False
        
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
