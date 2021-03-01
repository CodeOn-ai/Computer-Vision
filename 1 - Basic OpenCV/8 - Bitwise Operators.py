import cv2 as cv 

#Load image
img1 = cv.imread("resources/drawing_1.png")
img2 = cv.imread("resources/drawing_2.png")

# Bitwise operators
bit_and = cv.bitwise_and(img1,img2)
bit_or = cv.bitwise_or(img1,img2)
bit_xor = cv.bitwise_xor(img1,img2)
bit_not = cv.bitwise_not(img1)

# Show images 
cv.imshow("img1", img1)
cv.imshow("img2", img2)

# Show bitwise results 
cv.imshow("bit_and", bit_and)
cv.imshow("bit_or", bit_or)
cv.imshow("bit_xor", bit_xor)
cv.imshow("bit_not", bit_not)


cv.waitKey(20000)
cv.destroyAllWindows()