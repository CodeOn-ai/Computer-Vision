import cv2 as cv 
import numpy as np

img= cv.imread("resources/Jesko3.jpg")


"""
MANUAL PYRAMID 

# downsizing by half the original image
layerOne = cv.pyrDown(img)
# downsizing by half the layerOne image
layerTwo = cv.pyrDown(layerOne)

# to upsize the image to previous one 
layerThree = cv.pyrUp(layerTwo)



cv.imshow("original image",img)
cv.imshow("pyramid down", layerOne)
cv.imshow("pyramid downx2", layerTwo)
# since we lost information when we downsize the image got blurred
cv.imshow("pyramid up", layerThree)

"""
# Gaussian Pyramid 
layer = img.copy()
gaussian_pyramid = [layer]
length = 3

for i in range(length):
    layer = cv.pyrDown(layer)
    #we will store the new images into a array
    gaussian_pyramid.append(layer)
    # display the images
    #cv.imshow("Layer {}".format(i), gaussian_pyramid[i])

# Laplacian used to edge detection 
# we will grab the smallest value stored in the array we just did
layer = gaussian_pyramid[length]
laplacian_pyramid = [layer]

for i in range(length, 0, -1):# goes backward in the iteration
    # it will pick the smallest one which is the highest index and expand it
    gaussian_expanded = cv.pyrUp(gaussian_pyramid[i]) 
    # it will subtract the the values to get the laplacia
    laplacian = cv.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    # it will store the image into the laplacian_pyramid array´
    laplacian_pyramid.append(laplacian)
    
    cv.imshow("Laplacian {}".format(i), laplacian)
    


cv.waitKey(0)
cv.destroyAllWindows()