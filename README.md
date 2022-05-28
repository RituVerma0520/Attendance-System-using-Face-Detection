# Attendance-System-using-Face-Detection
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
	

	


	

	
	



