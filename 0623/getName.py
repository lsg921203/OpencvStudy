import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/name.jpg')
# [x,y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상->우상->좌하->우하
pts1 = np.float32([[1024,1154],[1002,2879],[301,803],[288,3266]])#

# 좌표의 이동점
pts2 = np.float32([[10,10],[1000,10],[10,1000],[1000,1000]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.


M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1100,1100))

imggray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imggray,180,255,cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cv2.imshow("result", thresh)
cv2.waitKey(0)

img = cv2.resize(img,dsize=None,fx=0.25,fy=0.20)

cv2.imshow("Original",img)
#cv2.imshow("thr",thresh)

#cv2.waitKey(0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('image', img)
#cv2.waitKey(0)

image = cv2.drawContours(dst, contours, -1, (0,255,0), -1)

nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

#cv2.imshow("hi",labels)
#print(type(labels[0][0]))

for i in range(nlabels):

    if i < 2:
        continue

    area = stats[i, cv2.CC_STAT_AREA]
    center_x = int(centroids[i, 0])
    center_y = int(centroids[i, 1])
    left = stats[i, cv2.CC_STAT_LEFT]
    top = stats[i, cv2.CC_STAT_TOP]
    width = stats[i, cv2.CC_STAT_WIDTH]
    height = stats[i, cv2.CC_STAT_HEIGHT]


    if area > 50:
        cv2.rectangle(dst,
                      (left, top),
                      (left + width, top + height),
                      (0, 0, 255), 1)
        cv2.circle(dst, (center_x, center_y), 5, (255, 0, 0), 1)
        cv2.putText(dst, str(i), (left + 20, top + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2);

        part = dst[top:top+height,left:left+width]
        cv2.imshow("part"+str(i),part)
        cv2.waitKey(0)



#cv2.imshow("result", dst)


image = cv2.resize(image,dsize=None,fx=0.5,fy=0.5)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()