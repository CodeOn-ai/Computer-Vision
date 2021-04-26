import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/highway.mp4")
_, first_frame = cap.read()
gfirst_frame = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)
gfirst_frame = cv.GaussianBlur(gfirst_frame, (5,5), 0)

while True:
    _, frame = cap.read()
    gframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gframe = cv.GaussianBlur(gframe, (5,5), 0)
    
    gframe = cv.resize(gframe, (500,500))
    gfirst_frame = cv.resize(gfirst_frame, (500,500))
    
    
    difference = cv.absdiff(first_frame, frame)
    difference = cv.resize(difference, (500,500))
    
    _, difference = cv.threshold(difference, 75,255, cv.THRESH_BINARY)
    
    
    cv.imshow("First Frame", gfirst_frame)
    cv.imshow("Frame", gframe)
    cv.imshow("Difference", difference)
    
    key = cv.waitKey(25)
    
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()