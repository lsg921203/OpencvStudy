import cv2
import numpy as np

cap = cv2.VideoCapture("videos/mimvideo.mp4")
cap.set(3,320)
cap.set(4,240)

while(1):
    ret, frame = cap.read()


    #dst2 = cv2.resize(frame, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
    if ret:
        frame = cv2.resize(frame, dsize=(150, 100), interpolation=cv2.INTER_AREA)
        #image = cv2.cvtColor(frame,cv2.COLOR)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lower_orange = np.array([55, 150, 100])#[11, 170, 50]
        upper_orange = np.array([170, 255, 255])#[33, 255, 255]

        mask = cv2.inRange(hsv, lower_orange, upper_orange)
        mask_inv = cv2.bitwise_not(mask)
        # bit연산자를 통해서 blue영역만 남김.
        res = cv2.bitwise_and(frame, frame, mask=mask_inv)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
    else:
        cap = cv2.VideoCapture("videos/mimvideo.mp4")

    if cv2.waitKey(25) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()