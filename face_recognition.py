from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import cv2.face
from time import strftime, time
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recogntion")

        # set the windows size to 640 * 1080
        self.root.geometry("640x1080+0+0")

        # background image
        bgimg = Image.open(r"images\recog.jpg")

        bgimg = bgimg.resize((640, 1080))
        self.photbgimg = ImageTk.PhotoImage(bgimg)

        label1 = Label(self.root, image=self.photbgimg)
        label1.place(x=0, y=0, relheight=1, relwidth=1)

        # button
        info_icon = ImageTk.PhotoImage(Image.open(
            r"images\Scanning.png").resize((20, 20), Image.LANCZOS))
        button_1 = customtkinter.CTkButton(
            master=root, image=info_icon, text="Facial Recognition", width=190, height=40, compound="left", command=self.face_recog,
            cursor="hand2", fg_color="#D35B58", hover_color="#C77C78")
        button_1.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.last_attendance_time = {}

    # -------------attendance--------------

    def mark_attendance(self, i, r, n, d, year):
        filename = f"attendance{year}.csv"
        current_time = time()

        # check if the person is already present
        if i in self.last_attendance_time:
            last_attendance_time = self.last_attendance_time[i]
            if current_time - last_attendance_time >= 60:  # check if 60 secs have passed
                self.write_attendance(
                    filename, i, r, n, d, year, current_time)
        else:
            self.write_attendance(filename, i, r, n, d, year, current_time)

    def write_attendance(self, filename, i, r, n, d, year, current_time):
        try:
            with open(filename, "r+", newline="\n", encoding="utf-8") as f:
                myDataList = f.readlines()
                name_list = []
                for line in myDataList:
                    entry = line.split(",")
                    name_list.append(entry[0])
                if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    f.writelines(
                        f"\n{i} {r} {n} {d} {dtString}, {d1},Present")
                    self.last_attendance_time[i] = current_time
        except FileNotFoundError:
            with open(filename, "w", newline="\n", encoding="utf-8") as f:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i} {r} {n} {d} {dtString}, {d1}, Present\n")
                self.last_attendance_time[i] = current_time

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_img, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y:y+h, x:x+h])
                confidence = int(100*(1-predict/300))
                print("predict="+str(predict)+"confidence=" + str(confidence))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Rajni@kanth,786", database="tate")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select year from student where sid=" + str(id))
                year = my_cursor.fetchone()

                year = "".join(str(year))

                # roll_no ki Student_id?
                my_cursor.execute(
                    "select name from student where sid="+str(id))
                n = my_cursor.fetchone()
                n = "".join(str(n))

                # roll_no ki Student_id?
                my_cursor.execute(
                    "select roll_no from student where sid="+str(id))
                r = my_cursor.fetchone()
                r = "".join(str(r))

                # roll_no ki Student_id?
                my_cursor.execute("select Dep from student where sid="+str(id))
                d = my_cursor.fetchone()
                d = "".join(str(d))

                # roll_no ki Student_id?
                my_cursor.execute("select sid from student where sid="+str(id))
                i = my_cursor.fetchone()
                i = "".join(str(i))

                i = str(i).replace("(", "").replace(
                    ")", "").replace("'", "").strip()
                r = str(r).replace("(", "").replace(
                    ")", "").replace("'", "").strip()
                n = str(n).replace("(", "").replace(
                    ")", "").replace("'", "").strip()
                d = str(d).replace("(", "").replace(
                    ")", "").replace("'", "").strip()
                year = year.strip("()\"',")

                if confidence > 70:
                    #     if not last_marked_time or (datetime.now() - last_marked_time).seconds>60:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d, year)
                    # last_marked_time = datetime.now()
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return (img)

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        # clf = cv2.LBPHFaceRecognizer_create()
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
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
