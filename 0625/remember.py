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

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter("videos/video1.avi",fourcc,25.0, (320,240))

while True:
    if cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow("camera",frame)
        writer.write(frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break
writer.release()
cap.release()
cv2.destroyWindow("camera")

video = cv2.VideoCapture("videos/video1.avi")

while video.isOpened():
    ret, frame = video.read()
    if ret:
        cv2.imshow("video",frame)
    else:
        break
    if cv2.waitKey(28)&0xFF == ord('q'):
        break





cv2.destroyAllWindows()

#plt.imshow(img)
#plt.xticks([])
#plt.yticks([])
#plt.show()