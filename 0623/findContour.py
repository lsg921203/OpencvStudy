import cv2
import numpy as np

img = cv2.imread('images/sooji7.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)

#contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
#hierachy는 contours line의 계층 구조
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('image', img)
cv2.waitKey(0)

image = cv2.drawContours(img, contours, -1, (0,255,0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()