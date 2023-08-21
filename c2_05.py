import cv2

#Load an image
image = cv2.imread("lenna.png")

#Write image pixel at x=100,y=100 as 0 (Black)
image[100,100] = 0

#Show edited image
cv2.imshow("display",image)

cv2.waitKey(0)
cv2.destroyAllWindows()