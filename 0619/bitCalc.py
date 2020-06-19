import cv2

img1 = cv2.imread('images/black_and_white.png')
img2 = cv2.imread('images/white_and_black.png')

img3 = cv2.bitwise_and(img1, img2)
img4 = cv2.bitwise_or(img1, img2)
img5 = cv2.bitwise_not(img2)
img6 = cv2.bitwise_xor(img1, img2)

imgh1 = cv2.hconcat([img1,img2,img3])
imgh2 = cv2.hconcat([img4,img5,img6])

res = cv2.vconcat([imgh1,imgh2])

cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()