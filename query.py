import os
import cv2
import numpy as np
from tkinter import*
from tkinter import ttk
from turtle import left, up, update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Query:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Queries")

        #variable
        self.var_Std_Name=StringVar()
        self.var_query=StringVar()
        self.var_id=StringVar()
        self.var_ans=StringVar()

        title_lbl=Label(self.root,text="Ask Your Doubt",font=("times new roman",38,"bold"),bg="navyblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        img=Image.open(r"college_images\lightblue.png")
        img=img.resize((1530,790))
        self.photoimg_top=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=0,y=50,width=1530,height=790)


        # ...........TABLE FRAME............
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE)
        table_frame.place(x=135,y=210,width=1030,height=435)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Query_id","Name","Query","Answer"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Query_id",text="Query Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Query",text="Doubt")
        self.student_table.heading("Answer",text="Answer")
        self.student_table["show"]="headings"

        self.student_table.column("Query_id",width=80)
        self.student_table.column("Name",width=100) 
        self.student_table.column("Query",width=400)
        self.student_table.column("Answer",width=400)

        self.student_table.pack(fill=BOTH,expand=1)


        # LEFT FRAME 
        Left_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg="lightblue")
        Left_frame.place(x=300,y=55,width=700,height=153) 

        queryid_label=Label(Left_frame,text="Query Id:",font=("times new roman",13,"bold"))
        queryid_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        queryid_entry=ttk.Entry(Left_frame,textvariable=self.var_id,width=18,font=("times new roman",13,"bold"),state="readonly")
        queryid_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        studentname_label=Label(Left_frame,text="Student Name:",font=("times new roman",13,"bold"))
        studentname_label.grid(row=1,column=2,padx=6,pady=10,sticky=W)

        studentname_entry=ttk.Entry(Left_frame,textvariable=self.var_Std_Name,width=18,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=3,padx=6,pady=10,sticky=W)

        query_label=Label(Left_frame,text="Any Question??",font=("times new roman",13,"bold"))
        query_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        query_entry=ttk.Entry(Left_frame,textvariable=self.var_query,width=22,font=("times new roman",13,"bold"))
        query_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        answer_label=Label(Left_frame,text="Answer:",font=("times new roman",13,"bold"))
        answer_label.grid(row=2,column=2,padx=6,pady=10,sticky=W)

        answer_entry=ttk.Entry(Left_frame,textvariable=self.var_ans,width=22,font=("times new roman",13,"bold"))
        answer_entry.grid(row=2,column=3,padx=6,pady=10,sticky=W)

        sendbutton = Button(Left_frame,font=("times new roman",15,"bold"), bg='midnight blue', fg='white', text='SEND QUERY', command=self.send)
        sendbutton.grid(row=3,column=1,padx=6,pady=10,sticky=W)

        ansbutton = Button(Left_frame,font=("times new roman",15,"bold"), bg='midnightblue', fg='white', text='ANSWER', command=self.get_answer)
        ansbutton.grid(row=3,column=2,padx=13,pady=10,sticky=W)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.update()


    
    def update(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from query")
        data=my_cursor.fetchall()

        if len(data)!=0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_id.set((data[0]))
        self.var_Std_Name.set(data[1])
        self.var_query.set(data[2])
        self.var_ans.set(data[3])

    def get_answer(self):
        if self.var_id.get()=="" or self.var_Std_Name.get()=="" or self.var_query.get()=="" or self.var_ans.get()=="":
            messagebox.showerror("Error","All Fields are Mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                my_cursor=conn.cursor()
                # qid=int(self.var_id.get())
                # my_cursor.execute("Update query set Answer={self.var_ans.get()} where Query_id={qid}")
                my_cursor.execute("Update query set Answer=%s where Query_id=%s",(
                                                                                    self.var_ans.get(),
                                                                                    self.var_id.get()
                                                                                ))
                
                messagebox.showinfo("Success","Answered successfully",parent=self.root)
                conn.commit()
                self.update()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    def send(self):
        if self.var_Std_Name.get()=="" or self.var_query.get()=="":
            messagebox.showerror("Error"," Name & Query is mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into query(Name,Query) values(%s,%s)",(self.var_Std_Name.get(),self.var_query.get()))
                                                                                                           
                conn.commit()
                
                conn.close()
                messagebox.showinfo("Status of you Query!!","Sent",parent=self.root)
                self.update()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

if __name__ == "__main__" :
    root=Tk()
    obj=Query(root) 
    root.mainloop()  
