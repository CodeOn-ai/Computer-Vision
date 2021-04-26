import cv2 as cv 
import numpy as np 


# Creating an image
## every image is height and width, if has color, it is height, width and channel
img = np.zeros((512,512,3),np.uint8)

img[:]  = 255,0,0 # blue
#img[:] = 0,255,0 # green
#img[:] = 0,0,255 # red

print(img.shape)

## Insert a rectangle within the image 
## img, position 1, position 2, color, type of rectangle
cv.rectangle(img,(0,0), (250,300), (0,255,0), 2)


cv.imshow("Ouput",img)

cv.waitKey(0)