from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import cv2.face

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Setting window size
        self.root.title("Train")  
        
        title_lbl = Label(self.root, text="Train Dataset", font=("Arial", 42, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=20, width=1530, height=45)
        
        topimg1 = Image.open(r"images\rightimg1.jpg")
        topimg1 = topimg1.resize((1400, 325))
        self.photimg_top = ImageTk.PhotoImage(topimg1)

        lbl_top = Label(self.root, image=self.photimg_top)
        lbl_top.place(x=60, y=75, width=1400, height=325)
        
        b1=Button(self.root,text="Train data",command=self.train_classifier,cursor ="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=403,width=1530,height=60)

        
        bottomimg1 = Image.open(r"images\rightimg1.jpg")
        bottomimg1 = bottomimg1.resize((1400, 325))
        self.photimg_bottom = ImageTk.PhotoImage(bottomimg1)

        lbl_bottom = Label(self.root, image=self.photimg_bottom)
        lbl_bottom.place(x=60, y=450, width=1400, height=325)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #greyscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")

if __name__ == "__main__": 
    root = Tk()
    obj = Train(root)
    root.mainloop()