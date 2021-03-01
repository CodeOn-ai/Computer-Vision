import cv2 as cv
import numpy as np



img = cv.imread("resources/elliot.jpg")
rows, cols, ch = img.shape # returns height, width and color channels

# height is the sum of rows, 
# width is the sum of cols 
shape = (rows, cols)

matrix = np.float32([[1,0,50],[0,1,50]])

# translate moves the image within the shape
translated_img = cv.warpAffine(img, matrix, shape)

# scale image fx1 and fy scale the image proportionally
## double the size is 2 
scaledImg = cv.resize(img, None, fx=2, fy=2)


# image rotatioin 
matrix_r = cv.getRotationMatrix2D((cols/2,rows/2), 90, 1)
rotatedImg = cv.warpAffine(img, matrix_r,shape)


cv.imshow("img", img)
#cv.imshow("scaledImg", scaledImg)
cv.imshow("translated_img", translated_img)
cv.imshow("rotatedImg", rotatedImg)

cv.waitKey(0)
cv.destroyAllWindows()