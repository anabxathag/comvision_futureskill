import cv2

img = cv2.imread('lenna.png')

# Display Image
cv2.imshow('Original Image',img)

# make a copy of the original image
imageText = img.copy()
#let's write the text you want to put on the image
text = 'Hello OpenCV'
#org: Where you want to put the text
org = (50,350)
# write the text on the input image
cv2.putText(imageText, text, org, fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (250,225,100))
# display the output image with text over it
cv2.imshow("Image Text",imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()