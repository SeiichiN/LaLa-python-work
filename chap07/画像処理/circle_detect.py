# 円の検出

import cv2
import sys

img = cv2.imread('data/road_sign.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_img.jpg', gray_img)
canny_img = cv2.Canny(gray_img, 600, 650)
cv2.imwrite('canny_img.jpg', canny_img)

circles = cv2.HoughCircles(
    canny_img, 
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=10,
    param1=700,
    param2=27,
    minRadius=20,
    maxRadius=60)
if circles is None:
    sys.exit()

for (x, y, r) in circles[0]:
    cv2.circle(img,
               (int(x),int(y)), 
               int(r), 
               (0,255,0), 
               6)    

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
