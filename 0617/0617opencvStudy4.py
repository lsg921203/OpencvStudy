import cv2

cap = cv2.VideoCapture(0)

print("width: {0}, height: {1}".format(cap.get(3),cap.get(4)))
cap.set(3,320)
cap.set(4,240)

while(True):
    ret, frame = cap.read()

    if(ret):
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()