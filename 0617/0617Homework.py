import numpy as np
import cv2
import os

def file_check(list, file_name):
    for f in list:
        if f == file_name:
            return False
    return True

list = os.listdir()
i =0

capture = cv2.VideoCapture(0)
ret, frame = capture.read()



cv2.waitKey(0)
cv2.destroyAllWindows()

while True:
    if(i>=len(list)):
        break
    strs = list[i].split(".")
    if(strs[1] == "jpg" or strs[1] ==".png" or strs[1] ==".gif"):
        i+=1
    else:
        del list[i]


i = 0
n = 0
camera_shot_check =False
while True:
    if(not camera_shot_check):
        fn = list[i]
        img = cv2.imread(fn, cv2.IMREAD_REDUCED_COLOR_2)
        cv2.imshow("image", img)

        cmd = cv2.waitKey(0)
    camera_shot_check = False

    if cmd & 0xFF==ord('q'):
        break
    elif cmd & 0xFF==ord('n'):
        i+=1
        if(i>=len(list)):
            i=0
    elif cmd & 0xFF==ord('p'):
        i-=1
        if(i<0):
            i = len(list)-1
    elif cmd & 0xFF==ord('c'):
        ret, frame = capture.read()
        cv2.imshow("image", frame)
        cmd = cv2.waitKey(0)
        camera_shot_check = True

    elif cmd & 0xFF==ord('s'):
        print("s 진입")
        while True:
            file_name = "photo" + str(n) + ".jpg"
            print("check : "+file_name)
            if (file_check(list, file_name)):
                break
            else:
                n += 1
        print(file_name)
        cv2.imwrite(file_name, frame)
        list.append(file_name)
cv2.destroyAllWindows()