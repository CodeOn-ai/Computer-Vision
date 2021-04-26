import cv2 as cv
import numpy as np


# load image
img = cv.imread("resources/red_panda.jpg")

# Select ROI
r = cv.selectROI(img)

#Crop img
imgCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

#Display cropped img
cv.imshow("cropped img", imgCrop)
cv.waitKey(0)
cv.destroyAllWindows()
