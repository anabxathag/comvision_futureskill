import cv2

#Load an image
image = cv2.imread("lenna.png")

#Show image properties
print(f'The size of the Image is: {image.shape}')
print(f'The data type of the Image is: {image.dtype}')
print(f'The dimensions of the Image is: {image.ndim}')

cv2.waitKey(0)
cv2.destroyAllWindows()