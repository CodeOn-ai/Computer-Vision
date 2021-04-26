import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # detect the color blue
    lower_blue = np.array([37, 150, 139])
    upper_blue = np.array([121, 255, 255])
    # display only the blue 
    mask = cv.inRange(hsv, lower_blue,upper_blue)
    
    # creating the contours
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw contours on the frames 
    #cv.drawContours(frame, contours,-1, (0,0,255),3)
    # Note: to improve and remove the noises on the image blur before convert to hsv
    
    
    # Display contour accoding to the area of the mask 
    for contour in contours:
        area = cv.contourArea(contour)
        
        if area > 5000:
            cv.drawContours(frame, contours,-1, (0,0,255),3)
    
    cv.imshow("Frame", frame)
    #cv.imshow("hsv", hsv)
    cv.imshow("mask", mask)
    
    key = cv.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()