import cv2
import sys
import numpy as np


class FaceDetect():
    def __init__(self):
        self.cascade_file = "C:\\Users\\Playdata\\Desktop\\sung\\python_sung\\opencvofficial\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml"
        self.cascade = cv2.CascadeClassifier(self.cascade_file)

    def face_detect_rec(self,image,image_gs):
        face_list = self.cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

        if len(face_list) > 0:

            print(face_list)
            color = (0, 0, 255)
            for face in face_list:
                x, y, w, h = face
                cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness=8)

            cv2.imwrite("res.png", image)
        else:
            print("no face")
        return image

    def face_detect_crown(self,image,image_gs):
        face_list = self.cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

        if len(face_list) > 0:


            color = (0, 0, 255)
            for face in face_list:
                x, y, w, h = face

                #print("start:",x,y)
                #print("end:",x + w, y + h)
                #cv2.rectangle(image, (x+w//2 - 5, y-5),  (x+w//2 + 5, y+5), color, thickness=8)  # 이걸 크라운으로
                self.draw_crown(y-10,x+w//3,image)


            cv2.imwrite("res.png", image)
        else:
            print("no face")
        return image

    def draw_crown(self,center_x,center_y,image):

        #print("crown center:",center_x, center_y)
        img1 = cv2.imread("crown.jpg")
        b, g, r = cv2.split(img1)
        img1 = cv2.merge([r, g, b])

        rows, cols, channels = img1.shape
        rows2, cols2, channels2 = image.shape
        if (center_x-70 <0 ):
            center_x = 70
        elif (center_x-70+rows>=rows2):
            center_x = rows2 - 1 - rows + 70

        if (center_y - 40 < 0):
            center_y = 40
        elif (center_y-40+cols >= cols2):
            center_y = cols2 - 1 - cols + 40

        roi = image[center_x-70:center_x-70+rows, center_y-40:center_y-40+cols]

        img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 120, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
        img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        dst = cv2.add(img1_fg, img2_bg)

        image[center_x-70:center_x-70+rows, center_y-40:center_y-40+cols] = dst

    def draw_caffebene(self,image):
        img1 = cv2.imread("endinglogo.jpg")
        b, g, r = cv2.split(img1)
        img1 = cv2.merge([r, g, b])
        cols, rows, channels = img1.shape
        cols2, rows2, channels2 = image.shape
        #print(rows,cols)
        #print(rows2, cols2)
        roi = image[cols2 -10 -cols : cols2 -10 , rows2//2 - rows//2 :  rows2//2 + rows//2 ]
        (cols2 -10 -cols , cols2 -10 , rows2//2 - rows//2 ,  rows2//2 + rows//2 )
        image[cols2 -10 -cols : cols2 -10 , rows2//2 - rows//2 :  rows2//2 + rows//2 ] = img1

    def face_detect_list(self,image):
        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_list = self.cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

        return face_list

image_file = ""#"photo9.jpg"

image = cv2.imread(image_file)

image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

f = FaceDetect()

f.face_detect_crown(image=image,image_gs=image_gs)

cv2.imshow("image",image)
cv2.waitKey(0)









