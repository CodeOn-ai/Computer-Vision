import cv2 as cv
import numpy as np 

video = cv.VideoCapture("resources/car.mp4")



while True:
    ret, frame = video.read()
    
    # resizing video frame
    frame = cv.resize(frame,(600,600))
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    #Values to capture the color white    
    minB = np.array([0,0,168]) 
    maxB = np.array([172,111,255]) 
    mask = cv.inRange(hsv,minB,maxB)
    edges = cv.Canny(mask, 75,150)
    
    lines = cv.HoughLinesP(edges, 1,
                           np.pi/180,
                           50, 
                           maxLineGap=50)
    
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            
            cv.line(frame, (x1,y1),(x2,y2),(0,255,0), 5)
            
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("hsv", hsv)
    
    key = cv.waitKey(1)
    if key == 27:
        break
    
video.release()
cv.destroyAllWindows()