import cv2

#Load an image
image = cv2.imread("lenna.png")

#Print image infomation as is
print(image)

cv2.waitKey(0)
cv2.destroyAllWindows()