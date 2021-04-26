import cv2 as cv 
import numpy as np 

img = cv.imread("resources/squares.jpg")

# conver to gray scale
g_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# corner detector 
corners = cv.goodFeaturesToTrack(g_img, 100, 0.1, 10)

# draw a circle on each corner detected
for corner in corners:
    x,y = corner.ravel() # numpy function to get points 
    cv.circle(img, (x,y), 3,(0,0,255), -1)  # drawing in the original image


cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()