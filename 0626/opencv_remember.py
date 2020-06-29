import cv2

img2 = cv2.imread('images/c2.jpg')
img1 = cv2.imread('images/c4.jpg')

h, w, c = img1.shape
print(w, h, c)

xleft = 100
ytop = 100
roi = img2[ytop:ytop+h, xleft:xleft+w]

img1_g = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img1_g, 170, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

mask_inv = cv2.bitwise_not(mask)

img_s = cv2.bitwise_and(img1, img1, mask=mask_inv)
img_b = cv2.bitwise_and(roi, roi, mask=mask)

dst = cv2.add(img_s,img_b)

cv2.imshow("dst",dst)
cv2.waitKey(0)