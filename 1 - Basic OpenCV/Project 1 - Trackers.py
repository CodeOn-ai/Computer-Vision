import cv2 as cv

# add trackers into an dict
trackerDict = {"csrt": cv.TrackerCSRT_create,
           "kcf": cv.TrackerKCF_create,
           #"boosting": cv.TrackerBoosting_create,
           "mil": cv.TrackerMIL_create,  
           #"tld": cv.TrackerTLD_create,
           #"medianflow": cv.TrackerMedianFlow_create, 
           #"mosse": cv.TrackerMOSSE_create           
           }


#selected tracker
tracker = trackerDict["csrt"]()

# loading the video, in this case webcam
cap = cv.VideoCapture(0)

# get the first frame and initialize the tracker
ret, frame = cap.read(1000)
cv.imshow("Frame", frame)
bb = cv.selectROI("Frame", frame)
tracker.init(frame, bb)


while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret: # when the video ends break
        break
    
    #update the box on "frame"
    (sucess,box) = tracker.update(frame)
    
    if sucess:
        #draw the box
        (x,y,w,h) = [int(a) for a in box]
        cv.rectangle(frame, (x,y),(x+w,y+h), (255,0,0), 2)
    cv.imshow("Frame", frame)
    
    key = cv.waitKey(27)
    
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()
