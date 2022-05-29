import os
import cv2
import numpy as np
from tkinter import*
from tkinter import ttk
from turtle import up, update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ..........VARIABLES...........
        self.var_Department=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_Std_Id=StringVar()
        self.var_Std_Name=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Father=StringVar()
        self.var_Phone=StringVar()
        self.var_Email=StringVar()

        # FIRST IMAGE
        img=Image.open(r"college_images\studentdet.png")
        img=img.resize((450,100))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=20,y=0,width=450,height=100)

        # SECOND IMAGE
        img1=Image.open(r"college_images\studentdet.png")
        img1=img1.resize((450,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=100)

        # THIRD IMAGE
        img2=Image.open(r"college_images\studentdet.png")
        img2=img2.resize((450,100))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=100)

        # BACKGROUNG IMAGE
        img3=Image.open(r"college_images\studentdet1.png")
        img3=img3.resize((1330,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1530,height=700)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="navyblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        # left label frame 
        Left_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        Left_frame.place(x=5,y=45,width=630,height=790) 

        img_left=Image.open(r"college_images\studentdet1.png")
        img_left=img_left.resize((620,100))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=620,height=100)

        # current course  
        current_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course",font=("times new roman",14,"bold"))
        current_frame.place(x=3,y=105,width=620,height=100)

        # DEPARTMENT
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=5,sticky=W) 

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),width=19,state="read only")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","Software","Electrical","Mechanical","Civil","Biotech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W) 

        # COURSE
        course_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=2,pady=5,sticky=W) 

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),width=19,state="read only")
        course_combo["values"]=("Select Course","B.Tech","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W) 

        # YEAR
        year_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=2,pady=5,sticky=W) 

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),width=19,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # SEMESTER
        semester_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=2,pady=5,sticky=W) 

        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_Semester,font=("times new roman",12,"bold"),width=19,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W) 

        # STUDENT INFO
        student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",14,"bold"))
        student_frame.place(x=3,y=210,width=620,height=259)

        # STUDENT ID
        studentid_label=Label(student_frame,text="Student Id:",font=("times new roman",12,"bold"))
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(student_frame,textvariable=self.var_Std_Id,width=18,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # STUDENT NAME
        studentname_label=Label(student_frame,text="Student Name:",font=("times new roman",12,"bold"))
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(student_frame,textvariable=self.var_Std_Name,width=18,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # ROLL NO
        rollno_label=Label(student_frame,text="Roll No:",font=("times new roman",12,"bold"))
        rollno_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        rollno_entry=ttk.Entry(student_frame,textvariable=self.var_Roll_No,width=18,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # GENDER
        gender_label=Label(student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),width=16,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W) 

        # DOB
        dob_label=Label(student_frame,text="DOB:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(student_frame,textvariable=self.var_DOB,width=18,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Father's Name
        father_label=Label(student_frame,text="Father's Name:",font=("times new roman",12,"bold"))
        father_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        father_entry=ttk.Entry(student_frame,textvariable=self.var_Father,width=18,font=("times new roman",12,"bold"))
        father_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Phone no
        phone_label=Label(student_frame,text="Phone No:",font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(student_frame,textvariable=self.var_Phone,width=18,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(student_frame,text="Email Id:",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(student_frame,textvariable=self.var_Email,width=18,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # radio buttons 
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=4,column=1)

        # BUTTONS
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=170,width=615,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="dark blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1) 

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="dark blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=200,width=615,height=40)

        take_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",13,"bold"),bg="dark blue",fg="white")
        take_btn.grid(row=0,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",13,"bold"),bg="dark blue",fg="white")
        updatephoto_btn.grid(row=0,column=1) 

        # Right label frame 
        # .....................SEARCH SYSTEM........................
        search_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=640,y=45,width=630,height=700)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=14,state="read only")
        search_combo["values"]=("Select","Student Id","Roll No","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W) 

        search_entry=ttk.Entry(search_frame,width=16,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        showall_btn.grid(row=0,column=4)

        # ......TABLE FRAME.......
        table_frame=LabelFrame(search_frame,bd=2,relief=RIDGE)
        table_frame.place(x=3,y=40,width=620,height=430)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","Student Id","Student Name","Roll No","Gender","DOB","Father's Name","Phone No","Email Id","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student Id",text="Student Id")
        self.student_table.heading("Student Name",text="Name")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Father's Name",text="Father's Name")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Email Id",text="Email Id")
        self.student_table.heading("Photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100) 
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student Id",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Father's Name",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Email Id",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ..........FUNCTION DECLARATION...........
    # ..........SAVE ADD.................
    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Std_Name.get()=="" or self.var_Std_Id.get()=="":
            messagebox.showerror("Error","All Fields are Mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_Department.get(),
                                                                                                            self.var_Course.get(),
                                                                                                            self.var_Year.get(),
                                                                                                            self.var_Semester.get(),
                                                                                                            self.var_Std_Id.get(),
                                                                                                            self.var_Std_Name.get(),
                                                                                                            self.var_Roll_No.get(),
                                                                                                            self.var_Gender.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_Father.get(),
                                                                                                            self.var_Phone.get(),
                                                                                                            self.var_Email.get(),
                                                                                                            self.var_radio1.get()
                                                                                                        
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details added successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # ............FETCH data.............
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ............cursor..............
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Std_Id.set(data[4]),
        self.var_Std_Name.set(data[5]),
        self.var_Roll_No.set(data[6]),
        self.var_Gender.set(data[7]),
        self.var_DOB.set(data[8]),
        self.var_Father.set(data[9]),
        self.var_Phone.set(data[10]),
        self.var_Email.set(data[11]),
        self.var_radio1.set(data[12]) 

    # ............UPDATE...........
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Std_Name.get()=="" or self.var_Std_Id.get()=="":
            messagebox.showerror("Error","All Fields are Mandatory",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this particular record",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,DOB=%s,Father=%s,Phone=%s,Email=%s,PhotoSample=%s where Student_Id=%s",(
                                                                                                                                                                                                                            self.var_Department.get(),
                                                                                                                                                                                                                            self.var_Course.get(),
                                                                                                                                                                                                                            self.var_Year.get(),
                                                                                                                                                                                                                            self.var_Semester.get(),
                                                                                                                                                                                                                            self.var_Std_Name.get(),
                                                                                                                                                                                                                            self.var_Roll_No.get(),
                                                                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                                                            self.var_Father.get(),
                                                                                                                                                                                                                            self.var_Phone.get(),
                                                                                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_Std_Id.get()
                                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # ............DELETE............
    def delete_data(self):
        if self.var_Std_Id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this particular record",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_Std_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # ............RESET..............
    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Std_Id.set("")
        self.var_Std_Name.set("")
        self.var_Roll_No.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_Father.set("")
        self.var_Phone.set("")
        self.var_Email.set("")
        self.var_radio1.set("")

    #..........generate dataset or take photo samples...............
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Std_Name.get()=="" or self.var_Std_Id.get()=="":
            messagebox.showerror("Error","All Fields are Mandatory",parent=self.root)

        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,DOB=%s,Father=%s,Phone=%s,Email=%s,PhotoSample=%s where Student_Id=%s",(
                                                                                                                                                                                                        self.var_Department.get(),
                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                        self.var_Year.get(),
                                                                                                                                                                                                        self.var_Semester.get(),
                                                                                                                                                                                                        self.var_Std_Name.get(),
                                                                                                                                                                                                        self.var_Roll_No.get(),
                                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                                        self.var_DOB.get(),
                                                                                                                                                                                                        self.var_Father.get(),
                                                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                                                        self.var_Email.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_Std_Id.get()==id+1
                                                                                                                                                                                                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #............load predefined data on face frontals from opencv............
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
                

                # faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5) # <- face is detected here 

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()# captures frame and returns boolean value and captured image
                    if not ret:
                        continue 
                    
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data sets completed")
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__" :
    root=Tk()
    obj=Student(root) 
    root.mainloop()                 
