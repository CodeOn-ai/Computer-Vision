import cv2 as cv 
import numpy as np


img = cv.imread("resources/1800s.jpg")

avr = cv.blur(img, (5,5))
gaussion = cv.GaussianBlur(img, (5,5), 0)
median = cv.medianBlur(img, 5)

cv.imshow("img", img)
cv.imshow("avr", avr)
cv.imshow("gaussion", gaussion)
cv.imshow("median", median)


cv.waitKey(0)
cv.destroyAllWindows()