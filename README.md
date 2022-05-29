## Attendance-System-using-Face-Detection
Facial detection based attendance system to ease the task of teachers &amp; eliminate the problem of proxies.
This project involves building an attendance system which utilizes facial recognition to mark the presence.

**Features:**
            
	1) Student management system (save Student info/Add Photo Sample, Update, Delete, Reset) 

	2) Train photo samples 

	3) Take attendance with Face Recognition 

	4) Attendance Report(Excel file/csv file) 

	5) Query page

	6)Feedback page
	
**Technology Used:** openCV (Opensource Computer Vision) -Python -tkinter GUI interface, deepface, MySQL for database

*Sample dataset in used to detect the faces.*

![user 12 26](https://user-images.githubusercontent.com/106318752/170840430-d393036a-4693-4625-89d0-92e7dcee3459.jpg)

**How does it work?**
	
*Face Recognition*

Face Recognition Algorithms -

Haar Cascade
LBPH (Local Binary Pattern Histogram)

	In this project it takes sample of 100 photos to detect the face and marks the attendance with time in the excel sheet.
	
*Emotion Detection*

For this I have used deepfae library.

	In this project it detects the emotion & generates a feedback score according to the *dominant emotion* of the student.
	
	After this it generates graph based on the data stored in database between number of student & feedback score
	
**Database**

I have created database  face_recognition to store data of student, queries & feedback of students in tables student, query & emotion respectively.

	Username-root
	Password-Test@123
	
	**Commands to create database and tables**
	create database face_recognition;
	use face_recognition;
	create table student(Department varchar(45), Course varchar(45),Year varchar(45),Semester varchar(45),Student_Id varchar(45) NOT NULL PRIMARY KEY,Name varchar(45),Roll_No varchar(45),Gender varchar(45),DOB varchar(45),Father varchar(45),Phone varchar(45),Email varchar(45),PhotoSample varchar(45));
	
	create table emotion(Feedback_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,Dominant_emotion varchar(45),Feedbck_score varchar(45),Angry varchar(45),Disgust varchar(45),Fear varchar(45),Happy varchar(45),Sad varchar(45),Surprise varchar(45),Neutral varchar(45));
	
	create table query(Query_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,Nmae varchar(45),Query varchar(1000),Answer varchar(1000));

| ![ss1](https://user-images.githubusercontent.com/106318752/170842510-a544a72e-847a-46be-9f3c-959229747587.jpg)| ![ss2](https://user-images.githubusercontent.com/106318752/170842519-6fed76ee-932d-4723-939f-35cfb46a123b.jpeg)| ![ss3](https://user-images.githubusercontent.com/106318752/170842610-108d1d36-83d7-42bf-a9a6-8bab7c9e3f35.png)| ![ss4](https://user-images.githubusercontent.com/106318752/170842561-05af2b60-1800-4c07-8935-c45098a5b5a8.png)| 
|-|-|-|-|
| Home Page | Student Details | Face Detection | Attendance Record |
| ![ss5](https://user-images.githubusercontent.com/106318752/170842571-00b1dc46-caa9-4d3f-999e-5e3da22de257.png))| ![ss6](https://user-images.githubusercontent.com/106318752/170842584-04009f5e-7f77-4737-8403-51f0fb9b7e97.jpeg)| ![ss7](https://user-images.githubusercontent.com/106318752/170842590-f44cd352-6b17-4943-a878-6e860556c6c3.png)| ![ss8](https://user-images.githubusercontent.com/106318752/170842595-4bae5213-e24a-4372-9f04-62454d613206.png)|
| Queris | Feedback Data| Emotion Detection | Graph to analyze feedback of students |
	

	


	

	
	



