from PIL import Image
from pytesseract import *
import cv2
import numpy as np

img = cv2.imread('images/tesseract_test3.jpg',0);

# contrast limit가 2이고 title의 size는 8X8
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
img1 = clahe.apply(img)

#img1 = cv2.resize(img1,None,None,0.5,0.5,)


ret, thresh = cv2.threshold(src=img1,
                            thresh=0,
                            maxval=210,
                            type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
thresh = cv2.adaptiveThreshold(src=img1,
                               maxValue=255,
                               adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               thresholdType=cv2.THRESH_BINARY,
                               blockSize=51,
                               C=20)
'''
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

erosion = cv2.erode(thresh, kernel, iterations=0)

cv2.imshow("Original", thresh)

cv2.imshow("Erosion", erosion)

image = Image.fromarray(erosion)
text = image_to_string(image, lang="eng")
print("sung: ", text)

cv2.waitKey(0)
cv2.destroyAllWindows()