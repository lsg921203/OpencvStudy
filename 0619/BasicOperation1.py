import cv2


img1 = cv2.imread("images/nothing.png")
img2 = cv2.imread('images/wind-turbine.jpg')

h,w,c = img1.shape
h2, w2 , c2 = img2.shape
print(w,h,c)
print(w2,h2,c2)
img2[427-164:427-164+h,0:0+w] = img1

cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()