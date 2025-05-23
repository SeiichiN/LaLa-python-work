# 画像処理

import cv2

img = cv2.imread('data/block.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画像サイズの変更
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img, (int(width/2), height))
cv2.imwrite('resized.jpg', resized_img)

# 色をグレーにする
gray_img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
cv2.imwrite('gray.jpg', gray_img)

# エッジ検出
canny_img = cv2.Canny(img, 50, 100)  # エッジの長さ、輝度
cv2.imwrite('canny.jpg', canny_img)