import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img=img,
               pt1=(110, 110),
               pt2=(400, 400),
               color=(255, 255, 255),
               thickness=5)

img = cv2.rectangle(img=img,
                    pt1=(10, 10),
                    pt2=(100, 100),
                    color=(255, 255, 0),
                    thickness=5)

img = cv2.circle(img=img,
                 center=(256, 256),
                 radius=100,
                 color=(0, 0, 255),
                 thickness=5)

img = cv2.ellipse(img=img,
                  center=(256, 256),
                  axes=(100, 50),
                  angle=70,
                  startAngle=10,
                  endAngle=130,
                  color=(255, 0, 255),
                  thickness=-1)

img = cv2.polylines(img=img,
                    pts=np.array([[[100, 100],
                                   [100, 200],
                                   [200, 200],
                                   [200, 300],
                                   [300, 400],
                                   [100, 400]]]),
                    isClosed=True,
                    color=(128, 128, 128),
                    thickness=5)

cv2.imshow("canvas",img)
cv2.waitKey(0)