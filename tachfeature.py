from unittest import result
import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import pandas as pd

def detect_face_points(image):
    detector = dlib.get_frontal_face_detector()
    pred = dlib.shape_predictor("D:\HK6\AI\PROJECTCUOIKI\Detect\shape_predictor_68_face_landmarks.dat")
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
a=[]
b=[]
data_folder='D:\HK6\AI\PROJECTCUOIKI\TEST'
#join tung anh
for folder in os.listdir(data_folder):
  #Lăp các file trong thư mục con
    curr_file= os.path.join(data_folder, folder)
#   for file in os.listdir(curr_path):
    #   curr_file=os.path.join(curr_path,file)
    img=cv2.imread(curr_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_points = detect_face_points(img)

    for x, y in face_points:
        cv2.circle(img, (x, y), 1, (0, 255, 0), -1)
    
    features = compute_features(face_points) 
    a.append(features) 
    b.append(data_folder)

    matrix=[b,a]
    np.savetxt('feature',matrix,fmt='%s')
print(len(a))
print(a[0]) 
