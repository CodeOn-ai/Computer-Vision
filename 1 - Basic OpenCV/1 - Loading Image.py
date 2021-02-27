# required libs 

import cv2 as cv

# -- load image -- #
img = cv.imread("resources/elliot.jpg")


# -- conver to grayscale --#
grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)


# -- display image --#
cv.imshow("Output",img)
# -- cv.imshow("Output gray",grayImg)
# -- 0 means it will remain open, any other number refers to milisec --#
cv.waitKey(5000) 
cv.destroyAllWindows()