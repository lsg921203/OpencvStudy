import tkinter as tk
from tkinter import *
from tkinter import ttk

import cv2
from PIL import Image
from PIL import ImageTk

import os
import threading
import time
import datetime

def make_video_file_list():
    list = os.listdir()
    i = 0

    while True:
        if (i >= len(list)):
            break
        strs = list[i].split(".")
        if len(strs)<2:
            del list[i]
            continue
        if (strs[1] == "avi" or strs[1] == "mp4" ):
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
        self.master.geometry('600x600+100+100')  # 윈도우창 크기 조절
        self.cap = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.videoList = make_video_file_list()
        self.capture_check = True
        self.create_widgets()
        self.th = threading.Thread(target=self.th_capture_manager,args=(lambda :self.capture_check,))
        self.th.start()

    def create_widgets(self):# 여기에서 위젯 변경

        self.frame = Frame(self.master)
        self.scrollbar=Scrollbar(self.frame)
        self.pack(side="right", fill="y")

        self.listbox=Listbox(master=self.frame,yscrollcommand=self.scrollbar.set,selectmode="single")
        self.listbox.pack(side="left")

        for i in range(len(self.videoList)):
            self.listbox.insert(i+1,self.videoList[i])

        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        self.scrollbar["command"]=self.listbox.yview

        self. frame.place(x=100,y=10)

        self.command1 = tk.Button(self.master, font=60, text='command1', command=self.capture_1min)
        self.command1.place( x=245 , y=610)

        self.command2 = tk.Button(self.master, font=60, text='stopVideo', command=self.stopVideo)
        self.command2.place(x=240, y=555)

        self.Exit = tk.Button(self.master, font=60, text='Exit', command=self.Exit)# 이건 지우지 말기
        self.Exit.place(x=280, y=555)
        #self.up_web = tk.Button(self, width=10, font=60, text='web upload')
        #self.up_web.pack()

    def th_capture_manager(self,ld_cc):
        while ld_cc():
            #self.capture_1min()
            self.capture_1min_face_detect()
            time.sleep(1)

    def capture_1min(self):
        now = time.localtime()
        now = "%04d-%02d-%02d %02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        videoName = now + ".avi"
        print(videoName)
        self.out = cv2.VideoWriter(videoName, self.fourcc, 25.0, (640, 480))

        start = time.time()
        end = time.time()
        x=50
        y=100
        t=1
        while (end-start)<60.0:
            if (self.capture_check == False):
                break
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)
                cv2.imshow("save",frame)
                cv2.moveWindow("save",x,y)
                cv2.waitKey(1)
            else:
                break
            x+=t
            if(x>200):
                t=-1
            elif(x<50):
                t=1
            end = time.time()
        self.videoList.append(videoName)
        self.listbox.insert(len(self.videoList),videoName)
        self.out.release()
        cv2.destroyAllWindows()

    def capture_1min_face_detect(self):
        now = time.localtime()
        now = "%04d-%02d-%02d %02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        #videoName = now + ".avi"
        #print(videoName)
        #self.out = cv2.VideoWriter(videoName, self.fourcc, 25.0, (640, 480))

        face_check = False
        frame_list = []
        face_list = []
        f = FaceDetect()

        start = time.time()
        end = time.time()
        x=50
        y=100
        t=1
        while (end-start)<10.0:
            if (self.capture_check == False):
                break
            ret, frame = self.cap.read()
            if ret:
                frame_list.append(frame)
                face_list = f.face_detect_list(frame)
                if len(face_list)>0:
                    face_check = True
                    print("face")


                #self.out.write(frame)
                cv2.imshow("save",frame)
                cv2.moveWindow("save",x,y)
                cv2.waitKey(1)
            else:
                break
            x+=t
            if(x>200):
                t=-1
            elif(x<50):
                t=1
            end = time.time()
        videoName = ""
        if face_check:
            videoName = "facedetected/"+now + ".avi"

        else:
            videoName = "notdetected/"+now + ".avi"

        print(videoName)
        self.out = cv2.VideoWriter(videoName, self.fourcc, 25.0, (640, 480))
        for fr in frame_list:
            self.out.write(frame)

        self.videoList.append(videoName)
        self.listbox.insert(len(self.videoList),videoName)
        self.out.release()
        cv2.destroyAllWindows()

    def onselect(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))
        self.play_video(value)

    def play_video(self,fileName):
        playcap = cv2.VideoCapture(fileName)

        while playcap.isOpened():
            try:
                ret, frame = playcap.read()
                cv2.imshow("load",frame)
                time.sleep(0.025)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except Exception as e:
                break
        playcap.release()
        cv2.destroyAllWindows()



    def stopVideo(self):
        self.capture_check = False
        cv2.waitKey(1)

    def Exit(self):# 이건 지우지 말기

        self.cap.release()
        self.master.destroy()



def main():
    root = tk.Tk()
    A = Application(root)

    root.mainloop()

main()