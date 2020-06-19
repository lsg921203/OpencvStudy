import cv2
import numpy as np

img1 = cv2.imread('images/black_and_white.png')
img2 = cv2.imread('images/white_and_black.png')

def nothing(x):
    pass

cv2.namedWindow('bw')
cv2.createTrackbar('W', 'bw', 0, 100, nothing)

while True:

    w = cv2.getTrackbarPos('W','bw')

    dst = cv2.addWeighted(img1,float(100-w) * 0.01, img2,float(w) * 0.01,0)

    cv2.imshow('bw', dst)

    if cv2.waitKey(1) &0xFF == 27:
        break;

cv2.destroyAllWindows()