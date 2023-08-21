import cv2

#Load an image
image = cv2.imread("lenna.png")

# Edit pixel in ROI (Region of Interest), y from 50 to 100 
# and x from 30 to 60 as 0 (Black)
image[50:100,30:60] = 0

#Show edited image
cv2.imshow("display",image)

cv2.waitKey(0)
cv2.destroyAllWindows()