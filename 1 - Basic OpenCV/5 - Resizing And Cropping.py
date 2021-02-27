import cv2 as cv 
import numpy as np

img = cv.imread("img.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# RESIZING

'''
# image shape (coloful ones have 3 dimensions)
print(img.shape)
print(imgGray.shape)

h,_,_ = img.shape
_,w,_ = img.shape

print("Height: {} and Width: {}".format(h,w))

halfH = int(h/2)
halfW = int(w/2)

halfImg = cv.resize(img,(halfH,halfW))

cv.imshow("Output",halfImg)

'''

# CROPPING

imgCropped = img[0:200,200:500]
cv.imshow("Output",imgCropped)


cv.waitKey(0)