from PIL import Image
from pytesseract import *
import cv2

filename = "images/tesseract_test.jpg"
img = cv2.imread(filename)

dst = img.copy()

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(src=imggray,
                            thresh=200,
                            maxval=255,
                            type=cv2.THRESH_BINARY)

kenel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

erosion = cv2.erode(thresh,kenel,iterations = 1)

cv2.imshow("Original",img)

cv2.imshow("Erosion",erosion)

image = Image.fromarray(erosion)
text = image_to_string(image, lang="eng")
print("sung: ",text)

cv2.waitKey(0)