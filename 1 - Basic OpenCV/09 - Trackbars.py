import cv2 as cv 


def nothing(x):
    pass

cap = cv.VideoCapture(0)
# Name the window to be used
cv.namedWindow("frame")

# Create the trackbar
cv.createTrackbar("test", "frame", 50, 500, nothing)

while True:
    _, frame = cap.read()
    
    #get the position of the video with trackbar
    test= cv.getTrackbarPos("test", "frame")
    
    #put a text in the video
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame, str(test), (50,150), font, 4, (0,0,255))
    
    cv.imshow("frame", frame)
    
    key = cv.waitKey(1)
    
    if key == 27:
        break 
    
    
cap.release()
cv.destroyAllWindows()