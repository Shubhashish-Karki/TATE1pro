from tkinter import *
import customtkinter
from tkinter import ttk
from PIL import Image, ImageTk
from studentdetails import Student
from tkinter import messagebox
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import cv2
import mysql.connector
import numpy as np
import cv2.face


class Face_recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                           root.winfo_screenheight()))  # setting window size
        # name of window
        self.root.title("Transparent Attendance Tracking System - TATE ")

        # background image
        img1 = Image.open(r"images\homebg.jpg")

        img1 = img1.resize((self.root.winfo_screenwidth(),
                           self.root.winfo_screenheight()))
        self.photimg1 = ImageTk.PhotoImage(img1)

        # lbl_1 = Label(self.root, image=self.photimg1)
        # lbl_1.place(x=0, y=0, width=1800, height=1000)

        lbl_1 = Label(self.root, image=self.photimg1)
        lbl_1.place(x=0, y=0, relwidth=1, relheight=1)

        # # font in image
        # title_lbl = Label(lbl_1, text="TATE", font=(
        #     "Arial", 42, "bold"), bg="gold", fg="green")
        # title_lbl.place(x=0, y=20, width=1530, height=45)

        # button
        info_icon = ImageTk.PhotoImage(Image.open(
            "icons\info.png").resize((20, 20), Image.LANCZOS))
        button_1 = customtkinter.CTkButton(
            master=root, image=info_icon, text="Student Info", width=190, height=40, compound="left", command=self.student_details,
            cursor="hand2")
        button_1.pack(side=LEFT, pady=20, padx=20)

        # buttons
        attendance_icon = ImageTk.PhotoImage(Image.open(
            r"icons\attendance.png").resize((20, 20), Image.LANCZOS))
        # Attendance info
        button_2 = customtkinter.CTkButton(
            master=root, image=attendance_icon, text="Attendance", width=190, height=40, compound="left", cursor="hand2", command=self.attendance_data)
        button_2.pack(side=LEFT, pady=20, padx=20)

        # train face button
        train_icon = ImageTk.PhotoImage(Image.open(
            r"icons\train.png").resize((20, 20), Image.LANCZOS))
        button_3 = customtkinter.CTkButton(
            master=root, image=train_icon, text="Train Data", width=190, height=40, compound="left", cursor="hand2", command=self.train_classifier)
        button_3.pack(side=LEFT, pady=20, padx=20)

        # face recognition
        detector_icon = ImageTk.PhotoImage(Image.open(
            "icons\detector.png").resize((20, 20), Image.LANCZOS))

        button_4 = customtkinter.CTkButton(
            master=root, image=detector_icon, text="Face Detector", width=190, height=40, compound="left", fg_color="#D35B58", hover_color="#C77C78", cursor="hand2", command=self.face_data)
        button_4.pack(side=LEFT, pady=20, padx=20)

    # button function --------------------------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # greyscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Face_recog(root)
    root.mainloop()
