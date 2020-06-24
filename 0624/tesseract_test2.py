from PIL import Image
from pytesseract import *
import cv2

filename = "images/tesseract_test6.png"
img = cv2.imread(filename)

img = cv2.resize(src=img,
                 dsize=None,
                 fx=0.25,
                 fy=0.25)

dst = img.copy()

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


ret, thresh = cv2.threshold(src=imggray,
                            thresh=180,
                            maxval=210,
                            type=cv2.THRESH_BINARY)
'''
thresh  = cv2.adaptiveThreshold(src=imggray,
                                     maxValue=255,
                                     adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     thresholdType=cv2.THRESH_BINARY_INV,
                                     blockSize=15,
                                     C=2)
'''

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

dilation = cv2.dilate(thresh, kernel, iterations=0)

cv2.imshow("Original", img)

cv2.imshow("Erosion", dilation)

image = Image.fromarray(dilation)
text = image_to_string(image, lang="kor")
print("sung: ", text)

cv2.waitKey(0)
