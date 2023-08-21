import cv2
import numpy as np

coins_color = cv2.imread('coins.png')
cv2.imshow("coins_color", coins_color)

coins_gray = cv2.cvtColor(coins_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("coins_gray", coins_gray)

_, coins_th = cv2.threshold(coins_gray, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("coins_th", coins_th)

contours, _ = cv2.findContours(coins_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(coins_color, contours, -1, (255, 0, 255), -1)

cv2.imshow("detected", coins_color)
cv2.waitKey(0)