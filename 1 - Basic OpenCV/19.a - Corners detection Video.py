import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0)
cv.namedWindow("original")

def nothing():
    pass
cv.createTrackbar("quality", "original", 1, 100, nothing)


while True: 
    
    ret, frame = cap.read()
    
    gframe = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    # points, 
    
    quality = cv.getTrackbarPos("quality","original")
    quality = quality/100 if quality > 0 else 0.01
    
    
    corners = cv.goodFeaturesToTrack(gframe, 100, quality, 10)
    
    if corners is not None:
        corners =np.int0(corners)
        
        for corner in corners:
            x,y = corner.ravel()
            cv.circle(frame, (x,y), 3,(0,0,255), -1)
    

    cv.imshow("original", frame)
    #cv.imshow("gray", gframe)
    
    key = cv.waitKey(1)
    
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()