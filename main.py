from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from emotion import Emotion
from student import Student
import os
from tkinter import Toplevel
from attendance import Attendance
from query import Query
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # FIRST IMAGE
        img1=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\college.jpg")
        img1=img1.resize((450,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=20,y=0,width=450,height=100)

        # SECOND IMAGE
        img2=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\college.jpg")
        img2=img2.resize((450,100))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=100)

        # THIRD IMAGE
        img3=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\college.jpg")
        img3=img3.resize((450,100))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=900,y=0,width=450,height=100)

        # BACKGROUNG IMAGE
        img4=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\trainimg.png")
        img4=img4.resize((1330,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION BASED ATTENDANCE SYSTEM", font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=30,y=0,width=1300,height=40)


        # STUDENT BUTTON
        img4=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\student.png")
        img4=img4.resize((180,180))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=75,width=180,height=180)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=100,y=230,width=180,height=25) 


        # TRAIN DATA BUTTON
        img5=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\traindata.png")
        img5=img5.resize((180,180))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b1.place(x=400,y=75,width=180,height=180)

        b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=400,y=230,width=180,height=25) 


        # DETECT FACE BUTTON
        img6=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\facedet.png")
        img6=img6.resize((180,180))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=700,y=75,width=180,height=180)

        b1_1=Button(bg_img,text="FACE IDENTIFICATION",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=700,y=230,width=180,height=25) 


        # ATTENDANCE BUTTON
        img7=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\atten.png")
        img7=img7.resize((180,180))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=1000,y=75,width=180,height=180)

        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=1000,y=230,width=180,height=25)


        # PHOTOS BUTTON
        img8=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\photos.png")
        img8=img8.resize((180,180))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=100,y=310,width=180,height=180)

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=100,y=480,width=180,height=25)


        # QUERY BUTTON
        img9=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\query.png")
        img9=img9.resize((180,180))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.query_data)
        b1.place(x=400,y=310,width=180,height=180)

        b1_1=Button(bg_img,text="QUERY",cursor="hand2",command=self.query_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=400,y=480,width=180,height=25)


        # FEEDBACK BUTTON    
        img10=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\feedback.png")
        img10=img10.resize((180,180))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.emotion_data)
        b1.place(x=700,y=310,width=180,height=180)

        b1_1=Button(bg_img,text="FEEDBACK",cursor="hand2",command=self.emotion_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=700,y=480,width=180,height=25)


        # EXIT BUTTON
        img11=Image.open(r"C:\Users\dell\OneDrive\Desktop\Face Recognition\college_images\exit.png")
        img11=img11.resize((180,180))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=310,width=180,height=180)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="black",fg="white")
        b1_1.place(x=1000,y=480,width=180,height=25)

    def open_img(self):
        os.startfile("data")

    # ..........FUNCTION BUTTONS..........

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def query_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Query(self.new_window)

    def emotion_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Emotion(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    
    
if __name__ == "__main__" :
    root=Tk()
    obj=Face_Recognition_System(root) 
    root.mainloop() 