import cv2

fn = "ironman.jpg"
img = cv2.imread(fn,cv2.IMREAD_REDUCED_COLOR_2)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()