import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hierarchy.jpg')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,200,255,cv2.THRESH_BINARY)

#cv2.imshow("test",thresh)
#cv2.waitKey(0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cnt = contours[2] # 14번째가 지도의 contour line

print(hierachy)
max_area = 0
max_index = 0

for idx,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    if(max_area<area):
        max_area = area
        max_index = idx

print(max_index)
cnt = contours[max_index]

# 끝점 좌표 찾기
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

# 좌표 표시하기
#cv2.circle(img1,leftmost,20,(0,0,255),-1)
#cv2.circle(img1,rightmost,20,(0,0,255),-1)
#cv2.circle(img1,topmost,20,(0,0,255),-1)
#cv2.circle(img1,bottommost,20,(0,0,255),-1)

img1 = cv2.drawContours(img1, cnt, -1, (255,0,0), 5)

titles = ['Original','Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()