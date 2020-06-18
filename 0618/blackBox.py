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
        if (strs[1] == "avi" or strs[1] == "mp4" ):
            i += 1
        else:
            del list[i]
    return list

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
            self.capture_1min()
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