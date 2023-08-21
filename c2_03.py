import cv2

#Load an image
image = cv2.imread("lenna.png")

#Display image
cv2.imshow("display",image)

cv2.waitKey(0)
cv2.destroyAllWindows()