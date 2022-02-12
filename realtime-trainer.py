import cv2
import numpy as np


def main():
    goodLowerHSV=np.array([10,0,108])
    goodHighHSV=np.array([160,255,255])
    badLowerHSV=np.array([170,50,50])
    badHighHSV=np.array([180,255,255])
    cameraResWidth=0
    cameraResHeight=0
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if capture.isOpened(): 
        # get vcap property 
        cameraResWidth  = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        cameraResHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(cameraResWidth)
        print(cameraResHeight)
    else:
        print('[ERROR] FAILED TO ACCESS CAMERA!')
        return

    while True:
        ret, frame = capture.read()
        if ret:
            regionOfInterest=frame[
                int(cameraResHeight/4):int(cameraResHeight/4 + cameraResHeight/2), 
                int(cameraResWidth/4):int(cameraResWidth/4 + cameraResWidth/2), 
            ]
            print(regionOfInterest.shape[:2])
            cv2.rectangle(
                frame, 
                (int(cameraResWidth/4), int(cameraResHeight/4)), 
                (int(cameraResWidth/4 + cameraResWidth/2), int(cameraResHeight/4 + cameraResHeight/2)), 
                (0, 255, 0), 
                3
            )
            hsvFrame=cv2.cvtColor(regionOfInterest, cv2.COLOR_BGR2HSV)
            mask1=cv2.inRange(hsvFrame, lowUpperRed, highUpperRed)
            mask2=cv2.inRange(hsvFrame, lowLowerRed, highLowerRed)
            mask=mask1+mask2
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 100:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            cv2.imshow("Frame", frame)
            cv2.imshow("regionOfInterest", regionOfInterest)
            cv2.imshow("Mask", mask)

        key = cv2.waitKey(30)
        if key == 27:
            break
        
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
