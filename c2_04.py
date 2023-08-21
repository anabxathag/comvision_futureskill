import cv2

#Load an image
image = cv2.imread("lenna.png")

#Read image pixel at x=100,y=100 then print to screen
print(image[100,100])

cv2.waitKey(0)
cv2.destroyAllWindows()