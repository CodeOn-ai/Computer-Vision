import cv2 as cv
import numpy as np



img = cv.imread("resources/orange.jpeg", cv.IMREAD_GRAYSCALE)
img = cv.GaussianBlur(img, (5,5), 0)

# sobelx
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
# sobely
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)

laplacian = cv.Laplacian(img, cv.CV_64F, ksize= 5)

canny = cv.Canny(img,100,150)

cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("laplacian", laplacian)
cv.imshow("canny", canny)

cv.waitKey()
cv.destroyAllWindows()