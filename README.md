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

A facial recognition software captures and compares patterns on a person’s face and analyses the details to identify and verify the individual. While the underlying system is complex, the whole technology can be broken down into three steps:

Face Detection: An essential step is locating human faces in real-time
Transform Data: Once captured, the analogue facial information is transformed into a set of data or vectors based on a person’s facial features
Face Match: The system matches the data above with the one in the database for verification

Face Recognition Algorithms -

Haar Cascade
LBPH (Local Binary Pattern Histogram)

	In this project it takes sample of 100 photos to detect the face and marks the attendance with time in the excel sheet.
	
*Emotion Detection*

For this I have used deepfae library.
DeepFace is a deep learning facial recognition system created by a research group at Facebook. It identifies human faces in digital images
DeepFace method reaches an accuracy of 97.35% ± 0.25% on Labeled Faces in the Wild (LFW) data set where human beings have 97.53%. This means that DeepFace is sometimes more successful than human beings.

	In this project it detects the emotion & generates a feedback score according to the *dominant emotion* of the student.
	
	After this it generates graph based on the data stored in database between number of student & feedback score
	
**Database**

I have created database  face_recognition to store data of student, queries & feedback of students in tables student, query & emotion respectively.

| ![ss1](https://user-images.githubusercontent.com/106318752/170842510-a544a72e-847a-46be-9f3c-959229747587.jpg)| ![ss2](https://user-images.githubusercontent.com/106318752/170842519-6fed76ee-932d-4723-939f-35cfb46a123b.jpeg)| ![ss3](https://user-images.githubusercontent.com/106318752/170842610-108d1d36-83d7-42bf-a9a6-8bab7c9e3f35.png)| ![ss4](https://user-images.githubusercontent.com/106318752/170842561-05af2b60-1800-4c07-8935-c45098a5b5a8.png)| 
|-|-|-|-|
| Home Page | Student Details | RFace Detection | Attendance Record |
| ![ss5](https://user-images.githubusercontent.com/106318752/170842571-00b1dc46-caa9-4d3f-999e-5e3da22de257.png))| ![ss6](https://user-images.githubusercontent.com/106318752/170842584-04009f5e-7f77-4737-8403-51f0fb9b7e97.jpeg)| ![ss7](https://user-images.githubusercontent.com/106318752/170842590-f44cd352-6b17-4943-a878-6e860556c6c3.png)| ![ss8](https://user-images.githubusercontent.com/106318752/170842595-4bae5213-e24a-4372-9f04-62454d613206.png)|
| Queris | Feedback Data| Emotion Detection | Graph to analyze feedback of students |
	

	


	

	
	



