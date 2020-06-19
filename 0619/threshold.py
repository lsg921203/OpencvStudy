import cv2
img1 = cv2.imread("images/yellowFlower.png")
img2 = cv2.imread("images/wind-turbine.jpg")

h,w,c = img1.shape
print(w,h,c)

roi = img2[0:0+h,0:0+w]

img1_g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1_g,185,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_s = cv2.bitwise_and(img1,img1,mask = mask )
img_b = cv2.bitwise_and(roi,roi,mask=mask_inv)

dst = cv2.add(img_b,img_s)

img2[0:0+h,0:0+w] = dst

cv2.imshow('img',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()