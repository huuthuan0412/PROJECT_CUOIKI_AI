import sys
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import Open, SaveAs
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
from matplotlib import image
import os.path
import dlib
import numpy as np
from PIL import ImageTk, Image
# import realtime as RL

root=Tk()

class Main:

    def __init__(self, root):
        def kiemtra():
            username = e1.get()
            password = e2.get()
            repassword=e3.get()

            if((username == "" and password == "")and(repassword == "")):
                messagebox.showinfo("Lỗi", "Tài khoản hoặc mật khẩu không được để trống")
            elif((password==repassword) and (username!="")):
                messagebox.showinfo("Thông báo","Tạo tài khoản thành công!")
                root.destroy()
                # import Main
                import GIAODIENCHINH
               
            else :
                messagebox.showinfo("Lỗi","Sai tài khoản hoặc mật khẩu")

        root.title("Tạo tài khoản mới")
        root.geometry("550x200")

        global e1
        global e2
        global e3

        Label(root, text="Tên đăng nhập:").place(x=100, y=30)
        Label(root, text="Mật khẩu:").place(x=100, y=50)
        Label(root, text="Xác nhận Mật khẩu:").place(x=100, y=70)

        e1 = Entry(root)
        e1.place(x=250, y=30)
        e2 = Entry(root)
        e2.place(x=250, y=50)
        e2.config(show="*")
        e3 = Entry(root)
        e3.place(x=250, y=70)
        e3.config(show="*")
        
        #fg='#6162FF', bg='white'
        Button(root, command=kiemtra,text='Tạo tài khoản mới').place(x=100,y=150)

        #Ẩn/hiện mật khẩu
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_image1 = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image1 = ImageTk.PhotoImage \
            (file='images\\hide.png')

        #nút e2
        self.show_button = Button(root, image=self.show_image,command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=380, y=50)

        #nút e3
        self.show_button1 = Button(root, image=self.show_image1, command=self.show1, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=380, y=70)

    #bật tắt hiện mật khẩu e2
    def show(self):
        self.hide_button = Button(root, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=380, y=50)
        e2.config(show='')

    def hide(self):
        self.show_button = Button(root, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=380, y=50)
        e2.config(show='*')
      

    #bật tắt hiện mật khẩu e3
    def show1(self):
        self.hide_button1 = Button(root, image=self.hide_image1, command=self.hide1, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button1.place(x=380, y=70)
        e3.config(show='')

    def hide1(self):
        self.show_button1 = Button(root, image=self.show_image1, command=self.show1, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=380, y=70)
        e3.config(show='*')


Main(root)
root.geometry("550x200")
root.mainloop()

