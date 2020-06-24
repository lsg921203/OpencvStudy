import cv2
import numpy as np
import math
from PIL import Image
from pytesseract import *
import random
from matplotlib import pyplot as plt
from pip._vendor.msgpack.fallback import xrange
import copy

def dist(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x**2 + y**2)

img = cv2.imread('images/c2.jpg')#
img = cv2.resize(img, (600,420))
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imggray = cv2.bilateralFilter(imggray, 7, 90, 30)

ret, thresh = cv2.threshold(imggray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

canny = cv2.Canny(imggray,70,150)

conotours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(img, conotours, -1 , (0,255,0), 3)

roi =[]
for idx, cnt in enumerate(conotours):

    area = cv2.contourArea(cnt)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    w = (dist(box[0],box[1]))
    h = (dist(box[1],box[2]))

    if(h>w):
        tmp = w
        w = h
        h = tmp

    if w==0:
        continue
    if 1/6 <= h/w <=1/4 and area>=100:
        img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        roi = img[box[1][1]:box[0][1], box[1][0]:box[2][0]]

        #perspective

        cv2.imshow("roi", roi)
        res = Image.fromarray(roi)
        text = pytesseract.image_to_string(res, lang='eng')  # 테스트 추출
        print(text)
        cv2.waitKey(0)

cv2.imshow("test", canny)
cv2.waitKey(0)
# 영상에서 번호판 추출 -> part image

#텍스트 추출