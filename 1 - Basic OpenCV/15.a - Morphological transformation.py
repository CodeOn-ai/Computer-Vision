import cv2 as cv 
import numpy as np

#required to pass the function to create the trackbar
def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow("Trackbars")

# create trackbar HSV colour channels 
## min range values 
cv.createTrackbar("Min - H", "Trackbars", 0, 179, nothing)
cv.createTrackbar("Min - S", "Trackbars", 0, 255, nothing)
cv.createTrackbar("Min - V", "Trackbars", 0, 255, nothing)

## max range values 
cv.createTrackbar("Max - H", "Trackbars", 179, 179, nothing)
cv.createTrackbar("Max - S", "Trackbars", 255, 255, nothing)
cv.createTrackbar("Max - V", "Trackbars", 255, 255, nothing)

while True:
    _, frame = cap.read()
    
    # convert to hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    
    
    # Get the position of the trackbars
    minH = cv.getTrackbarPos("Min - H",  "Trackbars")
    minS = cv.getTrackbarPos("Min - S",  "Trackbars")
    minV = cv.getTrackbarPos("Min - V",  "Trackbars")
    
    maxH = cv.getTrackbarPos("Max - H",  "Trackbars")
    maxS = cv.getTrackbarPos("Max - S",  "Trackbars")
    maxV = cv.getTrackbarPos("Max - V",  "Trackbars")
    
    # create a range of colour 
    min_blue = np.array([minH,minS,minV])
    max_blue = np.array([maxH,maxS,maxV])
    ## create the mask 
    mask = cv.inRange(hsv, min_blue, max_blue)
    
    # kernel and erosion 
    kernel = np.ones((5,5), np.uint8)
    erosion = cv.erode(mask, kernel)
    
    # dilation 
    dilation = cv.dilate(mask, kernel)
    
    # erosion then dilation
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=2)
    # dilation then erosion
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    
    
    #bitwise to get combine 
    result = cv.bitwise_and(frame, frame, mask = mask)
        
    #cv.imshow("frame", frame)
    
    #cv.imshow("hsv",hsv)
    cv.imshow("Trackbars", mask)
    #cv.imshow("erosion", erosion)
    #cv.imshow("dilation", dilation)
    cv.imshow("opening", opening)
    cv.imshow("closing", closing)
    cv.imshow("result", result)
    
    key = cv.waitKey(1)
    
    if key == 27:
        break 
    
    
cap.release()
cv.destroyAllWindows()