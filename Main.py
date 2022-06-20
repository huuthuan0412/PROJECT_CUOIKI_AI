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

# import realtime as RL

root=Tk()

class Main:

    def __init__(self, root):
        def kiemtra():
            username = e1.get()
            password = e2.get()

            if(username == "" and password == "") :
                messagebox.showinfo("Lỗi", "Không tìm thấy tài khoản hoặc mật khẩu")
            elif(username == "HT" and password == "041201"):
                messagebox.showinfo("Thông báo","Đăng nhập thành công!")
                root.destroy()
                import giaodien
               
            else :
                messagebox.showinfo("Lỗi","Sai tài khoản hoặc mật khẩu")
        def quenMK():     
            messagebox.showerror('Lấy lại mật khẩu','Vui lòng xác nhận email để lấy lại mật khẩu')
        def taoTK():
            import taoTK
                    
        root.title("Nguyễn Hữu Thuận_19146400")
        root.geometry("550x200")

        global e1
        global e2

        Label(root, text="Tên đăng nhập:").place(x=100, y=30)
        Label(root, text="Mật khẩu:").place(x=100, y=50)

        e1 = Entry(root)
        e1.place(x=250, y=30)
        e2 = Entry(root)
        e2.place(x=250, y=50)
        e2.config(show="*")
        #fg='#6162FF', bg='white'
        Button(root, text="Đăng Nhập", command=kiemtra ,bg='skyblue').place(x=220, y=90)
        Button(root, command=taoTK,text='Tạo tài khoản mới').place(x=100,y=150)
        Button(root,command=quenMK, text='Quên mật khẩu?').place(x=100,y=120)
                    
        Checkbutton(root, text="Lưu tài khoản").place(x=100, y=80)

Main(root)
root.geometry("550x200")
root.mainloop()

