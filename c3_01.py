import cv2

img = cv2.imread('lenna.png')

# Display Image
cv2.imshow('Original Image',img)

# make a copy of the original image
imageRectangle = img.copy()
# define the starting and end points of the rectangle
start_point =(300,115)
end_point =(475,225)
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(0)