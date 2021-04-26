import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/highway.mp4")

#subtractor = cv.createBackgroundSubtractorMOG2(history = 20, varThreshold = 25, detectShadows=False)

subtractor = cv.createBackgroundSubtractorKNN(history=20, detectShadows=False)


while True:
    _, frame = cap.read()
    frame = cv.GaussianBlur(frame, (5,5), 0)
    frame = cv.resize(frame, (600, 600))
    
    mask = subtractor.apply(frame)
    mask = cv.resize(mask, (600, 600))
    
    result = cv.bitwise_and(frame, frame, mask = mask)

    
   
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("result", result)
    key = cv.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()