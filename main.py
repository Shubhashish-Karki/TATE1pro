from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from studentdetails import Student
import os

class Face_recog:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0") #setting window size
        self.root.title("Face recognition attendance system ") # name of window

        #background image
        img1 = Image.open(r"C:\Users\shubh\OneDrive\Desktop\TATE\images\download.jpg")
        img1 = img1.resize((1800, 1000))
        self.photimg1=ImageTk.PhotoImage(img1)

        lbl_1 = Label(self.root,image=self.photimg1)
        lbl_1.place(x=0,y=0,width=1800,height=1000)

        #font in image
        title_lbl = Label(lbl_1,text="TATE",font=("Arial",42,"bold"),bg="gold",fg="green")
        title_lbl.place(x=0,y=20,width=1530,height=45)

        #button
        btn1 = Image.open(r"C:\Users\shubh\OneDrive\Desktop\TATE\images\btn1.jpg")
        btn1 = btn1.resize((220, 220))
        self.photoimg2=ImageTk.PhotoImage(btn1)
        
        #student info
        b1=Button(lbl_1,command=self.student_details,image=self.photoimg2,cursor ="hand2")
        b1.place(x=100,y=500,width=220,height=220)
        
        b_1=Button(lbl_1,text="Student Details",command=self.student_details,cursor ="hand2", font=("arial",25,),bg="darkblue",fg="white")
        b_1.place(x=100,y=720,width=220,height=30)

        #button
        btn2 = Image.open(r"C:\Users\shubh\OneDrive\Desktop\TATE\images\btn2.jpg")
        btn2 = btn2.resize((220, 220))
        self.photoimg3=ImageTk.PhotoImage(btn2)
        
        #student info
        b2=Button(lbl_1,image=self.photoimg3,cursor ="hand2")
        b2.place(x=350,y=500,width=220,height=220)
        
        b_2=Button(lbl_1,text="Attendance",cursor ="hand2", font=("arial",25,),bg="darkblue",fg="white")
        b_2.place(x=350,y=720,width=220,height=30)


        #button function --------------------------------

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()