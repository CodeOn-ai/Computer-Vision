import cv2 as cv

img  = cv.imread("resources/elliot.jpg") 
img1 = cv.imread("resources/maskmrrobot.jpg")
grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

print(img.shape)
print(img1.shape)

w, h, _ = img.shape

img1 = cv.resize(img1,(h,w))
ret, threshold = cv.threshold(grayImg, 128,255,cv.THRESH_BINARY)

print(img.shape)
print(img1.shape)



weighted = cv.addWeighted(img, 1, img1, 0.5, 0)

add = cv.add(img,img1)

cv.imshow("threshold", threshold)
cv.imshow("add", add)
'''
cv.imshow("add", add)
cv.imshow("weighted", weighted)
cv.imshow("img", img)
cv.imshow("img1",img1)

'''

cv.waitKey(40000)
cv.destroyAllWindows()