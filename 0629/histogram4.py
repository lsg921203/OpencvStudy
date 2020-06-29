import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('images/sky.jpg',0)

# OpenCV의 Equaliztion함수
img2 = cv2.equalizeHist(img)
img = cv2.resize(img,(400,400))
img2 = cv2.resize(img2,(400,400))

dst = np.hstack((img, img2))
cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()