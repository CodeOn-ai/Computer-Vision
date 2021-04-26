import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    
    
    cv.imshow("frame", frame)
    
    key = cv.waitKey(1)
    
    if key == ord("s"):
        # Select ROI
        r = cv.selectROI("frame",frame)
        
        imgCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        
        cv.imshow("Cropped", imgCrop)
        
        gray = cv.cvtColor(imgCrop, cv.COLOR_RGB2GRAY)
        
        cv.imshow("gray", gray)
        
        if key == 27:
            break
        
                
    elif key == 27:
        break
     
    
cap.release()
cv.destroyAllWindows()
    