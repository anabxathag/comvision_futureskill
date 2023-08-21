import cv2

#Load an image
image = cv2.imread("lenna.png")

#Show edited image in ROI (Region of Interest)
cv2.imshow("display",image[0:512,200:300])

cv2.waitKey(0)
cv2.destroyAllWindows()