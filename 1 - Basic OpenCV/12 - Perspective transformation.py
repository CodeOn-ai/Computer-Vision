import cv2 as cv 
import numpy as np


cap = cv.VideoCapture(0)


while True: 
    _, frame = cap.read()
    
    # frame, (cols(sum of cols = width)), rows(sum of rows = height))
    cv.circle(frame, (155,120), 5, (0,255,0), -1)
    cv.circle(frame, (480,120), 5, (0,255,0), -1)
    cv.circle(frame, (20,475), 5, (0,255,0), -1)
    cv.circle(frame, (620,475), 5, (0,255,0), -1)
    
    
    # gathering all the poings 
    pts1 = np.float32([[155,120],[480,120],[20,475],[620,475]])
    # points for a new image
    pts2 = np.float32([[0,0],[400,0],[0,600],[400,600]])
    # matrix to the points 
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    
    result = cv.warpPerspective(frame, matrix, (400,600))
    
    cv.imshow("Frame", frame)
    cv.imshow("result", result)
    key = cv.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()