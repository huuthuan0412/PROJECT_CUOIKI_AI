import sys
from tkinter import *
from tkinter.filedialog import Open, SaveAs
from click import command
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
import pickle as pkl
import dlib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

root = Tk()

class Main(Frame):  
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("PROJECT AI-Nhận dạng góc xoay của khuôn mặt")
        self.pack(fill=BOTH, expand=1)
  
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
  
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.quit)

        VideoMenu = Menu(menubar)
        VideoMenu.add_command(label="RealtimeVIDEO", command=self.onRealtimeVIDEO)
        VideoMenu.add_command(label="Nhandang", command=self.onNhandang)
        
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Face_detect", menu=VideoMenu)
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)
  
    def onOpen(self):
        global ftypes
        ftypes = [('Images', '*.jpg *.tif *.bmp *.gif *.png')]
        dlg = Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            global img
            global imgin
            imgin = cv2.imread(fl,cv2.IMREAD_COLOR)
            ################################################################
            # imgin = img[40:(40+480),:] # Tao ra anh 480x480
            # imgin = cv2.resize(imgin,(250,250))

            img = imgin[...,::-1]
            cv2.namedWindow("ImageIn", cv2.WINDOW_AUTOSIZE)
            #cv22.moveWindow("ImageIn", 200, 200)
            cv2.imshow("ImageIn", imgin)

    def onRealtimeVIDEO(self):
        import cam

    def onNhandang(self):
        global imgin
        def detect_face_points(image):
            detector = dlib.get_frontal_face_detector()
            pred = dlib.shape_predictor("D:/HK6/AI/PROJECTCUOIKI/Detect/shape_predictor_68_face_landmarks.dat")
            face_rect = detector(image, 1)
            if len(face_rect) != 1: return []
            
            dlib_points = pred(image, face_rect[0])
            face_points = []
            for i in range(68):
                x, y = dlib_points.part(i).x, dlib_points.part(i).y
                face_points.append(np.array([x, y]))
            return face_points
                
        def compute_features(face_points):
            assert (len(face_points) == 68), "len(face_points) must be 68"
            
            face_points = np.array(face_points)
            features = []
            for i in range(68):
                for j in range(i+1, 68):
                    features.append(np.linalg.norm(face_points[i]-face_points[j]))#khoang cách 
                    
            return np.array(features).reshape(1, -1)

        img = imgin
        face_points = detect_face_points(img)

        for x, y in face_points:
            cv2.circle(img, (x, y), 1, (0, 255, 0), -1)
            
        features = compute_features(face_points)
        features = std.transform(features)
        model = load_model('models/tinhgoc.h5')
        y_pred = model.predict(features)

        roll_pred, pitch_pred, yaw_pred = y_pred[0]
        print(' X: {:.2f}°'.format(roll_pred))
        print(' Y: {:.2f}°'.format(pitch_pred))
        print(' Z: {:.2f}°'.format(yaw_pred))

        cv2.putText(img,'X: '+str(roll_pred),(1, 10) , cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1)
        cv2.putText(img,'Y: '+str(pitch_pred),(1, 20) , cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0), 1)
        cv2.putText(img,'Z: '+str(yaw_pred),(1, 30) , cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 0, 0), 1)    

        plt.figure(figsize=(10, 10))
        plt.imshow(img)
        plt.show()

x, y = pkl.load(open('D:/HK6/AI/PROJECTCUOIKI/Detect/samples.pkl', 'rb'))
roll, pitch, yaw = y[:, 0], y[:, 1], y[:, 2]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=0.5, random_state=42)
#chuẩn hóa đối tượng
std = StandardScaler()
std.fit(x_train)

Main(root)
root.geometry("550x200")
root.mainloop()       