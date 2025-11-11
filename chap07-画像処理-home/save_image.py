import cv2

img = cv2.imread('data/block.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
cv2.imwrite('gray.jpg', gray_img)

canny_img = cv2.Canny(img, 50, 100)
cv2.imwrite('canny.jpg', canny_img)

cv2.imshow('img', canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
