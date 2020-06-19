import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import cv2
import os
import threading
import time
def file_check(list, file_name):
    for f in list:
        if f == file_name:
            return False
    return True

def make_image_file_list():
    list = os.listdir()
    i = 0

    while True:
        if (i >= len(list)):
            break
        strs = list[i].split(".")
        if (strs[1] == "jpg" or strs[1] == ".png" or strs[1] == ".gif"):
            i += 1
        else:
            del list[i]
    return list
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
class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('680x600+100+100')  # 윈도우창 크기 조절
        self.create_widgets()
        self.capture = cv2.VideoCapture(0)
        self.check_current_state = False #False:촬영모드 , True: 사진보기모드
        self.image_file_list = make_image_file_list()
        self.current_filenum = 0
        self.image_num = 0
        self.image_name = "photo"
        self.start_preview()
        self.isBlack = False
        self.f = FaceDetect()

    def create_widgets(self):# 여기에서 위젯 변경

        self.command1 = tk.Button(self.master, font=60,width=10, text='color', command=self.Button_command1)
        self.command1.place( x=145 , y=510)

        self.command2 = tk.Button(self.master, font=60,width=10, text='gray', command=self.Button_command2)
        self.command2.place(x=295, y=510)

        self.command3 = tk.Button(self.master, font=60,width=13, text='사진보기 모드로', command=self.Button_command3)
        self.command3.place(x=445, y=510)

        self.Exit = tk.Button(self.master, font=60, text='Exit', command=self.Exit)# 이건 지우지 말기
        self.Exit.place(x=280, y=555)

        self.label = tk.Label(master=self.master)
        self.label.place(x=10, y=10)
        #self.canvas = Canvas(self.master, width=320, height=240)
        #self.canvas.place(x=10,y=10)


        #self.up_web = tk.Button(self, width=10, font=60, text='web upload')
        #self.up_web.pack()
    def save_image(self,frame):
        while True:
            file_name = self.image_name + str(self.image_num) + ".jpg"
            print("check : "+file_name)
            if (file_check(self.image_file_list, file_name)):
                break
            else:
                self.image_num += 1
        print("save as :"+file_name)
        cv2.imwrite(file_name, frame)
        self.image_file_list.append(file_name)

    def start_preview(self):
        self.th = threading.Thread(target=self.th_preview)
        self.th.start()
    def th_preview(self):
        while not self.check_current_state:#촬영모드 일때만
            ret, frame = self.capture.read()
            b, g, r = cv2.split(frame)
            frame = cv2.merge([r, g, b])
            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.f.face_detect_crown(image=frame, image_gs=frame_gs)

            image = Image.fromarray(frame)
            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)
        if self.isBlack == True:
            ret, frame = self.capture.read()
            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.f.face_detect_crown(image=frame, image_gs=frame_gs)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.merge([frame,frame,frame])

            self.f.draw_caffebene(frame)

            image = Image.fromarray(frame)
            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)
            self.isBlack = False

    def Button_command1(self):
        if (not self.check_current_state):
            self.Button_command3()
            time.sleep(0.1)
            ret, frame = self.capture.read()

            print(ret)
            self.save_image(frame=frame)

            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            b, g, r = cv2.split(frame)
            frame = cv2.merge([r, g, b])




            self.f.face_detect_crown(image=frame, image_gs=frame_gs)
            self.f.draw_caffebene(frame)

            #cv2.imshow("frame",frame)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            image = Image.fromarray(frame)
            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)

            r, g, b = cv2.split(frame)
            frame = cv2.merge([b, g, r])

            self.save_image(frame=frame)

            self.current_filenum = len(self.image_file_list) - 1
            self.isBlack = False
        else:
            self.current_filenum -= 1
            if( self.current_filenum<0):
                self.current_filenum = len(self.image_file_list) - 1
            fn = self.image_file_list[self.current_filenum]
            frame = cv2.imread(fn, cv2.IMREAD_COLOR)  # IMREAD_REDUCED_COLOR_2

            b, g, r = cv2.split(frame)
            frame = cv2.merge([r, g, b])
            image = Image.fromarray(frame)

            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)
            print("before photo")


    def Button_command2(self):
        if (not self.check_current_state):
            self.Button_command3()

            ret, frame = self.capture.read()

            print(ret)

            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.f.face_detect_crown(image=frame, image_gs=frame_gs)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.merge([frame, frame, frame])

            self.f.draw_caffebene(frame)
            # cv2.imshow("frame",frame)

            r, g, b = cv2.split(frame)
            frame = cv2.merge([b, g, r])

            image = Image.fromarray(frame)

            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)

            self.save_image(frame=frame)

            self.current_filenum = len(self.image_file_list) - 1
            self.isBlack = True
        else:
            self.current_filenum += 1
            if(self.current_filenum>=len(self.image_file_list)):
                self.current_filenum = 0
            fn = self.image_file_list[self.current_filenum]
            frame = cv2.imread(fn, cv2.IMREAD_COLOR)  # IMREAD_REDUCED_COLOR_2
            b, g, r = cv2.split(frame)
            frame = cv2.merge([r, g, b])
            image = Image.fromarray(frame)

            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)
            print("next photo")
    def Button_command3(self):
        if(not self.check_current_state):
            self.check_current_state = True
            self.command1.config(text="이전 사진")
            self.command2.config(text="다음 사진")
            self.command3.config(text="촬영 모드로")

        else:
            self.check_current_state = False
            self.command1.config(text="color")
            self.command2.config(text="gray")
            self.command3.config(text="사진보기 모드로")
            self.start_preview()
        print(self.check_current_state)




    def Exit(self):# 이건 지우지 말기


        self.master.destroy()



def main():
    root = tk.Tk()
    A = Application(root)

    root.mainloop()

main()