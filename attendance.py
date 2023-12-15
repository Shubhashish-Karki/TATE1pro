from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                           root.winfo_screenheight()))  # setting window size
        self.root.title("Attendance")

        # ---------variables----------
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        # self.var_atten_year=StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Background image
        img1 = Image.open(r"images\student.jpg")
        img1 = img1.resize((1700, 1000))
        self.photimg1 = ImageTk.PhotoImage(img1)

        lbl_1 = Label(self.root, image=self.photimg1)
        lbl_1.place(x=0, y=0, width=1700, height=1000)

        # Font in image
        title_lbl = Label(lbl_1, text="Attendance Details", font=(
            "Arial", 42, "bold"), bg="gold", fg="green")
        title_lbl.place(x=0, y=20, width=1530, height=45)

        main_frame = Frame(lbl_1, bd=2, bg="gold")
        main_frame.place(x=20, y=84, width=1500, height=700)

        # Left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Attendance Info", font=("arial", 15, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=650)

        leftimg1 = Image.open(r"images\leftimg1.jpg")
        leftimg1 = leftimg1.resize((700, 130))
        self.photimg_left = ImageTk.PhotoImage(leftimg1)

        lbl_left = Label(Left_frame, image=self.photimg_left)
        lbl_left.place(x=10, y=0, width=680, height=170)

        Left_table_frame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        Left_table_frame.place(x=5, y=170, width=710, height=400)

        # for id
        id_label = Label(Left_table_frame, text="Attendance Id",
                         font=("arial", 12, "bold"), bg="white")
        id_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        id_entry = ttk.Entry(
            Left_table_frame, textvariable=self.var_atten_id, width=20, font=("arial", 12, "bold"))
        id_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        # for name
        name_label = Label(Left_table_frame, text="Name",
                           font=("arial", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        name_entry = ttk.Entry(
            Left_table_frame, textvariable=self.var_atten_name, width=20, font=("arial", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # for roll no
        roll_label = Label(Left_table_frame, text="Roll no",
                           font=("arial", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        roll_entry = ttk.Entry(
            Left_table_frame, textvariable=self.var_atten_roll, width=20, font=("arial", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        depart_label = Label(Left_table_frame, text="Department", font=(
            "arial", 12, "bold"), bg="white")
        depart_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        depart_entry = ttk.Entry(
            Left_table_frame, textvariable=self.var_atten_dep, width=20, font=("arial", 12, "bold"))
        depart_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # year_entry=ttk.Entry(Left_table_frame,textvariable=self.var_atten_year,width=20,font=("arial", 12, "bold"))
        # year_entry.grid(row=1, column=3, padx=10, pady=10 ,sticky=W)
        # year_entry=ttk.Entry(Left_table_frame,textvariable=self.var_atten_year,width=20,font=("arial", 12, "bold"))
        # year_entry.grid(row=1, column=3, padx=10, pady=10 ,sticky=W)

        time_label = Label(Left_table_frame, text="Time",
                           font=("arial", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        time_entry = ttk.Entry(
            Left_table_frame, textvariable=self.var_atten_time, width=20, font=("arial", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        date_label = Label(Left_table_frame, text="Date",
                           font=("arial", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        date_entry = ttk.Entry(
            Left_table_frame, textvariable=self.var_atten_date, width=20, font=("arial", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # attendance
        attendanceLabel = Label(
            Left_table_frame, text="Attendance Status", bg="white", font=("arial", 12, "bold"))
        attendanceLabel.grid(row=3, column=0, padx=10)
        self.atten_status = ttk.Combobox(
            Left_table_frame, textvariable=self.var_atten_attendance, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=10)
        self.atten_status.current(0)

        # button frame
        btn_frame = Frame(Left_table_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=675, height=120)

        #    Import csv
        save = Button(btn_frame, text="Import csv", command=self.importCsv,
                      width=15, font=("arial", 12, "bold"), bg="green", fg="white",)
        save.grid(row=0, column=0, padx=2)
        # Export csv
        update = Button(btn_frame, text="Export csv", command=self.exportCsv,
                        width=15, font=("arial", 12, "bold"), bg="blue", fg="white")
        update.grid(row=0, column=1, padx=2)

        # update csv
        delete = Button(btn_frame, text="Update", width=15, font=(
            "arial", 12, "bold"), bg="red", fg="white")
        delete.grid(row=0, column=2, padx=2)

        reset = Button(btn_frame, text="Reset", width=15, command=self.reset_data, font=(
            "arial", 12, "bold"), bg="red", fg="white")
        reset.grid(row=0, column=3, padx=2)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Info", font=("arial", 15, "bold"))
        Right_frame.place(x=720, y=10, width=720, height=650)

        rightimg1 = Image.open(r"images\rightimg1.jpg")
        rightimg1 = rightimg1.resize((700, 130))
        self.photoimg_right = ImageTk.PhotoImage(rightimg1)

        lbl_right = Label(Right_frame, image=self.photoimg_right)
        lbl_right.place(x=10, y=0, width=680, height=200)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=220, width=710, height=350)

        # ---------=scroll bar table======---------
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "Id", "RollNo", "Name", "Department", "time", "date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("Id", text="Attendance ID")
        self.AttendanceReportTable.heading("RollNo", text="Roll")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        # self.AttendanceReportTable.heading("Year", text="Year")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.heading("Id", text="Attendance ID")
        self.AttendanceReportTable.column("RollNo", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self. AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export cSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export", "Your data exported to"+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        # self.var_atten_year.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        # self.var_atten_year.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
