import cv2

#Load an image
image = cv2.imread("lenna.png")

#Edit pixel area
image[50:100,50:100] = 0

#Show edited image
cv2.imshow("display",image)

#Save edited image to disk
#cv2.imwrite("result.png",image)

cv2.waitKey(0)
cv2.destroyAllWindows()