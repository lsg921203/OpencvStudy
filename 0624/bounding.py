import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/contourApproximate.jpg')
img1 = img.copy()

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imggray,220,255,cv2.THRESH_BINARY_INV)
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[2]

#straight rec
x, y, w, h = cv2.boundingRect(cnt)
img1 = cv2.rectangle(img1, (x, y), (x+w, y+h),(0,255,0), 3)

#rotated rec
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img1 = cv2.drawContours(img1, [box], 0, (0, 0, 255), 3)

#minimum enclosing circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img1 = cv2.circle(img1, center, radius, (255, 255, 0), 3)

#fitting an ellipse
ellipse = cv2.fitEllipse(cnt)
img1 = cv2.ellipse(img1, ellipse, (255, 0, 0), 3)

titles = ['Original', 'Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.xticks([])
    plt.yticks([])

plt.show()