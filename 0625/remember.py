import cv2
from matplotlib import pyplot as plt
img = cv2.imread("images/c2.jpg")
img = cv2.resize(img,dsize=(300,200))

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite("images/c2gray.jpg",grayimg)

cv2.imshow("img",grayimg)
cv2.waitKey(0)

cv2.destroyWindow("img")
#cv2.destroyAllWindows()

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()