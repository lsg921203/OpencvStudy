import cv2


capture = cv2.VideoCapture(0)
ret, frame= capture.read()

print(frame.shape)

cv2.imshow('b',frame)
cv2.imwrite("images/test1.jpg", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()