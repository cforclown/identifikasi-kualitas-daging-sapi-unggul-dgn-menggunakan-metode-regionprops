# TESTING SCRIPT
import sys
from PySide2.QtWidgets import QApplication
from Views.MainViewController import View
import cv2


def checkQuality(self, contour, filteredFrame):
    x, y, w, h = cv2.boundingRect(contour)
    roi=filteredFrame[y:h, x:w]
    # convert to HSV
    for y in range(0, roi.shape[1]):
        for x in range(0, roi.shape[0]):
            pixel=roi[x, y]
            if pixel!=None and pixel[0]!=0:
                print(pixel)

def coodsMouseDisp(event, x, y, flags, param):
    # left mouse double click 
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if  img is not None and hsv is not None:
            print("Orginal BGR: ", img[x, y][0])
            print("HSV values: ", hsv[x, y])

def main():
    global img
    global hsv
    img=cv2.imread('./Resources/Templates/template-1.jpg')
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    while True:
        cv2.imshow("Original", img)
        cv2.imshow("HSV", hsv)
        #left mouse click event
        cv2.setMouseCallback("HSV", coodsMouseDisp)
        cv2.setMouseCallback("Original", coodsMouseDisp)

        if cv2.waitKey(1) &0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()
