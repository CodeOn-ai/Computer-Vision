import cv2 as cv
import datetime

cap = cv.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    font = cv.FONT_HERSHEY_SIMPLEX
    #txt = "This is a text I wanted to put in on"
    date = str(datetime.datetime.now())
    
    frame = cv.putText(frame, date, (10,50),
               font, 1, 
               (0, 0, 255), 
               2,
               cv.LINE_AA)
    
    key = cv.waitKey(1) 
    
    cv.imshow("frame", frame)
    
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()