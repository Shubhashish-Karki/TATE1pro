from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import cv2.face
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Setting window size
        self.root.title("Face recognition")  
        
        title_lbl = Label(self.root, text="Recognition", font=("Arial", 42, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=20, width=1530, height=45)
        
        leftimg1 = Image.open(r"images\rightimg1.jpg")
        leftimg1 = leftimg1.resize((750, 700))
        self.photimg_left = ImageTk.PhotoImage(leftimg1)

        lbl_left = Label(self.root, image=self.photimg_left)
        lbl_left.place(x=15, y=65, width=750, height=700)
        
        rightimg1 = Image.open(r"images\rightimg1.jpg")
        rightimg1 = rightimg1.resize((750, 700))
        self.photimg_right = ImageTk.PhotoImage(rightimg1)

        lbl_right = Label(self.root, image=self.photimg_right)
        lbl_right.place(x=775, y=65, width=750, height=700)
        
        b1=Button( lbl_right,text="Face Recognition",command=self.face_recog, cursor ="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1.place(x=275,y=500,width=350,height=60)

    # -------------attendance--------------
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+", newline ="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and   (r not in name_list) and   (n not in name_list) and   (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {d1}, Present")


        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
            
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+h])
                confidence=int(100*(1-predict/300))
                print("predict="+str(predict)+"confidence="+ str(confidence))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="University@12",database="tate")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from student where sid="+str(id ))#########  roll_no ki Student_id?
                n=my_cursor.fetchone()
                n="".join(str(n))
                
                my_cursor.execute("select roll_no from student where sid="+str(id)) #########  roll_no ki Student_id?
                r=my_cursor.fetchone()
                r="".join(str(r))
                
                my_cursor.execute("select Dep from student where sid="+str(id)) #########  roll_no ki Student_id?
                d=my_cursor.fetchone()
                d="".join(str(d))

                my_cursor.execute("select sid from student where sid="+str(id)) #########  roll_no ki Student_id?
                i=my_cursor.fetchone()
                i="".join(str(i))

                i = i.strip("()\"'")
                r = r.strip("()\"'")
                n = n.strip("()\"'")
                d = d.strip("()\"'")
                
               
                
                

                if confidence>70:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,( x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return(img)
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf = cv2.LBPHFaceRecognizer_create()
        clf=cv2.face.LBPHFaceRecognizer_create()
    
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()

    # Check if the frame was successfully captured
            if ret:
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to face Recognition", img)

        # Check for 'Enter' key press, but only once every 1 frames
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__": 
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()