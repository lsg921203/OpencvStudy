import cv2
import numpy as np

img1 = cv2.imread('images/sparrow.jpg')
img2 = cv2.imread('images/sky.jpg')

img1 = img1[0:426,0:640]
def nothing(x):
    pass

cv2.namedWindow('sparrow the hero')
cv2.createTrackbar('W', 'sparrow the hero', 0, 100, nothing)

while True:

    w = cv2.getTrackbarPos('W','sparrow the hero')

    dst = cv2.addWeighted(img1,float(100-w) * 0.01, img2,float(w) * 0.01,0)

    cv2.imshow('sparrow the hero', dst)

    if cv2.waitKey(1) &0xFF == 27:
        break;

cv2.destroyAllWindows()