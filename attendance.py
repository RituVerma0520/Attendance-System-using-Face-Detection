from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np  
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_attendance = StringVar()

        # BACKGROUNG IMAGE
        img3=Image.open(r"college_images\trainimg.png")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=55,width=1530,height=710)

        title_lbl=Label(self.root,text="ATTENDANCE RECORD",font=("times new roman",38,"bold"),bg="navyblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        # LEFT FRAME 
        Left_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=30,y=10,width=630,height=710) 

        img_left=Image.open(r"college_images\attendance.png")
        img_left=img_left.resize((620,150))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=620,height=150)

        img1_left=Image.open(r"college_images\att1.png")
        img1_left=img1_left.resize((620,280))
        self.photoimg1_left=ImageTk.PhotoImage(img1_left)

        f_lbl=Label(Left_frame,image=self.photoimg1_left)
        f_lbl.place(x=3,y=345,width=620,height=280)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=2, y=150, width=622, height=245)

        #Label and entry
        #attendance id
        attendanceId_label=Label(left_inside_frame,text="Sudent Id:",font=("times new roman", 13, "bold"))
        attendanceId_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        #roll
        rollLabel = Label(left_inside_frame, text="Roll No.:", font=("times new roman", 13, "bold"))
        rollLabel.grid(row=0, column=2, padx=12, pady=15,sticky=W)

        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll ,width=20,font=("times new roman", 12, "bold"))
        atten_roll.grid(row=0, column=3,padx=5,pady=15,sticky=W)

        # name
        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"))
        nameLabel.grid(row=1, column=0,padx=10,pady=10,sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name ,font=("times new roman", 12, "bold"))
        atten_name.grid(row=1, column=1,padx=5,pady=10,sticky=W)

        # department
        depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"))
        depLabel.grid(row=1, column=2,padx=12,pady=10,sticky=W)

        atten_dep = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep ,width=20,font=("times new roman", 12, "bold"))
        atten_dep.grid(row=1, column=3, padx=5,pady=10,sticky=W)

        #time
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"))
        timeLabel.grid(row=2, column=0,padx=10,pady=10,sticky=W)

        atten_time = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time , width=20,font=("times new roman", 12, "bold"))
        atten_time.grid(row=2, column=1, padx=5,pady=10,sticky=W)

        #date
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"))
        dateLabel.grid(row=2, column=2, padx=12,pady=10,sticky=W)

        atten_date = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date ,width=20,font=("times new roman", 12, "bold"))
        atten_date.grid(row=2, column=3, padx=5,pady=10,sticky=W)

        #attendance
        attendanceLabel = Label(left_inside_frame, text="Status:", font=("times new roman", 13, "bold"))
        attendanceLabel.grid(row=3, column=0,padx=10,pady=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, width=16, font="comicsansns 12 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=5,pady=10,sticky=W)
        self.atten_status.current(0)

        #buttonframe
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=205,width=710,height=35)

        importcsv=Button(btn_frame,text="Import Csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        importcsv.grid(row=0,column=0)

        exportcsv = Button(btn_frame, text="Export Csv",command=self.exportCsv, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        exportcsv.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        # right label frame
        Right_frame = LabelFrame(bg_img, bd=2, relief=RIDGE, text="Attendance Details",font=("times new roman", 15, "bold"))
        Right_frame.place(x=680, y=10, width=630, height=710)

        # ......TABLE FRAME.......
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=4, y=5, width=620, height=580)

        #.......SCROLL BAR.......
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance", text="Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global  mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", ".csv"),("ALL File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimete=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
