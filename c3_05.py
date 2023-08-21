import cv2
import numpy as np

img = cv2.imread('lenna.png')

# Display Image
cv2.imshow('Original Image',img)

# make a copy of the original image
imagePoly = img.copy()

penta = np.array([[[40,160],[120,100],[200,160],[160,240],[80,240]]], np.int32)
triangle = np.array([[[240, 130], [380, 230], [190, 280]]], np.int32)

cv2.polylines(imagePoly, [triangle], True, (0,255,0), thickness=3)
cv2.polylines(imagePoly, [penta], True, (255,120,255),3)
cv2.imshow('imagePoly', imagePoly)
cv2.waitKey(0)