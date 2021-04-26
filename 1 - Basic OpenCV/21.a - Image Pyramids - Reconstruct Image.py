import cv2 as cv 
import numpy as np

img= cv.imread("resources/Jesko3.jpg")


# Gaussian Pyramid 
layer = img.copy()
gaussian_pyramid = [layer]
length = 6

for i in range(length):
    layer = cv.pyrDown(layer)
    gaussian_pyramid.append(layer)
    #cv.imshow("Layer {}".format(i), gaussian_pyramid[i])

layer = gaussian_pyramid[length]
laplacian_pyramid = [layer]

for i in range(length, 0, -1):

    gaussian_expanded = cv.pyrUp(gaussian_pyramid[i]) 
    laplacian = cv.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)
    #cv.imshow("Laplacian {}".format(i), laplacian)

reconstructed_img = laplacian_pyramid[0]
for i in range(1, length):

    reconstructed_img = cv.pyrUp(reconstructed_img) # dstsize=size)
    reconstructed_img = cv.add(reconstructed_img, laplacian_pyramid[i])
    cv.imshow(str(i),reconstructed_img )

cv.waitKey(0)
cv.destroyAllWindows()