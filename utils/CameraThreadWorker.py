from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QImage
import cv2


class CameraThreadWorker(QThread):
    imageUpdate = Signal(QImage)

    def run(self):
        self.ThreadActive = True
        capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flippedImage = cv2.flip(image, 1)
                convertToQtFormat = QImage(
                    flippedImage.data,
                    flippedImage.shape[1],
                    flippedImage.shape[0],
                    QImage.Format_RGB888,
                )
                pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.imageUpdate.emit(pic)

    def pause(self):
        self.ThreadActive = False
        self.pause()

    def resume(self):
        self.run()
        
    def stop(self):
        self.ThreadActive = False
        self.quit()
