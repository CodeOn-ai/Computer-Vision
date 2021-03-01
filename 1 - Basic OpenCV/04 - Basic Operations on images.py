import cv2 as cv

img = cv.imread("resources/elliot.jpg")
rows, cols, ch = img.shape

roi = img[150:rows, 150:cols]

cv.imshow("Elliot", img)
cv.imshow("Roi", roi)

cv.waitKey(10000)
cv.destroyAllWindows()