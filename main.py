import sys
from PySide2.QtWidgets import QApplication
from Views.MainViewController import View
import cv2
import numpy as np


def main():
    app = QApplication(sys.argv)
    mainWindow=View()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
