import cv2

img = cv2.imread('lenna.png')

# Display Image
cv2.imshow('Original Image',img)
imageLine = img.copy()

#Draw the image from point A to B
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('Image Line', imageLine)

cv2.waitKey(0)