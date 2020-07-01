import numpy as np
import cv2

img = cv2.imread('images\chessboard.png')
edges = cv2.Canny(img,50,200,apertureSize = 3)
gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
minLineLength = 100
maxLineGap = 8

lines = cv2.HoughLinesP(edges,1,np.pi/360,100,minLineLength,maxLineGap)
for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)


cv2.imshow('img1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()