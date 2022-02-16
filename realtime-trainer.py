from __future__ import print_function
import cv2
import argparse

maxValueNSaturation = 255
maxHue = 360//2

lowHue = 50
highHue = 180

lowSaturation = 87
highSaturation = 255

lowValue = 170
highValue = 255

captureWindow = 'Video Capture'
detectionWindow = 'Detection'
lowHueTrackbarName = 'LOW H'
lowSaturationTrackbarName = 'LOW S'
lowValueTrackbarName = 'LOW V'
highHueTrackbarName = 'HIGH H'
highSaturationTrackbarName = 'HIGH S'
highValueTrackbarName = 'HIGH V'
enhancedDetectionWindow = 'Enhanced Detection'
enhancedScaleName = 'Enhanced Scale'
enhancedScale = 35

def lowHSlider(val):
    global lowHue
    global highHue
    lowHue = val
    lowHue = min(highHue-1, lowHue)
    cv2.setTrackbarPos(lowHueTrackbarName, detectionWindow, lowHue)
def highHSlider(val):
    global lowHue
    global highHue
    highHue = val
    highHue = max(highHue, lowHue+1)
    cv2.setTrackbarPos(highHueTrackbarName, detectionWindow, highHue)
def lowSSlider(val):
    global lowSaturation
    global highSaturation
    lowSaturation = val
    lowSaturation = min(highSaturation-1, lowSaturation)
    cv2.setTrackbarPos(lowSaturationTrackbarName, detectionWindow, lowSaturation)
def highSSlider(val):
    global lowSaturation
    global highSaturation
    highSaturation = val
    highSaturation = max(highSaturation, lowSaturation+1)
    cv2.setTrackbarPos(highSaturationTrackbarName, detectionWindow, highSaturation)
def lowVSlider(val):
    global lowValue
    global highValue
    lowValue = val
    lowValue = min(highValue-1, lowValue)
    cv2.setTrackbarPos(lowValueTrackbarName, detectionWindow, lowValue)
def highVSlider(val):
    global lowValue
    global highValue
    highValue = val
    highValue = max(highValue, lowValue+1)
    cv2.setTrackbarPos(highValueTrackbarName, detectionWindow, highValue)
def onEnhancedValueTrackbar(val):
    global enhancedScale
    enhancedScale = val if val%2>0 else val+1 
    print(val)
    cv2.setTrackbarPos(enhancedScaleName, enhancedDetectionWindow, enhancedScale)

parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv2.VideoCapture(args.camera)
cv2.namedWindow(captureWindow)
cv2.namedWindow(detectionWindow)
cv2.createTrackbar(lowHueTrackbarName, detectionWindow , lowHue, maxHue, lowHSlider)
cv2.createTrackbar(highHueTrackbarName, detectionWindow , highHue, maxHue, highHSlider)
cv2.createTrackbar(lowSaturationTrackbarName, detectionWindow , lowSaturation, maxValueNSaturation, lowSSlider)
cv2.createTrackbar(highSaturationTrackbarName, detectionWindow , highSaturation, maxValueNSaturation, highSSlider)
cv2.createTrackbar(lowValueTrackbarName, detectionWindow , lowValue, maxValueNSaturation, lowVSlider)
cv2.createTrackbar(highValueTrackbarName, detectionWindow , highValue, maxValueNSaturation, highVSlider)
cv2.namedWindow(enhancedDetectionWindow)
cv2.createTrackbar(enhancedScaleName, enhancedDetectionWindow , enhancedScale, 99, onEnhancedValueTrackbar)

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if capture.isOpened(): 
    # get vcap property 
    cameraResWidth  = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    cameraResHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(cameraResWidth, cameraResHeight)
    while True:
        ret, rawFrame = capture.read()
        if ret:
            frame_HSV = cv2.cvtColor(rawFrame, cv2.COLOR_BGR2HSV)
            frameThreshold = cv2.inRange(rawFrame, (lowHue, lowSaturation, lowValue), (highHue, highSaturation, highValue))
            enhancedThreshold = cv2.medianBlur(frameThreshold, enhancedScale)
            filteredDetection = cv2.bitwise_and(rawFrame, rawFrame, mask=enhancedThreshold)

            cv2.imshow(captureWindow, rawFrame)
            cv2.imshow(detectionWindow, frameThreshold)
            cv2.imshow(enhancedDetectionWindow, enhancedThreshold)
            cv2.imshow('Filtered Detection', filteredDetection)

        key = cv2.waitKey(30)
        if key == ord('q') or key == 27:
            break
else:
    print('[ERROR] FAILED TO ACCESS CAMERA!')
