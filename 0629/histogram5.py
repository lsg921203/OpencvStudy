import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('images/tesseract_test3.jpg',0);

# contrast limit가 2이고 title의 size는 8X8
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(5,5))
img2 = clahe.apply(img)

img = cv2.resize(img,(400,400))
img2 = cv2.resize(img2,(400,400))

i = list()


dst = np.hstack((img, img2))
cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()