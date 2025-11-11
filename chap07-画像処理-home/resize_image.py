# p284

import cv2

img = cv2.imread('data/block.jpg')

height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img, (int(width/2), height))
cv2.imwrite('resized.jpg', resized_img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
