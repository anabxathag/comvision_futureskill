import cv2

cap = cv2.VideoCapture(0) # 0 -> webcam no.1 your PC

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        # if 'ret' not return something, that mean...
        # there no have image in webcam.
        print("Can't receive frame (stream end?).")
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        # put "q" on keyboard for stop webcam.
        # put "q" again for close tab
        break
    
cv2.waitKey(0)
cap.release() # release file video from memmory
cv2.destroyAllWindows() # destroy all tap that opencv booked it
