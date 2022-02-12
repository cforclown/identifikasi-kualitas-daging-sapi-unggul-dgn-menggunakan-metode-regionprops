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

def on_low_H_thresh_trackbar(val):
    global lowHue
    global highHue
    lowHue = val
    lowHue = min(highHue-1, lowHue)
    cv2.setTrackbarPos(lowHueTrackbarName, detectionWindow, lowHue)
def on_high_H_thresh_trackbar(val):
    global lowHue
    global highHue
    highHue = val
    highHue = max(highHue, lowHue+1)
    cv2.setTrackbarPos(highHueTrackbarName, detectionWindow, highHue)
def on_low_S_thresh_trackbar(val):
    global lowSaturation
    global highSaturation
    lowSaturation = val
    lowSaturation = min(highSaturation-1, lowSaturation)
    cv2.setTrackbarPos(lowSaturationTrackbarName, detectionWindow, lowSaturation)
def on_high_S_thresh_trackbar(val):
    global lowSaturation
    global highSaturation
    highSaturation = val
    highSaturation = max(highSaturation, lowSaturation+1)
    cv2.setTrackbarPos(highSaturationTrackbarName, detectionWindow, highSaturation)
def on_low_V_thresh_trackbar(val):
    global lowValue
    global highValue
    lowValue = val
    lowValue = min(highValue-1, lowValue)
    cv2.setTrackbarPos(lowValueTrackbarName, detectionWindow, lowValue)
def on_high_V_thresh_trackbar(val):
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
cv2.createTrackbar(lowHueTrackbarName, detectionWindow , lowHue, maxHue, on_low_H_thresh_trackbar)
cv2.createTrackbar(highHueTrackbarName, detectionWindow , highHue, maxHue, on_high_H_thresh_trackbar)
cv2.createTrackbar(lowSaturationTrackbarName, detectionWindow , lowSaturation, maxValueNSaturation, on_low_S_thresh_trackbar)
cv2.createTrackbar(highSaturationTrackbarName, detectionWindow , highSaturation, maxValueNSaturation, on_high_S_thresh_trackbar)
cv2.createTrackbar(lowValueTrackbarName, detectionWindow , lowValue, maxValueNSaturation, on_low_V_thresh_trackbar)
cv2.createTrackbar(highValueTrackbarName, detectionWindow , highValue, maxValueNSaturation, on_high_V_thresh_trackbar)
cv2.namedWindow(enhancedDetectionWindow)
cv2.createTrackbar(enhancedScaleName, enhancedDetectionWindow , enhancedScale, 99, onEnhancedValueTrackbar)

meatTemplate=cv2.imread('./Resources/Templates/resource-1.jpg')
while True:
  frame_HSV = cv2.cvtColor(meatTemplate, cv2.COLOR_BGR2HSV)
  frameThreshold = cv2.inRange(meatTemplate, (lowHue, lowSaturation, lowValue), (highHue, highSaturation, highValue))
  enhancedThreshold = cv2.medianBlur(frameThreshold, enhancedScale)
  filteredDetection = cv2.bitwise_and(meatTemplate, meatTemplate, mask=enhancedThreshold)

  cv2.imshow(captureWindow, meatTemplate)
  cv2.imshow(detectionWindow, frameThreshold)
  cv2.imshow(enhancedDetectionWindow, enhancedThreshold)
  cv2.imshow('Filtered Detection', filteredDetection)

  key = cv2.waitKey(30)
  if key == ord('q') or key == 27:
      break
