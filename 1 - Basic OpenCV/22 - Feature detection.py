import cv2 as cv
import numpy as np

img = cv.imread("resources/Jesko3.jpg", cv.IMREAD_GRAYSCALE)


# sift, surf and orb are feature detection algorithms
sift = cv.xfeatures2d.SIFT_create()
#surf = cv.xfeatures2d.SURF_create()
#orb = cv.ORB_create()
# check the keypoints
#kp = sift.detect(img, None)

#imgKeyPoints = cv.drawKeypoints(img, kp, None) #only detect keypoints 

# detect keypoints and description of the points 
keypoints, descriptors = sift.detectAndCompute(img, None)

# draw the kp in the image 
img2 = cv.drawKeypoints(img, keypoints, None)

cv.imshow("img", img)
cv.imshow("img2", img2)
cv.waitKey(0)
cv.destroyAllWindows()