import os
from string import whitespace
from xml import dom
import cv2
import numpy as np
from tkinter import*
from tkinter import ttk
from turtle import up, update
from PIL import Image,ImageTk
from tkinter import messagebox
from deepface import DeepFace
import matplotlib.pyplot as plt
import mysql.connector

class Emotion:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Feedback")

        title_lbl=Label(self.root,text="FEEDBACK",font=("times new roman",38,"bold"),bg="navyblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        img=Image.open(r"college_images\feedbackbg.png")
        img=img.resize((1300,300))
        self.photoimg_top=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=20,y=55,width=1300,height=300)

        img1=Image.open(r"college_images\fb.png")
        img1=img1.resize((1300,300))
        self.photoimg1_top=ImageTk.PhotoImage(img1)

        bg_img1=Label(self.root,image=self.photoimg1_top)
        bg_img1.place(x=20,y=450,width=1300,height=300)

        capture_emotion=Button(self.root,text="Record Feedback",command=self.get_Emotion,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        capture_emotion.place(x=500,y=560,width=300,height=60)

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE)
        table_frame.place(x=60,y=235,width=1160,height=310)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Feedback_id","Dominant_emotion","Feedback_score","Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Feedback_id",text="Feedback Id")
        self.student_table.heading("Dominant_emotion",text="Dominant Emotion")
        self.student_table.heading("Feedback_score",text="Feedback Score")
        self.student_table.heading("Angry",text="Angry")
        self.student_table.heading("Disgust",text="Disgust")
        self.student_table.heading("Fear",text="Fear")
        self.student_table.heading("Happy",text="Happy")
        self.student_table.heading("Sad",text="Sad")
        self.student_table.heading("Surprise",text="Surprise")
        self.student_table.heading("Neutral",text="Neutral")
        self.student_table["show"]="headings"

        self.student_table.column("Feedback_id",width=85)
        self.student_table.column("Dominant_emotion",width=115)
        self.student_table.column("Feedback_score",width=95)
        self.student_table.column("Angry",width=120) 
        self.student_table.column("Disgust",width=120)
        self.student_table.column("Fear",width=120)
        self.student_table.column("Happy",width=120)
        self.student_table.column("Sad",width=120)
        self.student_table.column("Surprise",width=120)
        self.student_table.column("Neutral",width=120)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        #self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from emotion")
        data=my_cursor.fetchall()

        if len(data)!=0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        
    def getGraph(self):
        mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="Test@123",
                               database="face_recognition")
        mycursor = mydb.cursor()
        mycursor.execute("select Dominant_emotion,Feedback_score,count(Feedback_score) from emotion group by Feedback_score order by count(Feedback_score) asc,Feedback_score asc")
        result = mycursor.fetchall

        number = []
        feedback = []
        dominant=[]
    
        for i in mycursor:
            number.append(i[2])
            feedback.append(i[1])
            dominant.append(i[0])
        
        plt.bar(feedback,number,align="center", alpha=0.5, color=["k", "r", "g", "m", "b", "c", "y"])
        # plt.ylim(0, 2)
        plt.ylim(bottom=0)
        for i in range(len(dominant)):
            plt.annotate(str(dominant[i]), xy=(feedback[i],number[i]), ha='center', va='bottom')
        plt.xlabel("Feedback Score")
        plt.ylabel("No of Students")
        plt.title("FEEDBACK")
        plt.show()

    
    
    def get_Emotion(self):
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        return_value, image = camera.read()
        if return_value:
            cv2.imwrite(r'opencv.jpg', image)
            del(camera)
            img1=cv2.imread(r'opencv.jpg')

            try:
                result=DeepFace.analyze(img1,actions=['emotion'])
                print(result['dominant_emotion'])
                print(result)
                #to draw box on faces

                facecascasde=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
                gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
                faces=facecascasde.detectMultiScale(gray,1.1,4)
                for(x,y,w,h) in faces:
                    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)

                #plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
                #plt.show()

                #to write on image
                font=cv2.FONT_HERSHEY_COMPLEX

                cv2.putText(img1,result['dominant_emotion'],(0,50),font,1,(0,0,255),2,cv2.LINE_4)

                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognition")
                my_cursor=conn.cursor()
                
                f=0
                ang=str(result["emotion"]['angry'])
                dis=str(result["emotion"]["disgust"])
                fear=str(result["emotion"]['fear'])
                hap=str(result["emotion"]['happy'])
                sad=str(result["emotion"]['sad'])
                sur=str(result["emotion"]['surprise'])
                neu=str(result["emotion"]['neutral'])
                de=result['dominant_emotion']

                if de == 'angry':
                    f=2
                elif de == 'disgust':
                    f=1
                elif de == 'fear':
                    f=0
                elif de == 'happy':
                    f=9
                elif de == 'sad':
                    f=4
                elif de == 'surprise':
                    f=10
                elif de == 'neutral':
                    f=5

                my_cursor.execute("insert into emotion(Dominant_emotion,Feedback_score,Angry,Disgust,Fear,Happy,Sad,Surprise,Neutral) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(de,str(f),ang,dis,fear,hap,sad,sur,neu))

                conn.commit()

                plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
                plt.show()
                conn.close()
                self.fetch_data() 
                messagebox.showinfo("Feeback Received:",f"Your emotion captured are: {ang}, {dis},{fear}, {hap}, {sad}, {sur} & {neu}\n Your feedback score is: {str(f)}")
                self.getGraph()

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    

if __name__=="__main__":
    root=Tk()
    obj=Emotion(root)
    root.mainloop()

        
