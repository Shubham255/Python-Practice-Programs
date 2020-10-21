import os
import numpy
import cv2

#following block for detect the face
def faceDetection(test_img):
    gray_img=cv2.cvtColor=(test_img,cv2.COLOR_BGR2GRAY)
    face_haar=cv2.CascadeClassifier(r"C:\Users\Windows 10\AppData\Local\Programs\Python\Python37\haarcascade_frontalface_alt.xml")
    faces=face_haar.detectMultiScale(gray_img,scale_factor=1.3,minNeighbors=3)
    return faces,gray_img

#faceDetection(r'C:\Users\Windows 10\AppData\Local\Programs\Python\Python37\Test_image.jpg')


def labels_for_training_data(directory):
    faces=[]
    faceID=[]

    for path,subdirnames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("skipping system files")
                continue

            id=os.path.basename(path)
            img_path=os.path.join(path,filename)
            print("img_path",img_path)
            print("id",id)
            test_img=cv2.imread(img_path)
            if test_img is None:
                print("Not Loded properly")
                continue

            faces_rect,gray_img=faceDetection(test_img)
            (x,y,w,h)=face_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID

def train_Classifier(faces,faceID):
        face_recognizer=cv2.face.LBPHfFaceRecognizer_create()
        face_recognizer.train(faces,np.array(faceID))
        return face_recognizer
#following for rectangel on face
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

def put_text(test_img,label_name,x,y):
    cv2.putText(test_img,label_name,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),3)
