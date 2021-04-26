# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

# -- get from webcam image -- #
cap = cv.VideoCapture(0) 

# -- load a video -- #
cap = cv.VideoCapture("resources/Koenigsegg Jesko Absolut.mp4") 

# -- Videos are images per time, that images in loop creates the videos -- #
while True:
    ret, frame = cap.read() 
    grayFrame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    ret, threshold = cv.threshold(grayFrame, 128,255,cv.THRESH_BINARY)
    
    #cv.imshow("frame", frame)
    #cv.imshow("gray frame", grayFrame)
    cv.imshow("threshold", threshold)
    key = cv.waitKey(1)
    
    # -- break the loop - #
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()