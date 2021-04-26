import cv2 as cv 

#function to the mouse 
def mouseDrawing(event, x, y, flags, params):
    '''
    if event == cv.EVENT_LBUTTONDOWN:
        print("Left Clicked")
        print(x,y)
    elif event == cv.EVENT_LBUTTONUP:
        print("Left released")
        print(x,y)
    '''
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("Left Double Clicked")
        markers.append((x, y))
    
cap = cv.VideoCapture(0)

# name of the window the event will happen
cv.namedWindow("toEvent")

# Relate the event window with drawing fuction
cv.setMouseCallback("toEvent", mouseDrawing)

# used to store the events, since the frames are updated constantly 
markers = []

while True:
    _, frame = cap.read()
    
    
    for center in markers:
        #print(center)
        #to show the circles we use it to constantly show the values stored 
        cv.circle(frame, center, 5, (0,255,0), -1)
    
    cv.imshow("Frame", frame)
    cv.imshow("toEvent", frame)
    
    key = cv.waitKey(1)
    
    if key == 27:
        break
    elif key == ord("d"):
        markers = []
    
cap.release()
cv.destroyAllWindows()