import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hand.png')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,220,255,cv2.THRESH_BINARY_INV)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("test",thresh)
cv2.waitKey(0)
cnt = contours[0] # 1이 손모양 주변의 contour
hull = cv2.convexHull(cnt)

cv2.drawContours(img1, [hull], 0,(0,255,0), 3)

titles = ['Original','Convex Hull']
images = [img, img1]

for i in range(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()