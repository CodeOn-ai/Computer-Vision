import cv2 as cv 
import numpy as np 

img = cv.imread("resources/red_panda.jpg")


imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, normal_threshold = cv.threshold(imgGray, 155,255,cv.THRESH_BINARY)

#Since some images have different lighting we use can use adaptive
mean_c = cv.adaptiveThreshold(imgGray,
                                       255, 
                                       cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY,
                                       11,
                                       3,
                                       )

mean_gauss = cv.adaptiveThreshold(imgGray,
                                       255, 
                                       cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY,
                                       11,
                                       3,
                                       )

#cv.imshow("img", img)
cv.imshow("normal_threshold", normal_threshold)
cv.imshow("mean_c", mean_c)
cv.imshow("mean_gauss", mean_gauss)
cv.waitKey(0)
cv.destroyAllWindows()