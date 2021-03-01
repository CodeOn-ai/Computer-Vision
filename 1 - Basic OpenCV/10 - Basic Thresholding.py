import cv2 as cv 
import numpy as np

img = cv.imread("resources/red_panda.jpg")

imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# Replace the values with 1 or 0 according to their proximity

_, threshold_binary = cv.threshold(imgGray, 128, 255, cv.THRESH_BINARY)
_, threshold_trunc = cv.threshold(imgGray, 128, 255, cv.THRESH_TRUNC)
_, threshold_tozero = cv.threshold(imgGray, 128, 255, cv.THRESH_TOZERO)


cv.imshow("Black&White", imgGray)
cv.imshow("threshold_binary", threshold_binary)
cv.imshow("threshold_trunc", threshold_trunc)
cv.imshow("threshold_tozero", threshold_tozero)
cv.waitKey(20000)
cv.destroyAllWindows()

