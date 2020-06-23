import cv2
import numpy as np
from matplotlib import pyplot as plt

dotImage = cv2.imread('images/molpology1.JPG')
holeImage = cv2.imread('images/molpology1.JPG')
orig = cv2.imread('images/molpology1.JPG')


kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

erosion = cv2.erode(dotImage,kernel2,iterations = 1)
dilation = cv2.dilate(dotImage,kernel3,iterations = 1)

opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel2)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE,kernel1)
gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel1)
tophat = cv2.morphologyEx(orig, cv2.MORPH_TOPHAT, kernel1)
blackhat = cv2.morphologyEx(orig, cv2.MORPH_BLACKHAT, kernel1)

images =[dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat]
titles =['Dot Image','Erosion','Opening','Hole Image', 'Dilation','Closing', 'Gradient', 'Tophat','Blackhot']

for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()