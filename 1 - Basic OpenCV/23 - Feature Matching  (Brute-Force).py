import cv2 as cv 
import numpy as np 

img1 = cv.imread("resources/me1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("resources/me2.jpg", cv.IMREAD_GRAYSCALE)


# Create the detector 
sift = cv.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2  , None)


# Brute Force Matching 
bf = cv.BFMatcher(cv.NORM_L1, crossCheck=True)

matches = bf.match(des1,des2) # check the matches 

matches = sorted(matches, key = lambda x:x.distance)

matching_results = cv.drawMatches(img1,kp1, img2, kp2,matches[:20],None, flags=2)


cv.imshow("me1", img1)
cv.imshow("me2", img2)
cv.imshow("matching_results", matching_results)
cv.waitKey(0)
cv.destroyAllWindows()