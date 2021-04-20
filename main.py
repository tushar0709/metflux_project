import tkinter as tk
from tkinter import messagebox
import cv2
import time as tm
import os.path
import subprocess
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import resize
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle








window = tk.Tk()
window.title("Face_Recogniser")
window.geometry("858x720")

window.resizable(False,False)
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(
    window, text="Welcome to METFLUX pvt ltd",
    bg="green", fg="white", width=35,
    height=2, font=('times', 30, 'bold'))
message.place(x=5,y=20)

photo1 = ImageTk.PhotoImage(Image.open('metflux_logo.png'))
lab = tk.Label(image= photo1)
lab.place(x=330,y=150)

photo = ImageTk.PhotoImage(Image.open('face_recg.png'))
lab = tk.Label(image= photo)
lab.place(x=130,y=320)

def display_time():

    curr_day = tm.strftime("%A")
    curr_date = tm.strftime("%d")
    curr_month = tm.strftime("%B")
    curr_time = tm.strftime("%I:%M:%S %p")
    clock_label['text'] = curr_time
    clock_label.after(200,display_time)
    date_label['text'] = curr_day +',' +curr_date + ' '+ curr_month

clock_label = tk.Label(window,font= 'arial 20',fg = 'black')
clock_label.place(x=587,y=240)
date_label = tk.Label(window,font= 'arial 20',fg = 'black')
date_label.place(x=170,y=240)
display_time()




cap = cv2.VideoCapture(0)
global flag
flag= False
def upload():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="Select file" )
    messagebox.askquestion("Confirm","Are you sure?")
    flag = True

    if not filename:
        return



def Display():
    if flag is True:
        im = Image.open(filename)
        im.show()
    else:
        messagebox.showwarning("warning","Upload Image First !")

def from_camera():
    subprocess.run("python face_detection.py")


def from_image():

    if flag == True:
        pixels = imread(filename)
        pixels = resize(pixels, (1500, 900))
        classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
        bboxes = classifier.detectMultiScale(pixels, 1.1, 3)
        for box in bboxes:
            x, y, width, height = box
            x2, y2 = x + width, y + height
            rectangle(pixels, (x, y), (x2, y2), (0, 0, 255), 1)
        imshow('face detection', pixels)
        waitKey(0)
        destroyAllWindows()

    else:
        messagebox.showwarning("warning","Upload Image First !")



def destroy():
    if messagebox.askyesno('Quit', 'Are you sure you want to exit ? ', icon = 'question') == True:
        window.destroy()
    else:
        pass



takeImg = tk.Button(window, text="UPLOAD IMAGE",
                    command=upload, fg="white", bg="green",
                    width=18, height=3, activebackground="Red",
                    font=('times', 10, ' bold '))
takeImg.place(x=600, y=300)



entry = tk.Button(window, text="VIEW IMAGE",
                     command=Display, fg="white", bg="green",
                     width=18, height=3, activebackground="Red",
                     font=('times', 10, ' bold '))
entry.place(x=600, y=400)
open = tk.Button(window, text="OPEN CAMERA",
                     command=from_camera, fg="white", bg="green",
                     width=18, height=3, activebackground="Red",
                     font=('times', 10, ' bold '))
open.place(x=200, y=600)
quitWindow = tk.Button(window, text="DETECT FACE",
                       command=from_image, fg="white", bg="green",
                       width=18, height=3, activebackground="Red",
                       font=('times', 10, ' bold '))
quitWindow.place(x=600, y=500)


quitWindow = tk.Button(window, text="QUIT",
                       command=destroy, fg="white", bg="red",
                       width=18, height=3, activebackground="Red",
                       font=('times', 10, ' bold '))
quitWindow.place(x=600, y=600)


window.mainloop()
