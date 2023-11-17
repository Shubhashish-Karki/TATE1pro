from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Setting window size
        self.root.title("Student details")  # Name of window


        #variables to add in database
        self.var_dep=StringVar()
        self.dep_var = StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.year_var = StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()


        # Background image
        img1 = Image.open(r"C:\Users\shubh\OneDrive\Desktop\TATE\images\student.jpg")
        img1 = img1.resize((1700, 1000))
        self.photimg1 = ImageTk.PhotoImage(img1)

        lbl_1 = Label(self.root, image=self.photimg1)
        lbl_1.place(x=0, y=0, width=1700, height=1000)

        # Font in image
        title_lbl = Label(lbl_1, text="Student Details", font=("Arial", 42, "bold"), bg="gold", fg="green")
        title_lbl.place(x=0, y=20, width=1530, height=45)

        main_frame = Frame(lbl_1, bd=2, bg="gold")
        main_frame.place(x=20, y=84, width=1500, height=700)

        # Left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Info", font=("arial", 15, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=650)

        leftimg1 = Image.open(r"C:\Users\shubh\OneDrive\Desktop\TATE\images\leftimg1.jpg")
        leftimg1 = leftimg1.resize((700, 130))
        self.photimg_left = ImageTk.PhotoImage(leftimg1)

        lbl_left = Label(Left_frame, image=self.photimg_left)
        lbl_left.place(x=10, y=0, width=680, height=170)

        # Course frame----------------------------------------------------------------
        course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Course", font=("arial", 15, "bold"))
        course_frame.place(x=10, y=175, width=680, height=120)

        dep_label = Label(course_frame, text="Department", font=("arial", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        # Create a StringVar for department
        #department combobox
        
        self.dep_var.set("Select Department")
        
        dep_combobox = ttk.Combobox(course_frame,font=("arial", 12, "bold"), textvariable=self.dep_var, state="readonly")
        dep_combobox["values"] = ("Select Department", "DoCSE", "DoEE", "Mechanical", "Environmental", "Pharmacy", "Architecture")
        dep_combobox.grid(row=0, column=1, padx=2, pady=10)

        year_label = Label(course_frame, text="Year", font=("arial", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        # Create a StringVar for year
        #year combobox
        
        self.year_var.set("Select Year")
        
        year_combobox = ttk.Combobox(course_frame,font=("arial", 12, "bold"), textvariable=self.year_var, state="readonly")
        year_combobox["values"] = ("Select Year", "1", "2", "3", "4")
        year_combobox.grid(row=1, column=1, padx=2, pady=10)

        def on_department_change(*args):
            selected_department = self.dep_var.get()
            selected_year = self.year_var.get()
            
            if selected_department == "Select Department" or selected_year == "Select Year":
                course_combobox["values"] = ("Select Course",)
                course_combobox.current(0)
            else:
                #course update later
                course_options = {
                    ("DoCSE", "1"): ("Select Course", "CSE Course 1", "CSE Course 2"),
                    ("DoCSE", "2"): ("Select Course", "CSE Course 3", "CSE Course 4"),
                    ("DoEE", "1"): ("Select Course", "EE Course 1", "EE Course 2"),
                    ("DoEE", "2"): ("Select Course", "EE Course 3", "EE Course 4"),
                }
                
                selected_options = course_options.get((selected_department, selected_year), ("Select Course",))
                course_combobox["values"] = selected_options
                course_combobox.current(0)

        def on_year_change(*args):
            on_department_change()

        self.dep_var.trace("w", on_department_change)
        self.year_var.trace("w", on_year_change)

        #course combobox
        course_label = Label(course_frame, text="Course", font=("arial", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combobox = ttk.Combobox(course_frame, textvariable=self.var_course,font=("arial", 12, "bold"), state="readonly")
        course_combobox["values"] = ("Select Course",)
        course_combobox.grid(row=0, column=3, padx=2, pady=10)


        #Student information frame--------------------------------------------------------
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student details", font=("arial", 15, "bold"))
        student_frame.place(x=10, y=320, width=680, height=250)
        
        #for name
        name_label = Label(student_frame, text="Name", font=("arial", 12, "bold"), bg="white")
        name_label.grid(row=0, column=0, padx=10, sticky=W)

        name_entry=ttk.Entry(student_frame,textvariable=self.var_name,width=20,font=("arial", 12, "bold"))
        name_entry.grid(row=0, column=1, padx=10, sticky=W)

        #for roll no
        roll_label = Label(student_frame, text="Roll no", font=("arial", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, sticky=W)

        roll_entry=ttk.Entry(student_frame,textvariable=self.var_rollno,width=20,font=("arial", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, sticky=W)

        #photo sample
        self.var_rad1=StringVar()
        radio_btn1=ttk.Radiobutton(student_frame,text="Take photo samle", variable=self.var_rad1, value="Yes")
        radio_btn1.grid(row=2, column=0)

        
        radio_btn2=ttk.Radiobutton(student_frame,text="No photo samle", variable=self.var_rad1, value="No")
        radio_btn2.grid(row=2, column=1)

        #button frame
        btn_frame=Frame(student_frame, bd=2, relief=RIDGE, bg = "white")
        btn_frame.place(x=0,y=100,width =675, height= 120)

        #save
        save= Button(btn_frame,command=self.add,text="Save",width=15,font=("arial",12,"bold"),bg="green",fg="white",)
        save.grid(row=1,column=1,padx=2)
        #update
        update= Button(btn_frame,command=self.update,text="Update",width=15,font=("arial",12,"bold"),bg="blue",fg="white")
        update.grid(row=1,column=3,padx=2)
        #delete,
        delete= Button(btn_frame,command=self.delete,text="Delete",width=15,font=("arial",12,"bold"),bg="red",fg="white")
        delete.grid(row=1,column=5,padx=2)

        #take photo,
        take= Button(btn_frame,command=self.gen_dataset,text="Take Photo",width=15,font=("arial",12,"bold"),bg="gold",fg="green")
        take.grid(row=2,column=1,padx=2)

        #update photo
        update_photo= Button(btn_frame,text="Update Photo",width=15,font=("arial",12,"bold"),bg="gold",fg="green")
        update_photo.grid(row=2,column=3,padx=2)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Info", font=("arial", 15, "bold"))
        Right_frame.place(x=770, y=10, width=720, height=650)

        rightimg1 = Image.open(r"C:\Users\shubh\OneDrive\Desktop\TATE\images\rightimg1.jpg")
        rightimg1 = rightimg1.resize((700, 130))
        self.photoimg_right = ImageTk.PhotoImage(rightimg1)

        lbl_right = Label(Right_frame, image=self.photoimg_right)
        lbl_right.place(x=10, y=0, width=680, height=170)

        #search student details frame
        search_frame = LabelFrame(Right_frame, bg="white",relief=RIDGE,text="Search", font=("arial", 15, "bold"))
        search_frame.place(x=5,y=135, width= 710, height=70,)

        search_label = Label(search_frame,text="Search by", font=("arial", 12, "bold"),bg="red")
        search_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

        search_combobox = ttk.Combobox(search_frame, font=("arial", 10, "bold"), state="readonly")
        search_combobox["values"] = ("Select","Year","Department","Roll no","Name")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=2, pady=10)

        search_entry=ttk.Entry(search_frame,width=15,font=("arial", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn= Button(search_frame,text="Search",width=10,font=("arial",12,"bold"),bg="blue",fg="white",)
        search_btn.grid(row=0,column=3,padx=2)

        show_btn= Button(search_frame,text="Show All",width=10,font=("arial",12,"bold"),bg="blue",fg="white",)
        show_btn.grid(row=0,column=4,padx=2)

        #student database 
        table_frame = Frame(Right_frame, bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220, width= 710, height=350,)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.table=ttk.Treeview(table_frame,column=("dep","course","year","name","roll no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
       
        scroll_x.configure(command=self.table.xview)
        scroll_y.configure(command=self.table.yview)

       

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.table.heading("dep",text="Department")
        self.table.heading("course",text="Course")
        self.table.heading("year",text="Year")
        self.table.heading("name",text="Name")
        self.table.heading("roll no",text="Roll No")
        self.table.heading("photo",text="Photo status")
        self.table["show"] = "headings"

        #setting width of headings
        self.table.column("dep",width=100)
        self.table.column("course",width=100)
        self.table.column("year",width=100)
        self.table.column("name",width=100)
        self.table.column("roll no",width=100)
        self.table.column("photo",width=100)



        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch()

    #function to add in database--------------------

    def add(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="!@#mySQL123",database="tate")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.dep_var.get(),
                                                                                self.var_course.get(),
                                                                                self.year_var.get(),
                                                                                self.var_name.get(),
                                                                                self.var_rollno.get(),
                                                                                self.var_rad1.get(),
                                                                        ))
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo("Success","Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
    #function to fetch data:
    def fetch(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="!@#mySQL123",database="tate")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #function to get cursor i.e. get values in entry field to make update easy:
    def get_cursor(self,event=""):
        cursor_focus=self.table.focus()
        content=self.table.item(cursor_focus)
        data=content["values"]

        self.dep_var.set(data[0])
        self.var_course.set(data[1])
        self.year_var.set(data[2])
        self.var_name.set(data[3])
        self.var_rollno.set(data[4])
        self.var_rad1.set(data[5])

    #function to update info:
    def update(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure you want to update?",parent=self.root)
                if update>0:

                    conn=mysql.connector.connect(host="localhost",username="root",password="!@#mySQL123",database="tate")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,name=%s,photo=%s where roll_no =%s",(
                                                                                self.dep_var.get(),
                                                                                self.var_course.get(),
                                                                                self.year_var.get(),
                                                                                self.var_name.get(),       
                                                                                self.var_rad1.get(),  
                                                                                self.var_rollno.get()
                                                                                                                                                    
                    ))
                    conn.commit()
                    self.fetch()
                    conn.close()
                else:
                    if not update:
                        return 
                messagebox.showinfo("Success","Update successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
               

    #function to delete:
    def delete(self):
        if self.var_rollno=="":
            messagebox.showerror("Error","Roll no is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if delete>0:

                    conn=mysql.connector.connect(host="localhost",username="root",password="!@#mySQL123",database="tate")
                    my_cursor=conn.cursor()
                    my_cursor.execute("delete  from student where roll_no =%s",(self.var_rollno.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo("Delete","Deleted succesfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #  take photo sample----------------------------------------------------------------

    def gen_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="!@#mySQL123",database="tate")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                result=my_cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,name=%s,photo=%s where roll_no =%s",(
                                                                                self.dep_var.get(),
                                                                                self.var_course.get(),
                                                                                self.year_var.get(),
                                                                                self.var_name.get(),       
                                                                                self.var_rad1.get(),  
                                                                                self.var_rollno.get()==id+1
                                                                                                                                                    
                ))
                conn.commit()
                self.fetch()
                conn.close()

                #loading algorithm face frontal for opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray_scale,1.3,5) #scaling factor=1.3 min neighborhood=5
                    
                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                    
                cap = cv2.VideoCapture(1)
    

                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face= cv2.resize(face_crop(my_frame),(450,450))
                        face= cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)    #font size during cam
                        cv2.imshow("TATE",face)

                    if cv2.waitKey(1) == 13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!",parent=self.root)
        
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

if __name__ == "__main__": 
    root = Tk()
    obj = Student(root)
    root.mainloop()
