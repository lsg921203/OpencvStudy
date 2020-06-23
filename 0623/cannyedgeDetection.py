import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/IU2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img,100,190)

laplacian = cv2.Laplacian(img,cv2.CV_8U)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'SobelX', 'SobelY', 'Canny']

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title([titles[i]])
    plt.xticks([])
    plt.yticks([])
plt.show()