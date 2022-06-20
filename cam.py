#Import required modules
import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
from sklearn.preprocessing import StandardScaler
import pickle as pkl
from sklearn.model_selection import train_test_split
#Dlib positions
#  ("mouth", (48, 68)),
#	("right_eyebrow", (17, 22)),
#	("left_eyebrow", (22, 27)),
#	("right_eye", (36, 42)),
#	("left_eye", (42, 48)),
#	("nose", (27, 35)),
#	("jaw", (0, 17))

# Mở cam máy tính của bạn
video_capture = cv2.VideoCapture(0)
  
# #Thay đổi tốc độ khung hình
# video_capture.set(cv2.cv.CV_CAP_PROP_FPS, 30)

# #Thay đổi độ phân giải
# video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320);
# video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 130);
#Face detector

#(Landmark identifier). file thầy Trần Tiến Đức
def detect_face_points(image):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("D:/HK6/AI/PROJECTCUOIKI/Detect/shape_predictor_68_face_landmarks.dat")
    face_rect = detector(image, 1)
    if len(face_rect) != 1: return []
    
    dlib_points = predictor(image, face_rect[0])
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
            features.append(np.linalg.norm(face_points[i]-face_points[j]))
            
    return np.array(features).reshape(1, -1)


x, y = pkl.load(open('D:/HK6/AI/PROJECTCUOIKI/Detect/samples.pkl', 'rb'))
roll, pitch, yaw = y[:, 0], y[:, 1], y[:, 2]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=0.5, random_state=42)
#chuẩn hóa đối tượng
std = StandardScaler()
std.fit(x_train)

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1) 
    
    try:
    
        face_points = detect_face_points(frame)
        for x, y in face_points:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        model = load_model('D:/HK6/AI/PROJECTCUOIKI/models/tinhgoc.h5')
        
        features = compute_features(face_points)
        features = std.transform(features)
        y_pred = model.predict(features)
        
        roll_pred, pitch_pred, yaw_pred = y_pred[0]

        cv2.putText(frame,'X: '+str(roll_pred),(20, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
        cv2.putText(frame,'Y: '+str(pitch_pred),(20, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
        cv2.putText(frame,'Z: '+str(yaw_pred),(20, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)

    except:
        pass
    
    
    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
video_capture.release()
# Destroy all the windows
cv2.destroyAllWindows()

            
