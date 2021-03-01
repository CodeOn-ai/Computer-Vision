import cv2 as cv
import numpy as np

img = cv.imread("resources/orange.jpeg", cv.IMREAD_GRAYSCALE)

# creating the threshold
_, mask = cv.threshold(img, 250,255, cv.THRESH_BINARY_INV)

# creating a kernel, also known as filter
kernel= np.ones((5,5), np.uint8)
dilation = cv.dilate(mask, kernel)
erosion = cv.erode(mask, kernel)

cv.imshow("gray", img)
cv.imshow("mask", mask)
cv.imshow("dilation", dilation)
cv.imshow("erosion", erosion)

cv.waitKey(0)
cv.destroyAllWindows()