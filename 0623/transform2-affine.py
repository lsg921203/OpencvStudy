#-*- coding:utf-8 -*-
import cv2
import numpy as np
import math
img = cv2.imread('images/wind-turbine.jpg')

rows, cols = img.shape[:2]

# 변환 행렬, X축으로 10, Y축으로 20 이동
M = np.float32([[1,0,10],[0,1,20]])
M2 = cv2.getRotationMatrix2D((cols/2, rows/2),70, 0.7)

dst = cv2.warpAffine(img, M,(cols, rows))
dst2 = cv2.warpAffine(img, M2,(cols, rows))
cv2.imshow('Original', img)
cv2.imshow('Translation', dst)
cv2.imshow('Translation2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()