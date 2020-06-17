import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img = img,
               pt1=(0, 0),
               pt2=(511,511),
               color=(255, 0, 0),
               thickness=5)

img = cv2.rectangle(img=img,
                    pt1=(384,0),
                    pt2=(510,128),
                    color=(0,255,3),
                    thickness=3)

img = cv2.circle(img=img,
                 center=(447,63),
                 radius=63,
                 color=(0,0,255),
                 thickness=1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()