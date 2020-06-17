import cv2
import numpy as np

def draw_circle(event,x,y,flags, pram):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img=img,
                   center=(x,y),
                   radius=100,
                   color=(255,0,0),
                   thickness=-1)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img=img,
                   center=(x, y),
                   radius=100,
                   color=(0, 0, 0),
                   thickness=-1)
    elif event == cv2.EVENT_MOUSEMOVE :
        cv2.circle(img=img,
                   center=(x, y),
                   radius=50,
                   color=(0, 255, 0),
                   thickness=-1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)

while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == 27: #27 -> esc key
        break

cv2.destroyAllWindows()