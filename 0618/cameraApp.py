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

            image = Image.fromarray(frame)
            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)
        if self.isBlack == True:
            ret, frame = self.capture.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
            b, g, r = cv2.split(frame)
            frame = cv2.merge([r, g, b])
            frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            f = FaceDetect()

            f.face_detect_crown(image=image, image_gs=image_gs)
            # cv2.imshow("frame",frame)

            image = Image.fromarray(frame)
            self.img_tk = ImageTk.PhotoImage(image=image)
            self.label = tk.Label(master=self.master, image=self.img_tk)
            self.label.place(x=10, y=10)



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

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # cv2.imshow("frame",frame)

            image = Image.fromarray(frame)
            print(type(image))
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
            print("before photo")
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